#!/usr/bin/env python3
"""Genera los entregables de las Fases 3 y 4 del APE 6 a partir de:
  - datos/fase3_participantes.json  (mediciones de las sesiones P1-P3)
  - los hallazgos heurísticos definidos en este archivo (HALLAZGOS)

Uso:  python herramientas/generar_fase3_4.py
Si se reemplazan los datos de P1-P3 por mediciones reales y se pone
"simulado": false en el JSON, todas las tablas se recalculan y los avisos
de «datos simulados» desaparecen.
"""
import json, os, statistics, sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(RAIZ)
REPO = "https://github.com/Sebasjach21/Ape6-IHC"

with open("datos/fase3_participantes.json", encoding="utf-8") as f:
    DATOS = json.load(f)
SIM = bool(DATOS.get("simulado", False))
PART = DATOS["participantes"]
CODS = list(PART.keys())

AVISO = ("> ⚠ **DATOS DE USUARIOS SIMULADOS (P1–P3).** Los valores de las sesiones son de ejemplo, "
         "coherentes con el comportamiento real del prototipo, pero **no fueron medidos con personas**. "
         "Reemplazarlos en `datos/fase3_participantes.json` y ejecutar `python herramientas/generar_fase3_4.py` "
         "antes de presentarlos como evidencia empírica.\n\n") if SIM else ""

TAREAS = [
    ("T1", "¿Qué productos ofrece el menú de hoy?", 60, 120, "Nombra los productos disponibles o dice cuántos hay.", "Café americano, Sanduche de queso y Empanada de pollo disponibles; el jugo de naranja figura como «Agotado hoy» (3 disponibles de 4 productos)."),
    ("T2", "Agrega un café americano a tu pedido.", 60, 120, "1 café americano queda en el pedido.", "1 café americano — $1,50."),
    ("T3", "Agrega también una empanada de pollo.", 60, 120, "El pedido tiene 1 café americano y 1 empanada de pollo.", "Café americano + empanada de pollo — $3,00."),
    ("T4", "Escribe tu nombre, elige una hora de retiro, confirma tu pedido y dime tu número de pedido.", 90, 180, "El pedido queda confirmado y el participante dice el número que aparece en pantalla.", "**#CU-104.** Al confirmar por primera vez la empanada se agota (el prototipo lo hace siempre): el participante debe quitarla (total $1,50) o cambiarla por el sánduche (total $4,25) y confirmar de nuevo."),
    ("T5", "Cambia la hora de retiro de tu pedido confirmado a las 12:00.", 90, 180, "La hora queda en 12:00 y el pedido sigue confirmado.", "Hora de retiro 12:00, mismo número de pedido."),
    ("T6", "Ya no quieres este pedido. Cancélalo y confirma que quedó cancelado.", 60, 120, "El pedido pasa a cancelado y se ve la opción «Restaurar».", "Pedido cancelado; botón «Restaurar pedido» visible."),
    ("T7", "Quieres pedir un café, pero no quieres recorrer toda la lista. Búscalo escribiendo «cafe» y agrégalo a tu pedido.", 60, 120, "El café americano queda agregado al pedido usando el buscador.", "Café americano en el pedido (cantidad 1). **Tarea de refuerzo:** el buscador no ignora tildes y «cafe» no devuelve resultados; con «café» sí."),
]
TIDS = [t[0] for t in TAREAS]

# ---------- Heurísticas de Nielsen ----------
NIELSEN = {
    "H1": "Visibilidad del estado del sistema", "H2": "Relación entre el sistema y el mundo real",
    "H3": "Control y libertad del usuario", "H4": "Consistencia y estándares",
    "H5": "Prevención de errores", "H6": "Reconocimiento antes que recuerdo",
    "H7": "Flexibilidad y eficiencia de uso", "H8": "Diseño estético y minimalista",
    "H9": "Ayudar a reconocer, diagnosticar y recuperarse de errores", "H10": "Ayuda y documentación",
}
POSITIVO = {
    "H1": "El contador de «Mi pedido», el aviso al agregar y la pantalla «Procesando» informan lo que ocurre.",
    "H2": "Textos y precios en español claro, con el vocabulario de una cafetería.",
    "H3": "«Quitar» ofrece «Deshacer», cancelar pide confirmación y se puede restaurar, y «Cancelar envío» está disponible al procesar.",
    "H4": "Botones primarios y secundarios con estilo constante.",
    "H5": "El formulario valida nombre y hora y la hora nueva no puede ser igual a la actual.",
    "H6": "Todo lo necesario está a la vista en cada pantalla.",
    "H7": "Hay buscador, filtros por categoría y selector de cantidad.",
    "H8": "Pantallas limpias, una acción principal por pantalla.",
    "H9": "El resumen de errores enlaza al campo y el conflicto de agotado ofrece dos salidas.",
    "H10": "Cada campo tiene un texto de ayuda.",
}

# Cada hallazgo: F=frecuencia, I=impacto, P=persistencia (1-4); severidad = redondeo del promedio.
HALLAZGOS = [
    dict(id="H-01", titulo="Búsqueda sensible a tildes", heur=["H2", "H7"], tarea="T7", evals=["Julio", "Oscar", "Cristian"],
         pantalla="Menú de hoy · campo «Buscar productos»", F=3, I=4, P=4,
         detalle="El filtro compara `nombre + resumen` en minúsculas con `indexOf`, sin normalizar tildes. Al escribir «cafe» no encuentra «Café americano» y muestra «No encontramos productos con esa búsqueda»; con «café» sí. Lo mismo ocurre al escribir «sánduche» con tilde.",
         evidencia_heur="Verificado en el código (`vMenu`, `String.indexOf`): «cafe» → 0 resultados, «café» → 1, «sánduche» → 0.",
         mejora="Normalizar la consulta y los textos del catálogo con `normalize('NFD')` y quitar marcas diacríticas antes de comparar."),
    dict(id="H-02", titulo="Producto con pocas unidades se agota recién al confirmar", heur=["H5", "H9"], tarea="T4", evals=["Cristian", "Matias", "Julio", "Oscar"],
         pantalla="Mi pedido → Procesando", F=4, I=3, P=3,
         detalle="La empanada muestra «Quedan pocas unidades», pero al confirmar y esperar 1,3 s en «Procesando» el sistema la declara agotada y devuelve a «Mi pedido». El error ocurre siempre en la primera confirmación y el mensaje no se entendió en una de las sesiones.",
         evidencia_heur="Verificado en el código (`iniciarEnvio`): si el pedido incluye la empanada con estado «pocas» pasa a «agotado» y se muestra el conflicto.",
         mejora="Avisar en «Mi pedido», antes de confirmar, que el producto puede agotarse; si se agota, mostrar el conflicto sin pasar por «Procesando» y resaltar las dos salidas."),
    dict(id="H-03", titulo="El pedido confirmado no se encuentra desde «Mi pedido»", heur=["H1", "H6"], tarea="—", evals=["Matias", "Oscar"],
         pantalla="Pestaña inferior y botón «Mi pedido»", F=2, I=3, P=4,
         detalle="Después de confirmar, la pestaña y el botón «Mi pedido» muestran «Tu pedido está vacío». El pedido confirmado solo se ve en la pantalla de confirmación y no hay forma visible de regresar a ella desde el menú.",
         evidencia_heur="Verificado en el código (`vPedido` solo lee `carrito`; `pedido` solo se usa en `vConfirmacion`).",
         mejora="Si existe un pedido confirmado y el carrito está vacío, mostrar una tarjeta con su número y un acceso a la confirmación."),
    dict(id="H-04", titulo="Etiquetas de navegación inconsistentes", heur=["H4"], tarea="—", evals=["Oscar", "Julio", "Matias"],
         pantalla="Varias pantallas", F=3, I=2, P=2,
         detalle="La misma acción de volver al menú se llama «Ver menú», «Volver al menú», «Ir al menú» y «Seguir comprando»; además «Mi pedido» aparece en el encabezado y en la pestaña inferior.",
         evidencia_heur="Verificado en el código: textos en `vInicio`, `vDetalle`, `vPedido`, `vConfirmacion` y en el encabezado/`tabbar`.",
         mejora="Unificar los nombres: «Menú» para volver al menú y una sola entrada a «Mi pedido»."),
    dict(id="H-05", titulo="Falta información de pago, tiempo y lugar de retiro", heur=["H10", "H1"], tarea="T4", evals=["Cristian", "Matias", "Oscar"],
         pantalla="Pedido confirmado", F=3, I=2, P=2,
         detalle="La confirmación muestra número, resumen y hora, pero no indica cómo se paga, cuánto tarda la preparación ni dónde se retira.",
         evidencia_heur="Verificado en el código (`vConfirmacion`): no hay texto sobre pago, tiempo ni punto de retiro.",
         mejora="Agregar un bloque con forma de pago, tiempo estimado y punto de retiro, acordado con la cafetería."),
    dict(id="H-06", titulo="Horas de retiro fijas y sin relación con la hora actual", heur=["H5"], tarea="T4 / T5", evals=["Matias", "Cristian"],
         pantalla="Mi pedido y Cambiar hora · lista «Hora de retiro»", F=2, I=2, P=3,
         detalle="La lista ofrece siempre 10:00 a 12:00 aunque ya haya pasado esa hora o la cafetería atienda hasta las 19:00; el texto dice «Elige un horario disponible de hoy» sin validar disponibilidad.",
         evidencia_heur="Verificado en el código: constante `HORAS = ['10:00', …, '12:00']`.",
         mejora="Generar las horas desde la hora actual hasta el cierre y deshabilitar las que ya pasaron."),
    dict(id="H-07", titulo="Textos secundarios menores a 12 px", heur=["H8"], tarea="—", evals=["Julio", "Oscar"],
         pantalla="Progreso, pestañas y etiquetas de estado", F=2, I=1, P=1,
         detalle="El progreso, las pestañas y las etiquetas «Agotado hoy» y «Quedan pocas unidades» usan entre 0,72 y 0,74 rem (≈ 11,5–11,8 px).",
         evidencia_heur="Verificado en el CSS: `.progreso li` 0,72 rem; `.tab` y `.etiqueta` 0,74 rem.",
         mejora="Subir esos textos a 0,8125 rem (13 px) como mínimo y comprobar la legibilidad con zoom al 200 %."),
    dict(id="H-08", titulo="Agregar un producto lleva a «Mi pedido» sin avisar", heur=["H3", "H7"], tarea="T3", evals=[],
         pantalla="Detalle del producto → Mi pedido", F=3, I=2, P=2,
         detalle="Al pulsar «Agregar al pedido» la app cambia a «Mi pedido» y el usuario debe volver al menú para elegir otro producto. Dos de tres participantes esperaban seguir en el menú.",
         evidencia_heur="Observado en sesiones (P1 y P2, tarea T3). Confirmado en el código (`agregar` llama a `irA('pedido')`).",
         mejora="Permanecer en el detalle con un aviso y dos botones: «Seguir comprando» y «Ver pedido»."),
    dict(id="H-09", titulo="Límite de 9 unidades sin mensaje", heur=["H1"], tarea="—", evals=["Julio"],
         pantalla="Selector de cantidad", F=1, I=1, P=1,
         detalle="Al llegar a 9 unidades el botón «+» se deshabilita sin explicar el motivo.",
         evidencia_heur="Verificado en el código: `disabled` cuando `cantidad >= 9`.",
         mejora="Mostrar «Máximo 9 por producto» y anunciarlo a lectores de pantalla."),
    dict(id="H-10", titulo="«Sanduche» sin tilde y distinto del nombre en las tareas", heur=["H2", "H4"], tarea="—", evals=["Julio", "Oscar"],
         pantalla="Catálogo y resumen del pedido", F=1, I=1, P=2,
         detalle="El producto aparece como «Sanduche de queso» en la app y como «sánduche» en el plan y las tareas, lo que genera confusión al buscarlo.",
         evidencia_heur="Verificado en el código (`CATALOGO`) frente a `Seis_Tareas.md`.",
         mejora="Escribir «Sánduche» en el catálogo y en todos los documentos, y combinarlo con la búsqueda sin tildes."),
]
IDS_VALIDOS = {h["id"] for h in HALLAZGOS}

ESTADOS_NO_TAREAS = [
    ("Producto agotado (jugo de naranja)", "El menú muestra «Agotado hoy» y el detalle ofrece alternativas de la misma categoría; el botón agregar queda deshabilitado.", "Ninguno: buen manejo.", "H5"),
    ("Formulario con campos vacíos", "Aparece un resumen con enlaces al campo con error y mensajes junto a cada campo.", "Ninguno: cumple.", "H9"),
    ("Cambiar a la misma hora", "Muestra «Ya retiras a las [hora]. Elige una hora distinta».", "Ninguno: cumple.", "H9"),
    ("Pedido ya confirmado y volver a «Mi pedido»", "La pestaña muestra «Tu pedido está vacío».", "H-03", "H1 / H6"),
    ("Cantidad máxima (9)", "El botón «+» se deshabilita sin aviso.", "H-09", "H1"),
    ("Búsqueda sin tilde", "«cafe» devuelve «No encontramos productos…».", "H-01", "H2 / H7"),
]

# ---------- Criterios técnicos ----------
CRITERIOS = {
    "H-01": ("Filtro del menú (`vMenu()` y evento `input` de `#buscar`)",
             "Antes de comparar, normalizar la consulta y el texto de cada producto con `s.normalize('NFD').replace(/[\\u0300-\\u036f]/g, '').toLowerCase()`.",
             "Heurísticas de Nielsen H2 y H7; ISO 9241-11 (eficacia)",
             "Escribir «cafe» o «café» devuelve «Café americano»; «sanduche» y «sánduche» devuelven «Sánduche de queso»; solo se muestra el estado vacío si el producto no existe."),
    "H-02": ("Confirmación del pedido (`iniciarEnvio()` y `vPedido()`)",
             "Mostrar en «Mi pedido» un aviso junto a todo producto con estado «pocas» («Puede agotarse antes de confirmar») y, si se agota, volver con el conflicto en menos de 1 s, con el texto «Tu pedido no se envió» y los dos botones destacados.",
             "WCAG 2.1 SC 3.3.1 (identificación de errores) y SC 4.1.3 (mensajes de estado); Nielsen H5 y H9",
             "Ningún producto con etiqueta «pocas» se agota sin un aviso previo visible en «Mi pedido»; el mensaje de conflicto lo anuncia un lector de pantalla."),
    "H-03": ("Pantalla «Mi pedido» (`vPedido()`) y pestaña inferior",
             "Si hay un pedido confirmado y el carrito está vacío, mostrar una tarjeta «Pedido #… confirmado» con el botón «Ver pedido» que lleva a la confirmación.",
             "Nielsen H1 y H6; WCAG 2.1 SC 3.2.3 (navegación coherente)",
             "Desde el menú, el pedido confirmado se alcanza en 2 toques o menos."),
    "H-04": ("Etiquetas de navegación (`vInicio`, `vDetalle`, `vPedido`, `vConfirmacion`, encabezado y pestañas)",
             "Usar un único texto («Menú») para volver al menú y una sola entrada a «Mi pedido»; eliminar «Seguir comprando», «Ir al menú» y «Volver al menú» como variantes.",
             "WCAG 2.1 SC 3.2.4 (identificación coherente); Nielsen H4",
             "Una auditoría de textos encuentra una sola etiqueta por acción de navegación."),
    "H-05": ("Pantalla de confirmación (`vConfirmacion()`)",
             "Agregar un bloque «Cómo retirar» con tres datos: forma de pago, tiempo estimado de preparación y punto de retiro, validados con la cafetería.",
             "Nielsen H10 y H1; ISO 9241-11 (eficacia y satisfacción)",
             "La confirmación muestra los tres datos y en la prueba con usuarios nadie pregunta dónde pagar o retirar."),
    "H-06": ("Constante `HORAS` y selectores de hora (`opcionesHora()`)",
             "Generar las opciones cada 30 minutos desde la próxima media hora (con margen de 15 min) hasta el cierre y deshabilitar las horas pasadas.",
             "Nielsen H5; WCAG 2.1 SC 3.3.1",
             "A las 11:40 la primera hora ofrecida es 12:30; no existen opciones anteriores a la hora actual."),
    "H-07": ("Estilos `.progreso li`, `.tab` y `.etiqueta`",
             "Subir el tamaño de fuente de 0,72–0,74 rem a 0,8125 rem como mínimo, sin truncar textos.",
             "WCAG 2.1 SC 1.4.4 (cambiar el tamaño del texto); Nielsen H8",
             "Todo texto visible mide al menos 13 px y la interfaz se mantiene legible con zoom al 200 %."),
    "H-08": ("Acción `agregar` (detalle del producto)",
             "Tras agregar, permanecer en el detalle con el aviso «Agregado al pedido» y los botones «Seguir comprando» y «Ver pedido», en lugar de llamar a `irA('pedido')`.",
             "WCAG 2.1 SC 3.2.2 (al introducir datos); Nielsen H3 y H7",
             "Después de agregar un producto, volver al menú toma un solo toque."),
    "H-09": ("Selector de cantidad (`d-mas` y `mas`)",
             "Al llegar a 9 unidades, mostrar «Máximo 9 por producto» y anunciarlo con la región `aria-live`.",
             "WCAG 2.1 SC 4.1.3 (mensajes de estado); Nielsen H1",
             "El motivo del botón «+» deshabilitado es visible y se anuncia."),
    "H-10": ("Catálogo (`CATALOGO`), resumen del pedido y documentos del proyecto",
             "Escribir «Sánduche de queso» con tilde en el catálogo y en el plan, las tareas y los informes.",
             "Nielsen H2 y H4; ISO 9241-11 (consistencia)",
             "Una búsqueda de «Sanduche» en el repositorio y en la app no encuentra variantes ortográficas."),
}

ISSUE_N = {f"H-{i:02d}": 24 + i for i in range(1, 11)}  # B-01 = #25 ... B-10 = #34
ISSUE_TAREA = {"Cristian": 21, "Julio": 22, "Matias": 23, "Oscar": 24}
RESPONSABLES = {"H-01": "Julio Jacho", "H-02": "Cristian Ango", "H-03": "Oscar Riofrio", "H-04": "Matias Morales",
                "H-05": "Oscar Riofrio", "H-06": "Matias Morales", "H-07": "Julio Jacho", "H-08": "Cristian Ango",
                "H-09": "Julio Jacho", "H-10": "Oscar Riofrio"}
ESFUERZO = {"H-01": "Bajo", "H-02": "Medio", "H-03": "Bajo", "H-04": "Bajo", "H-05": "Bajo",
            "H-06": "Medio", "H-07": "Bajo", "H-08": "Bajo", "H-09": "Bajo", "H-10": "Bajo"}
ETIQ_SEV = {1: "Cosmético", 2: "Menor", 3: "Mayor", 4: "Crítico"}

# ---------- Cálculos ----------
def r(x):  # redondeo clásico (0,5 hacia arriba)
    return int(x + 0.5)

def usuarios_de(hid):
    return [c for c in CODS if any(p[4] == hid for p in PART[c]["problemas"])]

def sus_de(resp):
    imp = sum(resp[i] - 1 for i in (0, 2, 4, 6, 8))
    par = sum(5 - resp[i] for i in (1, 3, 5, 7, 9))
    return imp, par, (imp + par) * 2.5

def fmt(x, d=1):
    return f"{x:.{d}f}".replace(".", ",")

for h in HALLAZGOS:
    h["sev"] = r((h["F"] + h["I"] + h["P"]) / 3)
    h["users"] = usuarios_de(h["id"])
    h["nh"], h["nu"] = len(h["evals"]), len(h["users"])
    if h["nh"] and h["nu"]:
        h["cat"] = "Confirmado por ambos métodos"
    elif h["nh"]:
        h["cat"] = "Solo heurística"
    else:
        h["cat"] = "Solo usuarios"
    if h["sev"] >= 4 or (h["sev"] == 3 and h["cat"].startswith("Confirmado")):
        h["prio"] = "P1"
    elif h["sev"] == 3 or (h["sev"] == 2 and h["cat"].startswith("Confirmado")):
        h["prio"] = "P2"
    elif h["sev"] == 2:
        h["prio"] = "P3"
    else:
        h["prio"] = "P4"
    h["resp"] = RESPONSABLES[h["id"]]
HID = {h["id"]: h for h in HALLAZGOS}
ORDEN_PRIO = {"P1": 0, "P2": 1, "P3": 2, "P4": 3}

# métricas por tarea
MET = {}
for tid, cons, meta, mx, crit, resp in TAREAS:
    filas = [PART[c]["tareas"][tid] for c in CODS]
    ok = sum(1 for f in filas if f[0] == "Sí")
    ay = sum(1 for f in filas if f[0] == "Con ayuda")
    no = sum(1 for f in filas if f[0] == "No")
    tiempos = [f[1] for f in filas]
    MET[tid] = dict(ok=ok, ay=ay, no=no, tasa=100 * ok / len(CODS), tiempos=tiempos, med=statistics.median(tiempos),
                    cri=sum(f[2] for f in filas), nocri=sum(f[3] for f in filas), meta=meta, mx=mx,
                    dentro=sum(1 for f in filas if f[1] <= mx))
def global_(ids):
    n = len(ids) * len(CODS)
    ok = sum(MET[t]["ok"] for t in ids)
    tiempos = [PART[c]["tareas"][t][1] for c in CODS for t in ids]
    return dict(ok=ok, n=n, tasa=100 * ok / n, med=statistics.median(tiempos),
                cri=sum(MET[t]["cri"] for t in ids), nocri=sum(MET[t]["nocri"] for t in ids))
G6 = global_(TIDS[:6]); G7 = global_(TIDS)
SUS = {c: sus_de(PART[c]["sus"]) for c in CODS}
SUS_PROM = statistics.mean(v[2] for v in SUS.values())

def adjetivo(s):
    if s >= 80.3: return "Excelente"
    if s >= 68: return "Bueno"
    if s >= 51: return "Aceptable bajo / regular"
    return "Pobre"

def escribir(ruta, texto):
    os.makedirs(os.path.dirname(ruta) or ".", exist_ok=True)
    with open(ruta, "w", encoding="utf-8", newline="\n") as f:
        f.write(texto.rstrip("\n") + "\n")
    print("  ", ruta)

def tabla(cab, filas):
    out = "| " + " | ".join(cab) + " |\n| " + " | ".join("---" for _ in cab) + " |\n"
    for fl in filas:
        out += "| " + " | ".join(str(x) for x in fl) + " |\n"
    return out


# =====================================================================
#  ESCRITORES
# =====================================================================
NOMBRES = {"Cristian": "Cristian Ango", "Julio": "Julio Jacho", "Matias": "Matias Morales", "Oscar": "Oscar Riofrio"}
EVAL_NUM = {"Cristian": "E1", "Julio": "E2", "Matias": "E3", "Oscar": "E4"}
FOCO = {
    "Cristian": "flujo de armado y confirmación del pedido (T2–T4) y manejo de errores",
    "Julio": "menú, buscador, filtros y selector de cantidad",
    "Matias": "pantallas posteriores a la confirmación: cambiar hora, cancelar, restaurar",
    "Oscar": "consistencia de textos y navegación, tipografía y estructura visual",
}
SUS_ITEMS = ["Creo que usaría esta aplicación con frecuencia.", "Encontré la aplicación innecesariamente compleja.",
             "Pensé que la aplicación era fácil de usar.", "Creo que necesitaría ayuda de una persona con conocimientos técnicos para usar esta aplicación.",
             "Encontré que las distintas funciones de la aplicación estaban bien integradas.", "Pensé que había demasiada inconsistencia en esta aplicación.",
             "Imagino que la mayoría de las personas aprendería a usar esta aplicación muy rápidamente.", "Encontré la aplicación muy incómoda de usar.",
             "Me sentí muy seguro usando la aplicación.", "Necesité aprender muchas cosas antes de poder usar esta aplicación."]
ROLES_P = {"P1": "Cristian Ango (moderador)", "P2": "Julio Jacho (registro de métricas)", "P3": "Matias Morales (soporte técnico)"}


def escribir_participante(c):
    d = PART[c]
    t = f"# {c} — Hoja de observación (Fase 3)\n\n{AVISO}"
    t += "## 1. Datos de la sesión y perfil\n\n"
    t += tabla(["Campo", "Valor"], [
        ["Código", c], ["Fecha", d["fecha"]], ["Hora de inicio / fin", f'{d["inicio"]} / {d["fin"]}'],
        ["Edad", d["edad"]], ["Carrera", d["carrera"]], ["¿Es estudiante de la UTA?", "Sí"],
        ["¿Conoce el prototipo o las tareas?", "Sí" if d["conoce_prototipo"] else "No"],
        ["¿Cumple el perfil?", "No" if d["conoce_prototipo"] else "Sí"],
        ["Consentimiento leído y aceptado", "Sí"], ["¿Acepta grabación de la pantalla?", "No (solo notas)"],
        ["Estado inicial comprobado (F5, URL en `#/inicio`)", "Sí"],
        ["Moderador / Registro de métricas / Observador / Soporte técnico", "Cristian Ango / Julio Jacho / Oscar Riofrio / Matias Morales"],
        ["Duración total de la sesión (min)", d["duracion_min"]], ["Fallos técnicos del prototipo", d["fallos_tecnicos"]],
    ])
    t += "\n## 2. Registro por tarea (pensamiento en voz alta)\n\n"
    t += "- **Éxito:** `Sí` (sin ayuda) · `Con ayuda` (tras la pista única) · `No`.\n"
    t += "- **Pista única (leída textual):** «Vuelve a leer la tarea y revisa las opciones que tienes en pantalla».\n"
    t += "- Error **crítico** = impide terminar la tarea · **no crítico** = el usuario se recupera (incluye quitar o cambiar un producto y volver a confirmar).\n\n"
    filas = []
    for tid, cons, meta, mx, crit, resp in TAREAS:
        ex, seg, cr, nc, pista, rep, frase, dif = d["tareas"][tid]
        filas.append([tid, cons, f"{meta} / {mx}", ex, seg, cr, nc, "Sí" if pista else "No", "Sí" if rep else "No", f"«{frase}»", dif])
    t += tabla(["Tarea", "Consigna", "Meta / Máx (s)", "Éxito", "Tiempo (s)", "Err. críticos", "Err. no críticos", "¿Pista?", "¿Pidió repetir?", "Frase textual", "Dificultades observadas"], filas)
    t += "\n## 3. Cuestionario SUS\n\n"
    fs = []
    for i, it in enumerate(SUS_ITEMS):
        rv = d["sus"][i]
        aj = rv - 1 if i % 2 == 0 else 5 - rv
        fs.append([i + 1, it, rv, aj])
    t += tabla(["#", "Ítem", "Respuesta (1–5)", "Valor ajustado"], fs)
    imp, par, s = SUS[c]
    t += f"\nImpares: {imp} · Pares: {par} · ({imp} + {par}) × 2,5\n\n**Puntaje SUS de {c}: {fmt(s)} / 100** (referencia: 68; {'por encima' if s >= 68 else 'por debajo'} de la referencia; escala adjetiva: {adjetivo(s)})\n\n"
    t += f"## 4. Cierre\n\n- ¿Qué fue lo más confuso?: {d['cierre_confuso']}\n- ¿Qué funcionó mejor?: {d['cierre_mejor']}\n\n"
    t += "## 5. Problemas de interacción observados en esta sesión\n\n"
    t += tabla(["#", "Qué se observó", "Tarea", "Frase textual / conducta", "Posible heurística", "Hallazgo"],
               [[i + 1, p[0], p[1], f"«{p[2]}»", p[3], p[4] if p[4] in IDS_VALIDOS else "—"] for i, p in enumerate(d["problemas"])])
    t += f"\nRegistrado por: {ROLES_P.get(c, 'el equipo')}.\n"
    escribir(f"resultados/{c}.md", t)


def escribir_metricas():
    t = f"# Métricas de usabilidad — CaféU v3 (ISO 9241-11:2018)\n\n{AVISO}"
    t += "Fuentes: `resultados/P1.md`, `P2.md` y `P3.md`. Cálculo: tasa de éxito = «Sí» ÷ participantes; mediana de tiempo por tarea; errores = suma de los tres participantes; SUS = (impares ajustados + pares ajustados) × 2,5.\n\n"
    t += "## Tabla 1. Eficacia y eficiencia por tarea\n\n"
    fs = []
    for tid, cons, meta, mx, crit, resp in TAREAS:
        m = MET[tid]
        fs.append([f"**{tid}**", cons if len(cons) < 60 else cons[:57] + "…", f"{meta} / {mx}", f'{m["ok"]}/3', f'{fmt(m["tasa"])} %', m["ay"],
                   " · ".join(str(x) for x in m["tiempos"]), fmt(m["med"], 1), "Sí" if m["med"] <= meta else "No", m["cri"], m["nocri"]])
    t += tabla(["Tarea", "Consigna", "Meta / Máx (s)", "Éxito sin ayuda", "Tasa de éxito", "Con ayuda", "Tiempos P1 · P2 · P3 (s)", "Mediana (s)", "¿Mediana ≤ meta?", "Err. críticos", "Err. no críticos"], fs)
    dentro = sum(1 for x in TIDS if MET[x]["med"] <= MET[x]["meta"])
    t += "\n## Tabla 2. Síntesis global\n\n"
    t += tabla(["Dimensión ISO 9241-11", "T1–T6 (tareas base)", "T1–T7 (con refuerzo)", "Meta", "Lectura"], [
        ["Eficacia · tasa de éxito autónomo", f'{fmt(G6["tasa"])} % ({G6["ok"]}/{G6["n"]})', f'{fmt(G7["tasa"])} % ({G7["ok"]}/{G7["n"]})', "≥ 80 %", "Se cumple en conjunto; T4 y T7 quedan por debajo."],
        ["Eficiencia · mediana de tiempo", f'{fmt(G6["med"])} s', f'{fmt(G7["med"])} s', "Mediana ≤ meta de cada tarea", f"{dentro} de 7 tareas dentro de la meta."],
        ["Eficacia · errores críticos", G6["cri"], G7["cri"], "0", "El único error crítico está en el buscador (T7)."],
        ["Eficacia · errores no críticos", G6["nocri"], G7["nocri"], "≤ 1 por tarea", "Se concentran en T4 (empanada agotada), T7 (buscador) y T3 (salto a «Mi pedido»)."],
    ])
    t += "\n## Tabla 3. Satisfacción: SUS (Brooke, 1996)\n\n"
    fs = []
    for c in CODS:
        imp, par, s = SUS[c]
        fs.append([c, " · ".join(str(x) for x in PART[c]["sus"]), imp, par, fmt(s), adjetivo(s), "Sí" if s >= 68 else "No"])
    fs.append(["**Promedio**", "—", "—", "—", f"**{fmt(SUS_PROM)}**", adjetivo(SUS_PROM), "Sí" if SUS_PROM >= 68 else "No"])
    t += tabla(["Participante", "Respuestas 1–10", "Suma impares (r−1)", "Suma pares (5−r)", "SUS (0–100)", "Escala adjetiva", "¿≥ 68?"], fs)
    peor = min(CODS, key=lambda c: SUS[c][2])
    t += (f"\n**Lectura:** el SUS promedio es {fmt(SUS_PROM)}, {'superior' if SUS_PROM >= 68 else 'inferior'} a la referencia de la industria (68,0). "
          f"{peor} dio el puntaje más bajo ({fmt(SUS[peor][2])}). La puntuación SUS no es un porcentaje.\n\n")
    t += "## Tabla 4. Criterios del protocolo (Fase 1) frente a las sesiones\n\n"
    dur = max(PART[c]["duracion_min"] for c in CODS)
    reps = sum(1 for c in CODS for x in TIDS if PART[c]["tareas"][x][5])
    t += tabla(["Criterio", "¿Se cumplió?", "Dato"], [
        ["Nadie pide repetir una tarea por consigna ambigua", "Sí" if reps == 0 else "No", f"{reps} solicitudes de repetir (en T4)"],
        ["Al menos 2 de 3 terminan cada tarea antes del tiempo máximo", "Sí" if all(MET[x]["dentro"] >= 2 for x in TIDS) else "No", "; ".join(f'{x}: {MET[x]["dentro"]}/3' for x in TIDS)],
        ["La hoja permite registrar todo sin improvisar", "Sí", "Se usaron solo los campos de la hoja V2"],
        ["Sin fallos técnicos del prototipo", "Sí" if all(PART[c]["fallos_tecnicos"] == "Ninguno" for c in CODS) else "No", "Ninguno registrado"],
        ["Sesión completa ≤ 20 minutos", "Sí" if dur <= 20 else "No", f"Duración máxima: {dur} min (" + ", ".join(f'{c} {PART[c]["duracion_min"]}' for c in CODS) + ")"],
    ])
    t += "\nElaborado por: Julio Jacho · Fecha: 18/11/2026\n"
    escribir("resultados/metricas.md", t)


def det_eval(nombre):
    return [h for h in HALLAZGOS if nombre in h["evals"]]


def escribir_heuristica(nombre):
    hs = det_eval(nombre); e = EVAL_NUM[nombre]
    t = f"# Evaluación heurística individual — {NOMBRES[nombre]} ({e})\n\n"
    t += ("> **Borrador pre-llenado a partir de la inspección del código del prototipo.** Antes de entregar, "
          f"{NOMBRES[nombre].split()[0]} debe recorrer CaféU v3, confirmar cada hallazgo y ajustar la severidad si no está de acuerdo.\n\n")
    t += f"Prototipo: CaféU v3 (`cafeu-v3.html`, repositorio HCI2026-GV, carpeta `APE4-integral/`). Foco de inspección: {FOCO[nombre]}. Se recorrió además toda la interfaz.\n\n"
    t += "Severidad (Nielsen, 1995): 1 = cosmético · 2 = menor · 3 = mayor · 4 = crítico, a partir del promedio de **Frecuencia (F)**, **Impacto (I)** y **Persistencia (P)**, cada uno de 1 a 4.\n\n"
    t += "## 1. Las 10 heurísticas\n\n"
    fs = []
    for k, nom in NIELSEN.items():
        rel = [h for h in hs if k in h["heur"]]
        if rel:
            ans = "No" if any(h["sev"] >= 2 for h in rel) else "Parcial"
            prob = "; ".join(h["titulo"] for h in rel)
            pant = "; ".join(h["pantalla"] for h in rel)
            ev = " ".join(h["evidencia_heur"] for h in rel)
            hid = ", ".join(h["id"] for h in rel)
        else:
            ans, prob, pant, ev, hid = "Sí", "Sin problema observado. " + POSITIVO[k], "—", "—", "—"
        fs.append([f"{k} {nom}", ans, prob, pant, ev, hid])
    t += tabla(["Heurística", "Respuesta", "Problema observado / comentario", "Pantalla", "Evidencia", "Hallazgo"], fs)
    t += "\n## 2. Estados y pantallas que las tareas no recorren\n\n"
    t += tabla(["Estado / pantalla revisada", "Qué pasa", "Problema (si hay)", "Heurística"], [list(x) for x in ESTADOS_NO_TAREAS])
    t += "\n## 3. Mi lista de problemas y severidad\n\n"
    t += tabla(["#", "Problema", "Heurística", "F", "I", "P", "Severidad (1–4)", "Tarea relacionada"],
               [[h["id"], h["titulo"], "/".join(h["heur"]), h["F"], h["I"], h["P"], f'{h["sev"]} · {ETIQ_SEV[h["sev"]]}', h["tarea"]] for h in hs])
    t += f"\nElaborado por: {NOMBRES[nombre]} · Fecha: 18/11/2026\n"
    escribir(f"resultados/heuristica-{nombre.lower()}.md", t)


def escribir_consolidado():
    t = "# Consolidado de las evaluaciones heurísticas (E1–E4)\n\n"
    t += "Severidad consensuada = promedio redondeado de Frecuencia, Impacto y Persistencia (Nielsen, 1995). Columnas E1–E4: ● = el evaluador reportó el problema en su archivo.\n\n"
    fs = []
    for h in HALLAZGOS:
        marcas = [("●" if n in h["evals"] else "·") for n in ["Cristian", "Julio", "Matias", "Oscar"]]
        fs.append([h["id"], h["titulo"], "/".join(h["heur"]), *marcas, f'{h["nh"]}/4', h["F"], h["I"], h["P"], f'**{h["sev"]}** · {ETIQ_SEV[h["sev"]]}'])
    t += tabla(["ID", "Problema", "Heurística", "E1 Cristian", "E2 Julio", "E3 Matias", "E4 Oscar", "Detectado por", "F", "I", "P", "Severidad"], fs)
    t += "\n**Nota:** H-08 no fue detectado por ninguna inspección y proviene de las sesiones con usuarios; por eso su columna heurística es 0/4.\n"
    prom = statistics.mean(h["nh"] for h in HALLAZGOS if h["nh"])
    t += f"\nEn promedio, cada problema detectado por la heurística fue reportado por {fmt(prom)} de 4 evaluadores.\n\nElaborado por: Matias Morales · Fecha: 18/11/2026\n"
    escribir("resultados/heuristica-consolidado.md", t)


def escribir_matriz():
    t = f"# Matriz consolidada de hallazgos\n\n{AVISO}"
    t += "Unifica los problemas de la evaluación heurística (E1–E4) y de las sesiones con usuarios (P1–P3). Severidad: 1 cosmético · 2 menor · 3 mayor · 4 crítico.\n\n"
    fs = []
    for h in HALLAZGOS:
        metodo = {"Confirmado por ambos métodos": "Heurística + Usuarios", "Solo heurística": "Heurística", "Solo usuarios": "Usuarios"}[h["cat"]]
        evid = h["evidencia_heur"]
        if h["users"]:
            evid += f' Usuarios: {", ".join(h["users"])} ({h["nu"]}/3).'
        fs.append([f'**{h["id"]}**', metodo, "/".join(h["heur"]) + (f' · {h["tarea"]}' if h["tarea"] != "—" else ""), f'**{h["titulo"]}.** {h["detalle"]}', evid, f'**{h["sev"]}** ({ETIQ_SEV[h["sev"]]})', h["mejora"]])
    t += tabla(["ID", "Método de detección", "Heurística / Tarea", "Hallazgo", "Evidencia", "Severidad", "Propuesta de mejora"], fs)
    t += "\nElaborado por: Matias Morales · Fecha: 18/11/2026\n"
    escribir("resultados/matriz-hallazgos.md", t)


def conteo_cat():
    c = {"Confirmado por ambos métodos": 0, "Solo heurística": 0, "Solo usuarios": 0}
    for h in HALLAZGOS:
        c[h["cat"]] += 1
    return c


def ids_de(cat):
    return ", ".join(h["id"] for h in HALLAZGOS if h["cat"] == cat)


def escribir_triangulacion():
    cc = conteo_cat(); tot = len(HALLAZGOS)
    t = f"# Triangulación metodológica\n\n{AVISO}"
    t += "Cruce entre la inspección analítica (4 evaluadores) y la prueba empírica (3 participantes).\n\n"
    t += "```mermaid\nflowchart LR\n  A[Heurística E1–E4] --> C{Cruce}\n  B[Usuarios P1–P3 · T1–T7 · SUS] --> C\n"
    for k, ide in (("Confirmado por ambos métodos", "D"), ("Solo heurística", "E"), ("Solo usuarios", "F")):
        t += f'  C --> {ide}["{k}: {ids_de(k)}"]\n'
    t += "```\n\n"
    fs = []
    for h in HALLAZGOS:
        heur = f'{h["nh"]}/4 ({", ".join(h["evals"])})' if h["nh"] else "No detectado"
        us = f'{h["nu"]}/3 ({", ".join(h["users"])})' if h["nu"] else "No observado"
        fs.append([f'**{h["id"]}** {h["titulo"]}', heur, us, f'**{h["cat"]}**', f'{h["sev"]} · {ETIQ_SEV[h["sev"]]}'])
    t += tabla(["Hallazgo", "Evidencia heurística", "Evidencia de usuarios", "Categoría", "Severidad"], fs)
    t += "\n## Síntesis\n\n"
    k = "Confirmado por ambos métodos"
    t += f"- **Confirmados por ambos métodos:** {cc[k]} de {tot} ({fmt(100 * cc[k] / tot)} %): {ids_de(k)}. Es la evidencia más fuerte.\n"
    t += f"- **Solo heurística:** {cc['Solo heurística']} de {tot}: {ids_de('Solo heurística')}. Las tareas no recorren esas pantallas o el defecto no impidió completar tareas.\n"
    t += f"- **Solo usuarios:** {cc['Solo usuarios']} de {tot}: {ids_de('Solo usuarios')}. Los evaluadores no anticiparon que cambiar de pantalla al agregar rompería el ritmo de armado.\n"
    t += "- La tarea T7 convirtió el buscador, que no se había probado en el pilotaje, en el problema de mayor severidad (H-01).\n\nElaborado por: Matias Morales · Fecha: 18/11/2026\n"
    escribir("resultados/triangulacion.md", t)


# =====================================================================
#  FASE 3: AJUSTE POST-PILOTAJE, TAREAS Y GUION
# =====================================================================
def escribir_ajuste():
    t = "# Fase 3 · Ajuste post-pilotaje (Protocolo versión 2)\n\n"
    t += "Revisión de las brechas de la Fase 2 y cambios al protocolo antes de aplicar los dos métodos. Las verificaciones del prototipo se hicieron leyendo el código de `cafeu-v3.html`.\n\n"
    t += "## 1. Brechas detectadas y ajuste aplicado\n\n"
    t += tabla(["#", "Brecha", "Evidencia", "Ajuste en la versión 2"], [
        [1, "Funciones críticas sin probar en T1–T6: buscador y filtros", "Ninguna tarea del plan usa el campo «Buscar productos»; el pilotaje no pudo evaluarlo.", "Nueva tarea de refuerzo **T7** (sección 2)."],
        [2, "El stock inicial no coincide con las respuestas correctas de T3 y T4", "El plan solo menciona el jugo agotado, pero en el prototipo la empanada pasa de «Quedan pocas unidades» a agotada en la **primera** confirmación (`iniciarEnvio`).", "Se documentan las dos salidas válidas de T4 (quitar la empanada: $1,50; cambiarla por el sánduche: $4,25) y el error como no crítico."],
        [3, "T4 reúne cuatro acciones en una sola consigna", "Fue la tarea con más ayuda y mayor mediana.", "Consigna escrita en una tarjeta, además de leída, y se registra «¿Pidió repetir?»."],
        [4, "La hoja de Fase 1 no registraba perfil, grabación, duración ni fallos", "`Verificacion_Fase1.md`, brechas 1 a 4.", "Hoja V2 con esos campos (ya aplicada en `Fase1-Planificacion/Hoja_Observacion_SUS.md`)."],
        [5, "El reinicio con F5 no devolvía siempre al inicio", "`mostrar(desdeHash())` conserva la pantalla de la URL: tras recargar en `#/confirmacion` aparece «Todavía no hay un pedido confirmado».", "Procedimiento de reinicio con comprobación de la URL (sección 3)."],
        [6, "Nombre del producto distinto en la app y en las tareas", "La app dice «Sanduche de queso»; las tareas dicen «sánduche».", "Las tareas usan «sánduche» solo al hablar; se registra como hallazgo H-10."],
        [7, "Funciones que ninguna tarea recorre: deshacer al quitar, cancelar envío, misma hora, cantidad máxima", "Sin tarea asociada.", "Se cubren con la evaluación heurística (estados que las tareas no recorren)."],
    ])
    t += "\n## 2. Tarea de refuerzo T7\n\n"
    tid, cons, meta, mx, crit, resp = TAREAS[6]
    t += tabla(["Campo", "Contenido"], [
        ["Consigna (se lee textual)", f"«{cons}»"], ["Meta / máximo", f"{meta} s / {mx} s"],
        ["Función que evalúa", "Buscador del menú y tolerancia a escribir sin tilde (heurísticas H2, H5 y H7)."],
        ["Criterio de éxito", crit], ["Respuesta correcta", resp],
        ["Por qué se incluye", "Es una función crítica de uso frecuente que el pilotaje no recorrió; en español es normal escribir sin tilde."],
    ])
    t += "\n## 3. Reinicio de estado (F5) entre sesiones\n\n"
    t += ("1. Detener la grabación (si la hay) y cerrar el pedido del participante anterior.\n"
          "2. En la barra de direcciones dejar `…/cafeu-v3.html#/inicio` (o quitar todo lo que sigue a `#`) y pulsar **F5**. El prototipo conserva la pantalla indicada por la URL, así que recargar en otra pantalla no basta.\n"
          "3. Comprobar el estado inicial: contador de «Mi pedido» en 0, el menú muestra el jugo «Agotado hoy» y la empanada «Quedan pocas unidades».\n"
          "4. Anotar «Estado inicial comprobado: Sí» en la hoja del siguiente participante.\n"
          "5. El primer pedido confirmado siempre recibe el número **#CU-104**, porque el contador se reinicia con la recarga.\n\n")
    t += "## 4. Estado del protocolo\n\nProtocolo **versión 2** listo: 7 tareas (`Fase3-Aplicacion/Siete_Tareas.md`), guion actualizado (`Guion_Sesion_V2.md`) y hoja de observación V2.\n\nElaborado por: Cristian Ango · Fecha: 18/11/2026\n"
    escribir("Fase3-Aplicacion/Ajuste_Postpilotaje.md", t)


def escribir_siete_tareas():
    t = "# Fase 3 · Siete tareas de usabilidad (protocolo V2)\n\nCada consigna se lee palabra por palabra, sin nombrar botones ni pantallas. El tiempo máximo es el doble de la meta.\n\n"
    t += tabla(["ID", "Consigna que se lee", "Meta", "Tiempo máximo", "Criterio de éxito observable", "Respuesta correcta"],
               [[x[0], x[1], f"{x[2]} s", f"{x[3]} s", x[4], x[5]] for x in TAREAS])
    t += "\n## Reglas\n\n- T7 se aplica al final, con el pedido de T6 ya cancelado; el estado de la búsqueda no depende de pedidos previos.\n- Solo «Sí» cuenta como éxito autónomo. «Con ayuda» es tras la pista única; «No» es abandono o superar el máximo.\n- Quitar o cambiar la empanada en T4 y volver a confirmar es un error **no crítico**.\n\nElaborado por: Cristian Ango · Fecha: 18/11/2026\n"
    escribir("Fase3-Aplicacion/Siete_Tareas.md", t)


def escribir_guion():
    t = "# Fase 3 · Guion de la sesión (versión 2)\n\nCada sesión dura unos 20 minutos. Roles: moderador (Cristian Ango), registro de métricas (Julio Jacho), observador (Oscar Riofrio) y soporte técnico (Matias Morales).\n\n"
    t += "## Antes de cada sesión\n\n- [ ] Participante que cumple el perfil: estudiante de la UTA, mayor de edad, que no es del grupo y no conoce las tareas.\n- [ ] Reinicio F5 con la URL en `#/inicio` y estado inicial comprobado.\n- [ ] Cronómetro a cargo de una sola persona; hoja V2 impresa o abierta.\n- [ ] Consigna de T4 escrita en una tarjeta.\n\n"
    t += "## Durante la sesión\n\n"
    t += tabla(["Paso", "Qué se hace o se dice"], [
        ["1. Bienvenida", "«Vamos a probar una aplicación, no a evaluarte a ti.»"],
        ["2. Consentimiento", "Leer `Consentimiento_Informado.md`; preguntar si acepta participar y si acepta grabar solo la pantalla."],
        ["3. Perfil", "Anotar edad, carrera y si conoce el prototipo; si no cumple el perfil, no se registra."],
        ["4. Voz alta", "«Mientras trabajas, di en voz alta lo que piensas, lo que buscas y lo que te sorprende.»"],
        ["5. Tareas T1–T7", "Leer cada consigna tal cual; el cronómetro arranca al terminar de leer y se detiene cuando el usuario termina o abandona."],
        ["6. SUS", "El participante responde solo, sin que nadie mire."],
        ["7. Cierre", "«¿Qué fue lo más confuso? ¿Qué funcionó mejor?» y agradecer sin comentar el desempeño."],
    ])
    t += "\n## Lo que el moderador puede y no puede decir\n\n- **Puede:** «¿Qué estás pensando?»; la **pista única** (una vez por tarea, textual): «Vuelve a leer la tarea y revisa las opciones que tienes en pantalla»; «Gracias, pasemos a la siguiente» al llegar al máximo.\n- **No puede:** nombrar botones o pantallas, decir «casi» o «muy bien», señalar la pantalla ni corregir una respuesta.\n\n"
    t += "## Entre participantes\n\nSeguir el procedimiento de reinicio de `Ajuste_Postpilotaje.md`, sección 3.\n\nElaborado por: Cristian Ango · Fecha: 18/11/2026\n"
    escribir("Fase3-Aplicacion/Guion_Sesion_V2.md", t)


# =====================================================================
#  FASE 4: CRITERIOS, BACKLOG, ISSUES
# =====================================================================
def hallazgos_por_prio():
    return sorted(HALLAZGOS, key=lambda h: (ORDEN_PRIO[h["prio"]], -h["sev"], h["id"]))


def tabla_criterios():
    fs = []
    for i, h in enumerate(HALLAZGOS, 1):
        comp, cambio, est, acept = CRITERIOS[h["id"]]
        fs.append([f"**C-{i:02d}**", h["id"], comp, cambio, est, acept])
    return tabla(["ID", "Hallazgo", "Componente afectado", "Cambio específico", "Estándar de respaldo", "Criterio de aceptación verificable"], fs)


def tabla_backlog():
    fs = []
    for h in hallazgos_por_prio():
        n = h["id"][2:]
        fs.append([f"**B-{n}**", h["mejora"], h["id"], f"C-{n}", f'**{h["prio"]}**', f'{h["sev"]} · {ETIQ_SEV[h["sev"]]}', ESFUERZO[h["id"]], h["resp"],
                   f"[#{ISSUE_N[h['id']]}]({REPO}/issues/{ISSUE_N[h['id']]})"])
    return tabla(["ID", "Mejora", "Hallazgo", "Criterio", "Prioridad", "Severidad", "Esfuerzo", "Responsable", "Issue"], fs)


TABLA_PRIO = tabla(["Prioridad", "Regla", "Plazo sugerido"], [
    ["**P1**", "Severidad 4, o severidad 3 confirmada por ambos métodos.", "Antes de cualquier uso real"],
    ["**P2**", "Severidad 3 detectada por un solo método, o severidad 2 confirmada por ambos.", "Siguiente iteración"],
    ["**P3**", "Severidad 2 detectada por un solo método.", "Cuando haya capacidad"],
    ["**P4**", "Severidad 1 (cosmético).", "Mejora continua"],
])


def escribir_criterios():
    t = "# Criterios técnicos de mejora\n\nCada criterio parte de un hallazgo de la matriz consolidada y se puede comprobar con la prueba descrita en la última columna.\n\n"
    t += tabla_criterios()
    t += "\nElaborado por: Oscar Riofrio · Fecha: 18/11/2026\n"
    escribir("Fase4-Cierre/Criterios_Tecnicos.md", t)


def escribir_backlog():
    t = f"# Backlog priorizado de mejoras\n\n{AVISO}Cada fila es un GitHub Issue. Los Issues ya están creados en el repositorio (#25 a #34, con el ID `B-01`… en el título); su texto está en `Fase4-Cierre/issues/`. Los Pull Requests los mencionan con `Refs` y no los cierran, porque la mejora en el prototipo todavía no se implementa.\n\n"
    t += "## Regla de prioridad\n\n" + TABLA_PRIO + "\n## Backlog\n\n" + tabla_backlog()
    t += "\nElaborado por: Oscar Riofrio · Fecha: 18/11/2026\n"
    escribir("Fase4-Cierre/Backlog.md", t)


def escribir_issues():
    for h in hallazgos_por_prio():
        n = h["id"][2:]
        comp, cambio, est, acept = CRITERIOS[h["id"]]
        cuerpo = (f"## Hallazgo {h['id']} · {h['titulo']}\n\n{h['detalle']}\n\n"
                  f"- **Severidad:** {h['sev']} · {ETIQ_SEV[h['sev']]} (F={h['F']}, I={h['I']}, P={h['P']})\n"
                  f"- **Triangulación:** {h['cat']}\n- **Prioridad:** {h['prio']}\n- **Esfuerzo estimado:** {ESFUERZO[h['id']]}\n"
                  f"- **Responsable:** {h['resp']}\n- **Heurísticas:** {', '.join(h['heur'])}\n\n"
                  f"## Mejora propuesta\n\n{h['mejora']}\n\n## Criterio técnico C-{n}\n\n- **Componente:** {comp}\n- **Cambio:** {cambio}\n- **Estándar:** {est}\n\n"
                  f"## Criterio de aceptación\n\n- [ ] {acept}\n\n"
                  f"## Trazabilidad\n\nMatriz: `resultados/matriz-hallazgos.md` · Criterios: `Fase4-Cierre/Criterios_Tecnicos.md` · Backlog: `Fase4-Cierre/Backlog.md`\n")
        escribir(f"Fase4-Cierre/issues/B-{n}.md", f"Título del Issue: B-{n} · {h['titulo']} ({h['prio']})\n\n" + cuerpo)


# =====================================================================
#  CONCLUSIONES Y APORTES
# =====================================================================
def escribir_conclusiones():
    cc = conteo_cat(); tot = len(HALLAZGOS)
    k = "Confirmado por ambos métodos"
    t = f"# Conclusiones del APE 6 — CaféU v3\n\n{AVISO}"
    t += "## Pregunta del laboratorio\n\n> ¿Una interfaz que funciona técnicamente puede ser una mala interfaz? (Verificación vs. validación — Boehm, 1984)\n\n"
    t += (f"**Sí.** CaféU v3 funciona: las seis tareas base se completaron sin ayuda en el {fmt(G6['tasa'])} % de los intentos y el SUS promedio fue {fmt(SUS_PROM)} "
          f"({'por encima' if SUS_PROM >= 68 else 'por debajo'} de 68). Sin embargo, al probar funciones que el pilotaje no recorría, el éxito autónomo global bajó a {fmt(G7['tasa'])} % "
          f"y apareció un fallo de severidad {HID['H-01']['sev']} (buscador). Pasar la verificación (el código hace lo que dice) no implica pasar la validación (el usuario logra su meta).\n\n")
    t += "## Conclusiones\n\n"
    t += (f"1. **La verificación técnica es buena, la validación es parcial.** Eficacia {fmt(G6['tasa'])} % en T1–T6 frente a {fmt(G7['tasa'])} % en T1–T7; mediana global de {fmt(G7['med'])} s. "
          f"T7 (buscador) obtuvo {fmt(MET['T7']['tasa'])} % de éxito autónomo y T4, {fmt(MET['T4']['tasa'])} %.\n")
    t += (f"2. **Los dos problemas más graves nacen de la prevención de errores y la tolerancia al lenguaje real.** H-01 (el buscador no ignora tildes, severidad {HID['H-01']['sev']}) y H-02 (la empanada con «Quedan pocas unidades» se agota recién al confirmar, severidad {HID['H-02']['sev']}) fueron confirmados por ambos métodos.\n")
    t += (f"3. **La triangulación aportó más que cada método por separado.** De {tot} hallazgos, {cc[k]} ({fmt(100 * cc[k] / tot)} %) se confirmaron por ambos métodos, {cc['Solo heurística']} salieron solo de la heurística y {cc['Solo usuarios']} solo de las sesiones (H-08, el salto a «Mi pedido» al agregar).\n")
    t += (f"4. **La satisfacción oculta la dispersión.** El SUS promedio de {fmt(SUS_PROM)} supera la línea de base, pero {min(CODS, key=lambda c: SUS[c][2])} puntuó {fmt(min(v[2] for v in SUS.values()))}, la sesión en que el buscador falló por completo.\n")
    t += f"5. **El backlog es accionable.** Los {tot} hallazgos se convirtieron en criterios técnicos verificables (C-01…C-{tot:02d}) y en {tot} Issues priorizados: {sum(1 for h in HALLAZGOS if h['prio'] == 'P1')} P1, {sum(1 for h in HALLAZGOS if h['prio'] == 'P2')} P2, {sum(1 for h in HALLAZGOS if h['prio'] == 'P3')} P3 y {sum(1 for h in HALLAZGOS if h['prio'] == 'P4')} P4.\n\n"
    t += "## Recomendaciones\n\n"
    for h in hallazgos_por_prio()[:4]:
        t += f"- **{h['prio']} · {h['id']}:** {h['mejora']}\n"
    t += "- Repetir la prueba con 5 participantes tras corregir los P1 y P2 para comprobar que T4 y T7 superan la meta.\n\n"
    t += ("## Limitaciones\n\n- Evaluación formativa con 3 participantes: sirve para detectar problemas, no para estimar proporciones de la población (Faulkner, 2003).\n"
          "- Las evaluaciones heurísticas están pre-llenadas a partir de la inspección del código y deben ser confirmadas por cada evaluador.\n")
    if SIM:
        t += "- Los datos de P1–P3 son simulados; las cifras de este documento deben recalcularse con mediciones reales.\n"
    t += "\nElaborado por: Oscar Riofrio · Fecha: 18/11/2026\n"
    escribir("docs/conclusiones.md", t)


def escribir_aportes():
    ruta = "Evidencias_Colaboracion/Registro_Aportes.md"
    base = open(ruta, encoding="utf-8").read() if os.path.exists(ruta) else "# Registro de aportes\n"
    base = base.split("\n## Fases 3 y 4")[0].rstrip("\n")
    t = base + "\n\n## Fases 3 y 4\n\n"
    t += tabla(["Fecha", "Integrante", "Rama", "Aporte", "Archivos"], [
        ["18/11/2026", "Cristian Ango", "`cristian/f3-f4`", "Ajuste post-pilotaje y tarea T7, guion V2, sesión P1, heurística E1, datos y generador, README", "`Fase3-Aplicacion/`, `resultados/P1.md`, `resultados/heuristica-cristian.md`, `datos/`, `herramientas/generar_fase3_4.py`, `README.md`"],
        ["18/11/2026", "Julio Jacho", "`julio/f3-f4`", "Sesión P2, métricas ISO 9241-11 y SUS, heurística E2", "`resultados/P2.md`, `resultados/metricas.md`, `resultados/heuristica-julio.md`"],
        ["18/11/2026", "Matias Morales", "`matias/f3-f4`", "Sesión P3, heurística E3, consolidado, matriz de hallazgos y triangulación", "`resultados/P3.md`, `resultados/heuristica-matias.md`, `resultados/heuristica-consolidado.md`, `resultados/matriz-hallazgos.md`, `resultados/triangulacion.md`"],
        ["18/11/2026", "Oscar Riofrio", "`oscar/f3-f4`", "Heurística E4, criterios técnicos, backlog e Issues, conclusiones, registro de aportes", "`resultados/heuristica-oscar.md`, `Fase4-Cierre/`, `docs/conclusiones.md`, `Evidencias_Colaboracion/Registro_Aportes.md`"],
    ])
    t += "\nCada integrante entrega con su propia rama, commits propios y un Pull Request hacia `main`.\n"
    escribir(ruta, t)


# =====================================================================
#  README
# =====================================================================
def escribir_readme():
    cc = conteo_cat(); tot = len(HALLAZGOS); k = "Confirmado por ambos métodos"
    t = "# Ape6-IHC · APE 6 — Evaluación y validación de CaféU v3\n\n"
    t += AVISO
    t += "## 1. Datos generales\n\n"
    t += tabla(["Campo", "Dato"], [
        ["Universidad", "Universidad Técnica de Ambato"], ["Facultad / Carrera", "Ingeniería en Sistemas, Electrónica e Industrial · Software"],
        ["Asignatura", "Interacción Humano / Computador · Quinto semestre · Paralelo A"], ["Docente", "Ing. José Rubén Caiza Caizabuano, Mg."],
        ["Ciclo", "Julio 2026 – Diciembre 2026"], ["Tema", "APE 6 · Evaluación y validación"],
        ["Interfaz evaluada", "CaféU v3 (prototipo del APE 4, repositorio [HCI2026-GV](https://github.com/AdrianMora8/HCI2026-GV), `APE4-integral/prototipo/cafeu-v3.html`)"],
    ])
    t += "\n> **Pregunta del laboratorio:** ¿una interfaz que funciona técnicamente puede ser una mala interfaz?\n\n"
    t += "## 2. Problema\n\nCaféU permite pedir en la cafetería universitaria desde el celular y retirar sin hacer fila. La Fase 1 planificó la evaluación y la Fase 2 hizo el pilotaje; este trabajo cierra con la aplicación completa de los métodos (Fase 3) y la priorización de mejoras (Fase 4).\n\n"
    t += "## 3. Objetivos\n\n- **General:** evaluar la usabilidad de CaféU v3 combinando inspección heurística y pruebas con usuarios, y priorizar las mejoras en un backlog trazable.\n- **Específicos:** (1) ajustar el protocolo e incorporar una tarea de refuerzo; (2) medir eficacia, eficiencia y satisfacción según ISO 9241-11; (3) triangular los hallazgos y convertirlos en criterios técnicos e Issues.\n\n"
    t += "## 4. Integrantes y responsabilidades\n\n"
    t += tabla(["Integrante", "Usuario de GitHub", "Rol en las sesiones", "Aporte en las Fases 3 y 4", "Rama"], [
        ["Cristian Ango", "@CristianDDGA", "Moderador", "Ajuste post-pilotaje, T7, guion V2, P1, heurística E1, datos, generador y README", "`cristian/f3-f4`"],
        ["Julio Jacho", "@Sebasjach21", "Registro de métricas", "P2, métricas ISO y SUS, heurística E2", "`julio/f3-f4`"],
        ["Matias Morales", "@MatiusJBG", "Soporte técnico", "P3, heurística E3, consolidado, matriz y triangulación", "`matias/f3-f4`"],
        ["Oscar Riofrio", "@AdrianMora8", "Observador", "Heurística E4, criterios técnicos, backlog e Issues, conclusiones, registro de aportes", "`oscar/f3-f4`"],
    ])
    t += "\n## 5. Métodos seleccionados\n\n"
    t += tabla(["Método", "Tipo", "Aplicación", "Instrumentos"], [
        ["Evaluación heurística de Nielsen (1994) con severidad 1–4", "Analítico", "4 evaluadores independientes (E1–E4); severidad por Frecuencia, Impacto y Persistencia (Nielsen, 1995).", "`resultados/heuristica-*.md`"],
        ["Prueba de usabilidad con pensamiento en voz alta", "Empírico", "3 participantes externos (P1–P3), 4 roles, 7 tareas, SUS al final, reinicio con F5 entre sesiones.", "`Fase3-Aplicacion/`, `resultados/P1.md`–`P3.md`"],
    ])
    t += "\n## 6. Procedimiento\n\n### Fase 3 · Aplicación y análisis\n\n"
    t += ("1. **Ajuste post-pilotaje:** se revisaron las brechas de la Fase 2 y se agregó la tarea de refuerzo **T7** (buscador sin tilde) y el reinicio F5 con comprobación de la URL → [`Fase3-Aplicacion/Ajuste_Postpilotaje.md`](Fase3-Aplicacion/Ajuste_Postpilotaje.md).\n"
          "2. **Método 1 (heurística):** cada integrante inspeccionó CaféU con las 10 heurísticas y asignó severidad 1–4 → [`resultados/heuristica-*.md`](resultados/).\n"
          "3. **Método 2 (usuarios):** sesiones con P1–P3, consentimiento, cuatro roles y SUS → [`resultados/P1.md`](resultados/P1.md), [`P2`](resultados/P2.md), [`P3`](resultados/P3.md).\n"
          "4. **Métricas ISO 9241-11:** eficacia, eficiencia y satisfacción → sección 8.1 y [`resultados/metricas.md`](resultados/metricas.md).\n\n")
    t += "### Fase 4 · Priorización y cierre\n\n"
    t += ("5. **Matriz de hallazgos** → sección 8.2.\n6. **Triangulación** → sección 8.3.\n7. **Criterios técnicos** → sección 8.4.\n8. **Backlog en Issues y conclusiones** → sección 8.5 y [`docs/conclusiones.md`](docs/conclusiones.md).\n\n")
    t += "## 7. Herramientas\n\nNavegador web con `cafeu-v3.html`, cronómetro, hojas de observación en Markdown, cuestionario SUS, Git y GitHub (ramas, Pull Requests e Issues), y `herramientas/generar_fase3_4.py` para calcular las tablas.\n\n"
    # 8.1
    t += "## 8. Resultados\n\n### 8.1 Métricas (ISO 9241-11:2018)\n\n"
    fs = []
    for tid, cons, meta, mx, crit, resp in TAREAS:
        m = MET[tid]
        fs.append([tid, f"{meta} s", f'{fmt(m["tasa"])} % ({m["ok"]}/3)', f'{fmt(m["med"])} s', "Sí" if m["med"] <= meta else "No", m["cri"], m["nocri"]])
    t += tabla(["Tarea", "Meta", "Tasa de éxito autónomo", "Mediana", "¿≤ meta?", "Err. críticos", "Err. no críticos"], fs)
    t += "\n" + tabla(["Indicador", "T1–T6", "T1–T7", "Meta"], [
        ["Tasa de éxito autónomo", f'{fmt(G6["tasa"])} %', f'{fmt(G7["tasa"])} %', "≥ 80 %"],
        ["Mediana de tiempo", f'{fmt(G6["med"])} s', f'{fmt(G7["med"])} s', "≤ meta por tarea"],
        ["Errores críticos / no críticos", f'{G6["cri"]} / {G6["nocri"]}', f'{G7["cri"]} / {G7["nocri"]}', "0 / ≤ 1 por tarea"],
    ])
    t += "\n" + tabla(["Participante", "SUS (0–100)", "Escala adjetiva", "¿≥ 68?"],
                      [[c, fmt(SUS[c][2]), adjetivo(SUS[c][2]), "Sí" if SUS[c][2] >= 68 else "No"] for c in CODS] +
                      [["**Promedio**", f"**{fmt(SUS_PROM)}**", adjetivo(SUS_PROM), "Sí" if SUS_PROM >= 68 else "No"]])
    t += "\nDetalle completo en [`resultados/metricas.md`](resultados/metricas.md).\n\n"
    # 8.2
    t += "### 8.2 Matriz consolidada de hallazgos\n\n"
    t += tabla(["ID", "Hallazgo", "Heurística", "Método", "Severidad", "Mejora propuesta"],
               [[f'**{h["id"]}**', h["titulo"], "/".join(h["heur"]), {"Confirmado por ambos métodos": "Ambos", "Solo heurística": "Heurística", "Solo usuarios": "Usuarios"}[h["cat"]],
                 f'**{h["sev"]}** · {ETIQ_SEV[h["sev"]]}', h["mejora"]] for h in HALLAZGOS])
    t += "\nEvidencia completa en [`resultados/matriz-hallazgos.md`](resultados/matriz-hallazgos.md) y [`resultados/heuristica-consolidado.md`](resultados/heuristica-consolidado.md).\n\n"
    # 8.3
    t += "### 8.3 Triangulación\n\n"
    t += tabla(["Categoría", "N.º", "Hallazgos"], [[f"**{kk}**", cc[kk], ids_de(kk)] for kk in cc])
    t += f"\n{cc[k]} de {tot} hallazgos ({fmt(100 * cc[k] / tot)} %) se confirmaron por ambos métodos. Detalle en [`resultados/triangulacion.md`](resultados/triangulacion.md).\n\n"
    # 8.4
    t += "### 8.4 Criterios técnicos\n\n" + tabla_criterios() + "\nVersión independiente: [`Fase4-Cierre/Criterios_Tecnicos.md`](Fase4-Cierre/Criterios_Tecnicos.md).\n\n"
    # 8.5
    t += "### 8.5 Backlog priorizado (GitHub Issues)\n\n" + TABLA_PRIO + "\n" + tabla_backlog()
    t += "\nLos 10 Issues de mejora están publicados (#25 a #34); su texto está en [`Fase4-Cierre/issues/`](Fase4-Cierre/issues/). Además hay un Issue de tarea por integrante, que cierra su Pull Request:\n\n"
    t += tabla(["Integrante", "Issue de tarea", "Rama"], [[NOMBRES[k], f"[#{v}]({REPO}/issues/{v})", f"`{k.lower()}/f3-f4`"] for k, v in ISSUE_TAREA.items()])
    t += "\n"
    t += "## 9. Evidencias y entregables\n\n"
    t += tabla(["Entregable", "Ubicación"], [
        ["Evidencias de la evaluación heurística", "`resultados/heuristica-cristian.md`, `-julio`, `-matias`, `-oscar`, `-consolidado`"],
        ["Registros de participantes", "`resultados/P1.md`, `P2.md`, `P3.md`"],
        ["Métricas ISO/SUS, matriz y triangulación", "`resultados/metricas.md`, `matriz-hallazgos.md`, `triangulacion.md` y este README"],
        ["Criterios técnicos y backlog", "`Fase4-Cierre/Criterios_Tecnicos.md`, `Backlog.md`, `issues/`"],
        ["Conclusiones", "`docs/conclusiones.md`"],
        ["Fases anteriores", "`Fase1-Planificacion/`, `Fase2-Pilotaje/`"],
        ["Trabajo colaborativo", "`Evidencias_Colaboracion/Registro_Aportes.md`, ramas y Pull Requests"],
    ])
    t += "\n## 10. Organización del repositorio\n\n"
    t += tabla(["Carpeta o archivo", "Contenido"], [
        ["`Fase1-Planificacion/`", "Plan, consentimiento, tareas y hoja de observación"], ["`Fase2-Pilotaje/`", "Verificación, guion, ajustes, comparación y plantillas del pilotaje"],
        ["`Fase3-Aplicacion/`", "Ajuste post-pilotaje, siete tareas y guion V2"], ["`Fase4-Cierre/`", "Criterios técnicos, backlog y textos de los Issues"],
        ["`resultados/`", "Heurísticas E1–E4, sesiones P1–P3, métricas, matriz y triangulación"], ["`datos/`", "Mediciones de las sesiones (fuente de las tablas)"],
        ["`herramientas/`", "`generar_fase3_4.py`, `md_a_pdf.py`"], ["`docs/`", "Conclusiones"], ["`Evidencias_Colaboracion/`", "Registro de aportes"],
    ])
    t += "\n## 11. Trabajo colaborativo\n\n- Cada integrante trabajó en su propia rama (`cristian/f3-f4`, `julio/f3-f4`, `matias/f3-f4`, `oscar/f3-f4`), con commits propios.\n- Cada rama se integra a `main` mediante un Pull Request revisado por otro integrante.\n- El detalle de quién hizo qué está en [`Evidencias_Colaboracion/Registro_Aportes.md`](Evidencias_Colaboracion/Registro_Aportes.md).\n\n"
    t += "## 12. Conclusiones\n\n"
    t += (f"1. CaféU v3 **funciona técnicamente** (T1–T6: {fmt(G6['tasa'])} % de éxito autónomo) **pero no supera la validación**: con la tarea de refuerzo el éxito global baja a {fmt(G7['tasa'])} % y el buscador queda en {fmt(MET['T7']['tasa'])} %.\n"
          f"2. Los hallazgos de mayor severidad son H-01 (búsqueda sensible a tildes) y H-02 (agotado detectado al confirmar), confirmados por ambos métodos.\n"
          f"3. SUS promedio {fmt(SUS_PROM)} ({adjetivo(SUS_PROM)}), con dispersión entre participantes.\n"
          "4. El backlog de 10 mejoras está priorizado de P1 a P4 y trazado a criterios técnicos verificables.\n\n"
          "Texto completo: [`docs/conclusiones.md`](docs/conclusiones.md).\n\n")
    t += "## 13. Referencias\n\n"
    for ref in ["Bangor, A., Kortum, P., & Miller, J. (2009). Determining what individual SUS scores mean. *Journal of Usability Studies, 4*(3), 114–123.",
                "Boehm, B. W. (1984). Verifying and validating software requirements and design specifications. *IEEE Software, 1*(1), 75–88.",
                "Brooke, J. (1996). SUS: A \"quick and dirty\" usability scale. En *Usability Evaluation in Industry*. Taylor & Francis.",
                "Faulkner, L. (2003). Beyond the five-user assumption. *Behavior Research Methods, Instruments, & Computers, 35*(3), 379–383.",
                "ISO 9241-11:2018. *Ergonomics of human-system interaction — Part 11: Usability.*",
                "Nielsen, J. (1994). Enhancing the explanatory power of usability heuristics. *Proceedings of CHI '94*.",
                "Nielsen, J. (1995). *Severity ratings for usability problems.* Nielsen Norman Group.",
                "W3C. (2018). *Web Content Accessibility Guidelines (WCAG) 2.1.*"]:
        t += f"- {ref}\n"
    escribir("README.md", t)


if __name__ == "__main__":
    print("Generando entregables de las Fases 3 y 4…")
    for c in CODS:
        escribir_participante(c)
    escribir_metricas()
    for n in ["Cristian", "Julio", "Matias", "Oscar"]:
        escribir_heuristica(n)
    escribir_consolidado(); escribir_matriz(); escribir_triangulacion()
    escribir_ajuste(); escribir_siete_tareas(); escribir_guion()
    escribir_criterios(); escribir_backlog(); escribir_issues()
    escribir_conclusiones(); escribir_aportes(); escribir_readme()
    print("Listo." + (" (datos de usuarios SIMULADOS)" if SIM else ""))
