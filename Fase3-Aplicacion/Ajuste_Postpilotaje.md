# Fase 3 · Ajuste post-pilotaje (Protocolo versión 2)

Revisión de las brechas de la Fase 2 y cambios al protocolo antes de aplicar los dos métodos. Las verificaciones del prototipo se hicieron leyendo el código de `cafeu-v3.html`.

## 1. Brechas detectadas y ajuste aplicado

| # | Brecha | Evidencia | Ajuste en la versión 2 |
| --- | --- | --- | --- |
| 1 | Funciones críticas sin probar en T1–T6: buscador y filtros | Ninguna tarea del plan usa el campo «Buscar productos»; el pilotaje no pudo evaluarlo. | Nueva tarea de refuerzo **T7** (sección 2). |
| 2 | El stock inicial no coincide con las respuestas correctas de T3 y T4 | El plan solo menciona el jugo agotado, pero en el prototipo la empanada pasa de «Quedan pocas unidades» a agotada en la **primera** confirmación (`iniciarEnvio`). | Se documentan las dos salidas válidas de T4 (quitar la empanada: $1,50; cambiarla por el sánduche: $4,25) y el error como no crítico. |
| 3 | T4 reúne cuatro acciones en una sola consigna | Fue la tarea con más ayuda y mayor mediana. | Consigna escrita en una tarjeta, además de leída, y se registra «¿Pidió repetir?». |
| 4 | La hoja de Fase 1 no registraba perfil, grabación, duración ni fallos | `Verificacion_Fase1.md`, brechas 1 a 4. | Hoja V2 con esos campos (ya aplicada en `Fase1-Planificacion/Hoja_Observacion_SUS.md`). |
| 5 | El reinicio con F5 no devolvía siempre al inicio | `mostrar(desdeHash())` conserva la pantalla de la URL: tras recargar en `#/confirmacion` aparece «Todavía no hay un pedido confirmado». | Procedimiento de reinicio con comprobación de la URL (sección 3). |
| 6 | Nombre del producto distinto en la app y en las tareas | La app dice «Sanduche de queso»; las tareas dicen «sánduche». | Las tareas usan «sánduche» solo al hablar; se registra como hallazgo H-10. |
| 7 | Funciones que ninguna tarea recorre: deshacer al quitar, cancelar envío, misma hora, cantidad máxima | Sin tarea asociada. | Se cubren con la evaluación heurística (estados que las tareas no recorren). |

## 2. Tarea de refuerzo T7

| Campo | Contenido |
| --- | --- |
| Consigna (se lee textual) | «Quieres pedir un café, pero no quieres recorrer toda la lista. Búscalo escribiendo «cafe» y agrégalo a tu pedido.» |
| Meta / máximo | 60 s / 120 s |
| Función que evalúa | Buscador del menú y tolerancia a escribir sin tilde (heurísticas H2, H5 y H7). |
| Criterio de éxito | El café americano queda agregado al pedido usando el buscador. |
| Respuesta correcta | Café americano en el pedido (cantidad 1). **Tarea de refuerzo:** el buscador no ignora tildes y «cafe» no devuelve resultados; con «café» sí. |
| Por qué se incluye | Es una función crítica de uso frecuente que el pilotaje no recorrió; en español es normal escribir sin tilde. |

## 3. Reinicio de estado (F5) entre sesiones

1. Detener la grabación (si la hay) y cerrar el pedido del participante anterior.
2. En la barra de direcciones dejar `…/cafeu-v3.html#/inicio` (o quitar todo lo que sigue a `#`) y pulsar **F5**. El prototipo conserva la pantalla indicada por la URL, así que recargar en otra pantalla no basta.
3. Comprobar el estado inicial: contador de «Mi pedido» en 0, el menú muestra el jugo «Agotado hoy» y la empanada «Quedan pocas unidades».
4. Anotar «Estado inicial comprobado: Sí» en la hoja del siguiente participante.
5. El primer pedido confirmado siempre recibe el número **#CU-104**, porque el contador se reinicia con la recarga.

## 4. Estado del protocolo

Protocolo **versión 2** listo: 7 tareas (`Fase3-Aplicacion/Siete_Tareas.md`), guion actualizado (`Guion_Sesion_V2.md`) y hoja de observación V2.

Elaborado por: Cristian Ango · Fecha: 18/11/2026
