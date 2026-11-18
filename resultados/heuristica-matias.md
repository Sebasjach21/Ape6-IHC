# Evaluación heurística individual — Matias Morales (E3)

> **Borrador pre-llenado a partir de la inspección del código del prototipo.** Antes de entregar, Matias debe recorrer CaféU v3, confirmar cada hallazgo y ajustar la severidad si no está de acuerdo.

Prototipo: CaféU v3 (`cafeu-v3.html`, repositorio HCI2026-GV, carpeta `APE4-integral/`). Foco de inspección: pantallas posteriores a la confirmación: cambiar hora, cancelar, restaurar. Se recorrió además toda la interfaz.

Severidad (Nielsen, 1995): 1 = cosmético · 2 = menor · 3 = mayor · 4 = crítico, a partir del promedio de **Frecuencia (F)**, **Impacto (I)** y **Persistencia (P)**, cada uno de 1 a 4.

## 1. Las 10 heurísticas

| Heurística | Respuesta | Problema observado / comentario | Pantalla | Evidencia | Hallazgo |
| --- | --- | --- | --- | --- | --- |
| H1 Visibilidad del estado del sistema | No | El pedido confirmado no se encuentra desde «Mi pedido»; Falta información de pago, tiempo y lugar de retiro | Pestaña inferior y botón «Mi pedido»; Pedido confirmado | Verificado en el código (`vPedido` solo lee `carrito`; `pedido` solo se usa en `vConfirmacion`). Verificado en el código (`vConfirmacion`): no hay texto sobre pago, tiempo ni punto de retiro. | H-03, H-05 |
| H2 Relación entre el sistema y el mundo real | Sí | Sin problema observado. Textos y precios en español claro, con el vocabulario de una cafetería. | — | — | — |
| H3 Control y libertad del usuario | Sí | Sin problema observado. «Quitar» ofrece «Deshacer», cancelar pide confirmación y se puede restaurar, y «Cancelar envío» está disponible al procesar. | — | — | — |
| H4 Consistencia y estándares | No | Etiquetas de navegación inconsistentes | Varias pantallas | Verificado en el código: textos en `vInicio`, `vDetalle`, `vPedido`, `vConfirmacion` y en el encabezado/`tabbar`. | H-04 |
| H5 Prevención de errores | No | Producto con pocas unidades se agota recién al confirmar; Horas de retiro fijas y sin relación con la hora actual | Mi pedido → Procesando; Mi pedido y Cambiar hora · lista «Hora de retiro» | Verificado en el código (`iniciarEnvio`): si el pedido incluye la empanada con estado «pocas» pasa a «agotado» y se muestra el conflicto. Verificado en el código: constante `HORAS = ['10:00', …, '12:00']`. | H-02, H-06 |
| H6 Reconocimiento antes que recuerdo | No | El pedido confirmado no se encuentra desde «Mi pedido» | Pestaña inferior y botón «Mi pedido» | Verificado en el código (`vPedido` solo lee `carrito`; `pedido` solo se usa en `vConfirmacion`). | H-03 |
| H7 Flexibilidad y eficiencia de uso | Sí | Sin problema observado. Hay buscador, filtros por categoría y selector de cantidad. | — | — | — |
| H8 Diseño estético y minimalista | Sí | Sin problema observado. Pantallas limpias, una acción principal por pantalla. | — | — | — |
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
| H-02 | Producto con pocas unidades se agota recién al confirmar | H5/H9 | 4 | 3 | 3 | 3 · Mayor | T4 |
| H-03 | El pedido confirmado no se encuentra desde «Mi pedido» | H1/H6 | 2 | 3 | 4 | 3 · Mayor | — |
| H-04 | Etiquetas de navegación inconsistentes | H4 | 3 | 2 | 2 | 2 · Menor | — |
| H-05 | Falta información de pago, tiempo y lugar de retiro | H10/H1 | 3 | 2 | 2 | 2 · Menor | T4 |
| H-06 | Horas de retiro fijas y sin relación con la hora actual | H5 | 2 | 2 | 3 | 2 · Menor | T4 / T5 |

Elaborado por: Matias Morales · Fecha: 18/11/2026
