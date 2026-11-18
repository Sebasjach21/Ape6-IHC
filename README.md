# Ape6-IHC · APE 6 — Evaluación y validación de CaféU v3

> ⚠ **DATOS DE USUARIOS SIMULADOS (P1–P3).** Los valores de las sesiones son de ejemplo, coherentes con el comportamiento real del prototipo, pero **no fueron medidos con personas**. Reemplazarlos en `datos/fase3_participantes.json` y ejecutar `python herramientas/generar_fase3_4.py` antes de presentarlos como evidencia empírica.

## 1. Datos generales

| Campo | Dato |
| --- | --- |
| Universidad | Universidad Técnica de Ambato |
| Facultad / Carrera | Ingeniería en Sistemas, Electrónica e Industrial · Software |
| Asignatura | Interacción Humano / Computador · Quinto semestre · Paralelo A |
| Docente | Ing. José Rubén Caiza Caizabuano, Mg. |
| Ciclo | Julio 2026 – Diciembre 2026 |
| Tema | APE 6 · Evaluación y validación |
| Interfaz evaluada | CaféU v3 (prototipo del APE 4, repositorio [HCI2026-GV](https://github.com/AdrianMora8/HCI2026-GV), `APE4-integral/prototipo/cafeu-v3.html`) |

> **Pregunta del laboratorio:** ¿una interfaz que funciona técnicamente puede ser una mala interfaz?

## 2. Problema

CaféU permite pedir en la cafetería universitaria desde el celular y retirar sin hacer fila. La Fase 1 planificó la evaluación y la Fase 2 hizo el pilotaje; este trabajo cierra con la aplicación completa de los métodos (Fase 3) y la priorización de mejoras (Fase 4).

## 3. Objetivos

- **General:** evaluar la usabilidad de CaféU v3 combinando inspección heurística y pruebas con usuarios, y priorizar las mejoras en un backlog trazable.
- **Específicos:** (1) ajustar el protocolo e incorporar una tarea de refuerzo; (2) medir eficacia, eficiencia y satisfacción según ISO 9241-11; (3) triangular los hallazgos y convertirlos en criterios técnicos e Issues.

## 4. Integrantes y responsabilidades

| Integrante | Usuario de GitHub | Rol en las sesiones | Aporte en las Fases 3 y 4 | Rama |
| --- | --- | --- | --- | --- |
| Cristian Ango | @CristianDDGA | Moderador | Ajuste post-pilotaje, T7, guion V2, P1, heurística E1, datos, generador y README | `cristian/f3-f4` |
| Julio Jacho | @Sebasjach21 | Registro de métricas | P2, métricas ISO y SUS, heurística E2 | `julio/f3-f4` |
| Matias Morales | @MatiusJBG | Soporte técnico | P3, heurística E3, consolidado, matriz y triangulación | `matias/f3-f4` |
| Oscar Riofrio | @AdrianMora8 | Observador | Heurística E4, criterios técnicos, backlog e Issues, conclusiones, registro de aportes | `oscar/f3-f4` |

## 5. Métodos seleccionados

| Método | Tipo | Aplicación | Instrumentos |
| --- | --- | --- | --- |
| Evaluación heurística de Nielsen (1994) con severidad 1–4 | Analítico | 4 evaluadores independientes (E1–E4); severidad por Frecuencia, Impacto y Persistencia (Nielsen, 1995). | `resultados/heuristica-*.md` |
| Prueba de usabilidad con pensamiento en voz alta | Empírico | 3 participantes externos (P1–P3), 4 roles, 7 tareas, SUS al final, reinicio con F5 entre sesiones. | `Fase3-Aplicacion/`, `resultados/P1.md`–`P3.md` |

## 6. Procedimiento

### Fase 3 · Aplicación y análisis

1. **Ajuste post-pilotaje:** se revisaron las brechas de la Fase 2 y se agregó la tarea de refuerzo **T7** (buscador sin tilde) y el reinicio F5 con comprobación de la URL → [`Fase3-Aplicacion/Ajuste_Postpilotaje.md`](Fase3-Aplicacion/Ajuste_Postpilotaje.md).
2. **Método 1 (heurística):** cada integrante inspeccionó CaféU con las 10 heurísticas y asignó severidad 1–4 → [`resultados/heuristica-*.md`](resultados/).
3. **Método 2 (usuarios):** sesiones con P1–P3, consentimiento, cuatro roles y SUS → [`resultados/P1.md`](resultados/P1.md), [`P2`](resultados/P2.md), [`P3`](resultados/P3.md).
4. **Métricas ISO 9241-11:** eficacia, eficiencia y satisfacción → sección 8.1 y [`resultados/metricas.md`](resultados/metricas.md).

### Fase 4 · Priorización y cierre

5. **Matriz de hallazgos** → sección 8.2.
6. **Triangulación** → sección 8.3.
7. **Criterios técnicos** → sección 8.4.
8. **Backlog en Issues y conclusiones** → sección 8.5 y [`docs/conclusiones.md`](docs/conclusiones.md).

## 7. Herramientas

Navegador web con `cafeu-v3.html`, cronómetro, hojas de observación en Markdown, cuestionario SUS, Git y GitHub (ramas, Pull Requests e Issues), y `herramientas/generar_fase3_4.py` para calcular las tablas.

## 8. Resultados

### 8.1 Métricas (ISO 9241-11:2018)

| Tarea | Meta | Tasa de éxito autónomo | Mediana | ¿≤ meta? | Err. críticos | Err. no críticos |
| --- | --- | --- | --- | --- | --- | --- |
| T1 | 60 s | 100,0 % (3/3) | 22,0 s | Sí | 0 | 1 |
| T2 | 60 s | 100,0 % (3/3) | 24,0 s | Sí | 0 | 0 |
| T3 | 60 s | 100,0 % (3/3) | 41,0 s | Sí | 0 | 2 |
| T4 | 90 s | 33,3 % (1/3) | 134,0 s | No | 0 | 5 |
| T5 | 90 s | 100,0 % (3/3) | 30,0 s | Sí | 0 | 0 |
| T6 | 60 s | 100,0 % (3/3) | 22,0 s | Sí | 0 | 0 |
| T7 | 60 s | 33,3 % (1/3) | 98,0 s | No | 1 | 5 |

| Indicador | T1–T6 | T1–T7 | Meta |
| --- | --- | --- | --- |
| Tasa de éxito autónomo | 88,9 % | 81,0 % | ≥ 80 % |
| Mediana de tiempo | 28,0 s | 30,0 s | ≤ meta por tarea |
| Errores críticos / no críticos | 0 / 8 | 1 / 13 | 0 / ≤ 1 por tarea |

| Participante | SUS (0–100) | Escala adjetiva | ¿≥ 68? |
| --- | --- | --- | --- |
| P1 | 80,0 | Bueno | Sí |
| P2 | 55,0 | Aceptable bajo / regular | No |
| P3 | 75,0 | Bueno | Sí |
| **Promedio** | **70,0** | Bueno | Sí |

Detalle completo en [`resultados/metricas.md`](resultados/metricas.md).

### 8.2 Matriz consolidada de hallazgos

| ID | Hallazgo | Heurística | Método | Severidad | Mejora propuesta |
| --- | --- | --- | --- | --- | --- |
| **H-01** | Búsqueda sensible a tildes | H2/H7 | Ambos | **4** · Crítico | Normalizar la consulta y los textos del catálogo con `normalize('NFD')` y quitar marcas diacríticas antes de comparar. |
| **H-02** | Producto con pocas unidades se agota recién al confirmar | H5/H9 | Ambos | **3** · Mayor | Avisar en «Mi pedido», antes de confirmar, que el producto puede agotarse; si se agota, mostrar el conflicto sin pasar por «Procesando» y resaltar las dos salidas. |
| **H-03** | El pedido confirmado no se encuentra desde «Mi pedido» | H1/H6 | Heurística | **3** · Mayor | Si existe un pedido confirmado y el carrito está vacío, mostrar una tarjeta con su número y un acceso a la confirmación. |
| **H-04** | Etiquetas de navegación inconsistentes | H4 | Heurística | **2** · Menor | Unificar los nombres: «Menú» para volver al menú y una sola entrada a «Mi pedido». |
| **H-05** | Falta información de pago, tiempo y lugar de retiro | H10/H1 | Ambos | **2** · Menor | Agregar un bloque con forma de pago, tiempo estimado y punto de retiro, acordado con la cafetería. |
| **H-06** | Horas de retiro fijas y sin relación con la hora actual | H5 | Heurística | **2** · Menor | Generar las horas desde la hora actual hasta el cierre y deshabilitar las que ya pasaron. |
| **H-07** | Textos secundarios menores a 12 px | H8 | Heurística | **1** · Cosmético | Subir esos textos a 0,8125 rem (13 px) como mínimo y comprobar la legibilidad con zoom al 200 %. |
| **H-08** | Agregar un producto lleva a «Mi pedido» sin avisar | H3/H7 | Usuarios | **2** · Menor | Permanecer en el detalle con un aviso y dos botones: «Seguir comprando» y «Ver pedido». |
| **H-09** | Límite de 9 unidades sin mensaje | H1 | Heurística | **1** · Cosmético | Mostrar «Máximo 9 por producto» y anunciarlo a lectores de pantalla. |
| **H-10** | «Sanduche» sin tilde y distinto del nombre en las tareas | H2/H4 | Heurística | **1** · Cosmético | Escribir «Sánduche» en el catálogo y en todos los documentos, y combinarlo con la búsqueda sin tildes. |

Evidencia completa en [`resultados/matriz-hallazgos.md`](resultados/matriz-hallazgos.md) y [`resultados/heuristica-consolidado.md`](resultados/heuristica-consolidado.md).

### 8.3 Triangulación

| Categoría | N.º | Hallazgos |
| --- | --- | --- |
| **Confirmado por ambos métodos** | 3 | H-01, H-02, H-05 |
| **Solo heurística** | 6 | H-03, H-04, H-06, H-07, H-09, H-10 |
| **Solo usuarios** | 1 | H-08 |

3 de 10 hallazgos (30,0 %) se confirmaron por ambos métodos. Detalle en [`resultados/triangulacion.md`](resultados/triangulacion.md).

### 8.4 Criterios técnicos

| ID | Hallazgo | Componente afectado | Cambio específico | Estándar de respaldo | Criterio de aceptación verificable |
| --- | --- | --- | --- | --- | --- |
| **C-01** | H-01 | Filtro del menú (`vMenu()` y evento `input` de `#buscar`) | Antes de comparar, normalizar la consulta y el texto de cada producto con `s.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase()`. | Heurísticas de Nielsen H2 y H7; ISO 9241-11 (eficacia) | Escribir «cafe» o «café» devuelve «Café americano»; «sanduche» y «sánduche» devuelven «Sánduche de queso»; solo se muestra el estado vacío si el producto no existe. |
| **C-02** | H-02 | Confirmación del pedido (`iniciarEnvio()` y `vPedido()`) | Mostrar en «Mi pedido» un aviso junto a todo producto con estado «pocas» («Puede agotarse antes de confirmar») y, si se agota, volver con el conflicto en menos de 1 s, con el texto «Tu pedido no se envió» y los dos botones destacados. | WCAG 2.1 SC 3.3.1 (identificación de errores) y SC 4.1.3 (mensajes de estado); Nielsen H5 y H9 | Ningún producto con etiqueta «pocas» se agota sin un aviso previo visible en «Mi pedido»; el mensaje de conflicto lo anuncia un lector de pantalla. |
| **C-03** | H-03 | Pantalla «Mi pedido» (`vPedido()`) y pestaña inferior | Si hay un pedido confirmado y el carrito está vacío, mostrar una tarjeta «Pedido #… confirmado» con el botón «Ver pedido» que lleva a la confirmación. | Nielsen H1 y H6; WCAG 2.1 SC 3.2.3 (navegación coherente) | Desde el menú, el pedido confirmado se alcanza en 2 toques o menos. |
| **C-04** | H-04 | Etiquetas de navegación (`vInicio`, `vDetalle`, `vPedido`, `vConfirmacion`, encabezado y pestañas) | Usar un único texto («Menú») para volver al menú y una sola entrada a «Mi pedido»; eliminar «Seguir comprando», «Ir al menú» y «Volver al menú» como variantes. | WCAG 2.1 SC 3.2.4 (identificación coherente); Nielsen H4 | Una auditoría de textos encuentra una sola etiqueta por acción de navegación. |
| **C-05** | H-05 | Pantalla de confirmación (`vConfirmacion()`) | Agregar un bloque «Cómo retirar» con tres datos: forma de pago, tiempo estimado de preparación y punto de retiro, validados con la cafetería. | Nielsen H10 y H1; ISO 9241-11 (eficacia y satisfacción) | La confirmación muestra los tres datos y en la prueba con usuarios nadie pregunta dónde pagar o retirar. |
| **C-06** | H-06 | Constante `HORAS` y selectores de hora (`opcionesHora()`) | Generar las opciones cada 30 minutos desde la próxima media hora (con margen de 15 min) hasta el cierre y deshabilitar las horas pasadas. | Nielsen H5; WCAG 2.1 SC 3.3.1 | A las 11:40 la primera hora ofrecida es 12:30; no existen opciones anteriores a la hora actual. |
| **C-07** | H-07 | Estilos `.progreso li`, `.tab` y `.etiqueta` | Subir el tamaño de fuente de 0,72–0,74 rem a 0,8125 rem como mínimo, sin truncar textos. | WCAG 2.1 SC 1.4.4 (cambiar el tamaño del texto); Nielsen H8 | Todo texto visible mide al menos 13 px y la interfaz se mantiene legible con zoom al 200 %. |
| **C-08** | H-08 | Acción `agregar` (detalle del producto) | Tras agregar, permanecer en el detalle con el aviso «Agregado al pedido» y los botones «Seguir comprando» y «Ver pedido», en lugar de llamar a `irA('pedido')`. | WCAG 2.1 SC 3.2.2 (al introducir datos); Nielsen H3 y H7 | Después de agregar un producto, volver al menú toma un solo toque. |
| **C-09** | H-09 | Selector de cantidad (`d-mas` y `mas`) | Al llegar a 9 unidades, mostrar «Máximo 9 por producto» y anunciarlo con la región `aria-live`. | WCAG 2.1 SC 4.1.3 (mensajes de estado); Nielsen H1 | El motivo del botón «+» deshabilitado es visible y se anuncia. |
| **C-10** | H-10 | Catálogo (`CATALOGO`), resumen del pedido y documentos del proyecto | Escribir «Sánduche de queso» con tilde en el catálogo y en el plan, las tareas y los informes. | Nielsen H2 y H4; ISO 9241-11 (consistencia) | Una búsqueda de «Sanduche» en el repositorio y en la app no encuentra variantes ortográficas. |

Versión independiente: [`Fase4-Cierre/Criterios_Tecnicos.md`](Fase4-Cierre/Criterios_Tecnicos.md).

### 8.5 Backlog priorizado (GitHub Issues)

| Prioridad | Regla | Plazo sugerido |
| --- | --- | --- |
| **P1** | Severidad 4, o severidad 3 confirmada por ambos métodos. | Antes de cualquier uso real |
| **P2** | Severidad 3 detectada por un solo método, o severidad 2 confirmada por ambos. | Siguiente iteración |
| **P3** | Severidad 2 detectada por un solo método. | Cuando haya capacidad |
| **P4** | Severidad 1 (cosmético). | Mejora continua |

| ID | Mejora | Hallazgo | Criterio | Prioridad | Severidad | Esfuerzo | Responsable | Issue |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **B-01** | Normalizar la consulta y los textos del catálogo con `normalize('NFD')` y quitar marcas diacríticas antes de comparar. | H-01 | C-01 | **P1** | 4 · Crítico | Bajo | Julio Jacho | [B-01](https://github.com/Sebasjach21/Ape6-IHC/issues?q=B-01) |
| **B-02** | Avisar en «Mi pedido», antes de confirmar, que el producto puede agotarse; si se agota, mostrar el conflicto sin pasar por «Procesando» y resaltar las dos salidas. | H-02 | C-02 | **P1** | 3 · Mayor | Medio | Cristian Ango | [B-02](https://github.com/Sebasjach21/Ape6-IHC/issues?q=B-02) |
| **B-03** | Si existe un pedido confirmado y el carrito está vacío, mostrar una tarjeta con su número y un acceso a la confirmación. | H-03 | C-03 | **P2** | 3 · Mayor | Bajo | Oscar Riofrio | [B-03](https://github.com/Sebasjach21/Ape6-IHC/issues?q=B-03) |
| **B-05** | Agregar un bloque con forma de pago, tiempo estimado y punto de retiro, acordado con la cafetería. | H-05 | C-05 | **P2** | 2 · Menor | Bajo | Oscar Riofrio | [B-05](https://github.com/Sebasjach21/Ape6-IHC/issues?q=B-05) |
| **B-04** | Unificar los nombres: «Menú» para volver al menú y una sola entrada a «Mi pedido». | H-04 | C-04 | **P3** | 2 · Menor | Bajo | Matias Morales | [B-04](https://github.com/Sebasjach21/Ape6-IHC/issues?q=B-04) |
| **B-06** | Generar las horas desde la hora actual hasta el cierre y deshabilitar las que ya pasaron. | H-06 | C-06 | **P3** | 2 · Menor | Medio | Matias Morales | [B-06](https://github.com/Sebasjach21/Ape6-IHC/issues?q=B-06) |
| **B-08** | Permanecer en el detalle con un aviso y dos botones: «Seguir comprando» y «Ver pedido». | H-08 | C-08 | **P3** | 2 · Menor | Bajo | Cristian Ango | [B-08](https://github.com/Sebasjach21/Ape6-IHC/issues?q=B-08) |
| **B-07** | Subir esos textos a 0,8125 rem (13 px) como mínimo y comprobar la legibilidad con zoom al 200 %. | H-07 | C-07 | **P4** | 1 · Cosmético | Bajo | Julio Jacho | [B-07](https://github.com/Sebasjach21/Ape6-IHC/issues?q=B-07) |
| **B-09** | Mostrar «Máximo 9 por producto» y anunciarlo a lectores de pantalla. | H-09 | C-09 | **P4** | 1 · Cosmético | Bajo | Julio Jacho | [B-09](https://github.com/Sebasjach21/Ape6-IHC/issues?q=B-09) |
| **B-10** | Escribir «Sánduche» en el catálogo y en todos los documentos, y combinarlo con la búsqueda sin tildes. | H-10 | C-10 | **P4** | 1 · Cosmético | Bajo | Oscar Riofrio | [B-10](https://github.com/Sebasjach21/Ape6-IHC/issues?q=B-10) |

Los Issues se publican con [`herramientas/crear_issues.ps1`](herramientas/crear_issues.ps1) a partir de los textos de [`Fase4-Cierre/issues/`](Fase4-Cierre/issues/).

## 9. Evidencias y entregables

| Entregable | Ubicación |
| --- | --- |
| Evidencias de la evaluación heurística | `resultados/heuristica-cristian.md`, `-julio`, `-matias`, `-oscar`, `-consolidado` |
| Registros de participantes | `resultados/P1.md`, `P2.md`, `P3.md` |
| Métricas ISO/SUS, matriz y triangulación | `resultados/metricas.md`, `matriz-hallazgos.md`, `triangulacion.md` y este README |
| Criterios técnicos y backlog | `Fase4-Cierre/Criterios_Tecnicos.md`, `Backlog.md`, `issues/` |
| Conclusiones | `docs/conclusiones.md` |
| Fases anteriores | `Fase1-Planificacion/`, `Fase2-Pilotaje/` |
| Trabajo colaborativo | `Evidencias_Colaboracion/Registro_Aportes.md`, ramas y Pull Requests |

## 10. Organización del repositorio

| Carpeta o archivo | Contenido |
| --- | --- |
| `Fase1-Planificacion/` | Plan, consentimiento, tareas y hoja de observación |
| `Fase2-Pilotaje/` | Verificación, guion, ajustes, comparación y plantillas del pilotaje |
| `Fase3-Aplicacion/` | Ajuste post-pilotaje, siete tareas y guion V2 |
| `Fase4-Cierre/` | Criterios técnicos, backlog y textos de los Issues |
| `resultados/` | Heurísticas E1–E4, sesiones P1–P3, métricas, matriz y triangulación |
| `datos/` | Mediciones de las sesiones (fuente de las tablas) |
| `herramientas/` | `generar_fase3_4.py`, `crear_issues.ps1`, `md_a_pdf.py` |
| `docs/` | Conclusiones |
| `Evidencias_Colaboracion/` | Registro de aportes |

## 11. Trabajo colaborativo

- Cada integrante trabajó en su propia rama (`cristian/f3-f4`, `julio/f3-f4`, `matias/f3-f4`, `oscar/f3-f4`), con commits propios.
- Cada rama se integra a `main` mediante un Pull Request revisado por otro integrante.
- El detalle de quién hizo qué está en [`Evidencias_Colaboracion/Registro_Aportes.md`](Evidencias_Colaboracion/Registro_Aportes.md).

## 12. Conclusiones

1. CaféU v3 **funciona técnicamente** (T1–T6: 88,9 % de éxito autónomo) **pero no supera la validación**: con la tarea de refuerzo el éxito global baja a 81,0 % y el buscador queda en 33,3 %.
2. Los hallazgos de mayor severidad son H-01 (búsqueda sensible a tildes) y H-02 (agotado detectado al confirmar), confirmados por ambos métodos.
3. SUS promedio 70,0 (Bueno), con dispersión entre participantes.
4. El backlog de 10 mejoras está priorizado de P1 a P4 y trazado a criterios técnicos verificables.

Texto completo: [`docs/conclusiones.md`](docs/conclusiones.md).

## 13. Referencias

- Bangor, A., Kortum, P., & Miller, J. (2009). Determining what individual SUS scores mean. *Journal of Usability Studies, 4*(3), 114–123.
- Boehm, B. W. (1984). Verifying and validating software requirements and design specifications. *IEEE Software, 1*(1), 75–88.
- Brooke, J. (1996). SUS: A "quick and dirty" usability scale. En *Usability Evaluation in Industry*. Taylor & Francis.
- Faulkner, L. (2003). Beyond the five-user assumption. *Behavior Research Methods, Instruments, & Computers, 35*(3), 379–383.
- ISO 9241-11:2018. *Ergonomics of human-system interaction — Part 11: Usability.*
- Nielsen, J. (1994). Enhancing the explanatory power of usability heuristics. *Proceedings of CHI '94*.
- Nielsen, J. (1995). *Severity ratings for usability problems.* Nielsen Norman Group.
- W3C. (2018). *Web Content Accessibility Guidelines (WCAG) 2.1.*
