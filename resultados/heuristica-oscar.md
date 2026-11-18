# Evaluación heurística individual — Oscar Riofrio (E4)

> **Borrador pre-llenado a partir de la inspección del código del prototipo.** Antes de entregar, Oscar debe recorrer CaféU v3, confirmar cada hallazgo y ajustar la severidad si no está de acuerdo.

Prototipo: CaféU v3 (`cafeu-v3.html`, repositorio HCI2026-GV, carpeta `APE4-integral/`). Foco de inspección: consistencia de textos y navegación, tipografía y estructura visual. Se recorrió además toda la interfaz.

Severidad (Nielsen, 1995): 1 = cosmético · 2 = menor · 3 = mayor · 4 = crítico, a partir del promedio de **Frecuencia (F)**, **Impacto (I)** y **Persistencia (P)**, cada uno de 1 a 4.

## 1. Las 10 heurísticas

| Heurística | Respuesta | Problema observado / comentario | Pantalla | Evidencia | Hallazgo |
| --- | --- | --- | --- | --- | --- |
| H1 Visibilidad del estado del sistema | No | El pedido confirmado no se encuentra desde «Mi pedido»; Falta información de pago, tiempo y lugar de retiro | Pestaña inferior y botón «Mi pedido»; Pedido confirmado | Verificado en el código (`vPedido` solo lee `carrito`; `pedido` solo se usa en `vConfirmacion`). Verificado en el código (`vConfirmacion`): no hay texto sobre pago, tiempo ni punto de retiro. | H-03, H-05 |
| H2 Relación entre el sistema y el mundo real | No | Búsqueda sensible a tildes; «Sanduche» sin tilde y distinto del nombre en las tareas | Menú de hoy · campo «Buscar productos»; Catálogo y resumen del pedido | Verificado en el código (`vMenu`, `String.indexOf`): «cafe» → 0 resultados, «café» → 1, «sánduche» → 0. Verificado en el código (`CATALOGO`) frente a `Seis_Tareas.md`. | H-01, H-10 |
| H3 Control y libertad del usuario | Sí | Sin problema observado. «Quitar» ofrece «Deshacer», cancelar pide confirmación y se puede restaurar, y «Cancelar envío» está disponible al procesar. | — | — | — |
| H4 Consistencia y estándares | No | Etiquetas de navegación inconsistentes; «Sanduche» sin tilde y distinto del nombre en las tareas | Varias pantallas; Catálogo y resumen del pedido | Verificado en el código: textos en `vInicio`, `vDetalle`, `vPedido`, `vConfirmacion` y en el encabezado/`tabbar`. Verificado en el código (`CATALOGO`) frente a `Seis_Tareas.md`. | H-04, H-10 |
| H5 Prevención de errores | No | Producto con pocas unidades se agota recién al confirmar | Mi pedido → Procesando | Verificado en el código (`iniciarEnvio`): si el pedido incluye la empanada con estado «pocas» pasa a «agotado» y se muestra el conflicto. | H-02 |
| H6 Reconocimiento antes que recuerdo | No | El pedido confirmado no se encuentra desde «Mi pedido» | Pestaña inferior y botón «Mi pedido» | Verificado en el código (`vPedido` solo lee `carrito`; `pedido` solo se usa en `vConfirmacion`). | H-03 |
| H7 Flexibilidad y eficiencia de uso | No | Búsqueda sensible a tildes | Menú de hoy · campo «Buscar productos» | Verificado en el código (`vMenu`, `String.indexOf`): «cafe» → 0 resultados, «café» → 1, «sánduche» → 0. | H-01 |
| H8 Diseño estético y minimalista | Parcial | Textos secundarios menores a 12 px | Progreso, pestañas y etiquetas de estado | Verificado en el CSS: `.progreso li` 0,72 rem; `.tab` y `.etiqueta` 0,74 rem. | H-07 |
| H9 Ayudar a reconocer, diagnosticar y recuperarse de errores | No | Producto con pocas unidades se agota recién al confirmar | Mi pedido → Procesando | Verificado en el código (`iniciarEnvio`): si el pedido incluye la empanada con estado «pocas» pasa a «agotado» y se muestra el conflicto. | H-02 |
| H10 Ayuda y documentación | No | Falta información de pago, tiempo y lugar de retiro | Pedido confirmado | Verificado en el código (`vConfirmacion`): no hay texto sobre pago, tiempo ni punto de retiro. | H-05 |

## 2. Estados y pantallas que las tareas no recorren

| Estado / pantalla revisada | Qué pasa | Problema (si hay) | Heurística |
| --- | --- | --- | --- |
| Producto agotado (jugo de naranja) | El menú muestra «Agotado hoy» y el detalle ofrece alternativas de la misma categoría; el botón agregar queda deshabilitado. | Ninguno: buen manejo. | H5 |
| Formulario con campos vacíos | Aparece un resumen con enlaces al campo con error y mensajes junto a cada campo. | Ninguno: cumple. | H9 |
| Cambiar a la misma hora | Muestra «Ya retiras a las [hora]. Elige una hora distinta». | Ninguno: cumple. | H9 |
| Pedido ya confirmado y volver a «Mi pedido» | La pestaña muestra «Tu pedido está vacío». | H-03 | H1 / H6 |
| Cantidad máxima (9) | El botón «+» se deshabilita sin aviso. | H-09 | H1 |
| Búsqueda sin tilde | «cafe» devuelve «No encontramos productos…». | H-01 | H2 / H7 |

## 3. Mi lista de problemas y severidad

| # | Problema | Heurística | F | I | P | Severidad (1–4) | Tarea relacionada |
| --- | --- | --- | --- | --- | --- | --- | --- |
| H-01 | Búsqueda sensible a tildes | H2/H7 | 3 | 4 | 4 | 4 · Crítico | T7 |
| H-02 | Producto con pocas unidades se agota recién al confirmar | H5/H9 | 4 | 3 | 3 | 3 · Mayor | T4 |
| H-03 | El pedido confirmado no se encuentra desde «Mi pedido» | H1/H6 | 2 | 3 | 4 | 3 · Mayor | — |
| H-04 | Etiquetas de navegación inconsistentes | H4 | 3 | 2 | 2 | 2 · Menor | — |
| H-05 | Falta información de pago, tiempo y lugar de retiro | H10/H1 | 3 | 2 | 2 | 2 · Menor | T4 |
| H-07 | Textos secundarios menores a 12 px | H8 | 2 | 1 | 1 | 1 · Cosmético | — |
| H-10 | «Sanduche» sin tilde y distinto del nombre en las tareas | H2/H4 | 1 | 1 | 2 | 1 · Cosmético | — |

Elaborado por: Oscar Riofrio · Fecha: 18/11/2026
