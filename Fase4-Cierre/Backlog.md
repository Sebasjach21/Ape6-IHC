# Backlog priorizado de mejoras

> ⚠ **DATOS DE USUARIOS SIMULADOS (P1–P3).** Los valores de las sesiones son de ejemplo, coherentes con el comportamiento real del prototipo, pero **no fueron medidos con personas**. Reemplazarlos en `datos/fase3_participantes.json` y ejecutar `python herramientas/generar_fase3_4.py` antes de presentarlos como evidencia empírica.

Cada fila es un GitHub Issue. Los Issues ya están creados en el repositorio (#25 a #34, con el ID `B-01`… en el título); su texto está en `Fase4-Cierre/issues/`. Los Pull Requests los mencionan con `Refs` y no los cierran, porque la mejora en el prototipo todavía no se implementa.

## Regla de prioridad

| Prioridad | Regla | Plazo sugerido |
| --- | --- | --- |
| **P1** | Severidad 4, o severidad 3 confirmada por ambos métodos. | Antes de cualquier uso real |
| **P2** | Severidad 3 detectada por un solo método, o severidad 2 confirmada por ambos. | Siguiente iteración |
| **P3** | Severidad 2 detectada por un solo método. | Cuando haya capacidad |
| **P4** | Severidad 1 (cosmético). | Mejora continua |

## Backlog

| ID | Mejora | Hallazgo | Criterio | Prioridad | Severidad | Esfuerzo | Responsable | Issue |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **B-01** | Normalizar la consulta y los textos del catálogo con `normalize('NFD')` y quitar marcas diacríticas antes de comparar. | H-01 | C-01 | **P1** | 4 · Crítico | Bajo | Julio Jacho | [#25](https://github.com/Sebasjach21/Ape6-IHC/issues/25) |
| **B-02** | Avisar en «Mi pedido», antes de confirmar, que el producto puede agotarse; si se agota, mostrar el conflicto sin pasar por «Procesando» y resaltar las dos salidas. | H-02 | C-02 | **P1** | 3 · Mayor | Medio | Cristian Ango | [#26](https://github.com/Sebasjach21/Ape6-IHC/issues/26) |
| **B-03** | Si existe un pedido confirmado y el carrito está vacío, mostrar una tarjeta con su número y un acceso a la confirmación. | H-03 | C-03 | **P2** | 3 · Mayor | Bajo | Oscar Riofrio | [#27](https://github.com/Sebasjach21/Ape6-IHC/issues/27) |
| **B-05** | Agregar un bloque con forma de pago, tiempo estimado y punto de retiro, acordado con la cafetería. | H-05 | C-05 | **P2** | 2 · Menor | Bajo | Oscar Riofrio | [#29](https://github.com/Sebasjach21/Ape6-IHC/issues/29) |
| **B-04** | Unificar los nombres: «Menú» para volver al menú y una sola entrada a «Mi pedido». | H-04 | C-04 | **P3** | 2 · Menor | Bajo | Matias Morales | [#28](https://github.com/Sebasjach21/Ape6-IHC/issues/28) |
| **B-06** | Generar las horas desde la hora actual hasta el cierre y deshabilitar las que ya pasaron. | H-06 | C-06 | **P3** | 2 · Menor | Medio | Matias Morales | [#30](https://github.com/Sebasjach21/Ape6-IHC/issues/30) |
| **B-08** | Permanecer en el detalle con un aviso y dos botones: «Seguir comprando» y «Ver pedido». | H-08 | C-08 | **P3** | 2 · Menor | Bajo | Cristian Ango | [#32](https://github.com/Sebasjach21/Ape6-IHC/issues/32) |
| **B-07** | Subir esos textos a 0,8125 rem (13 px) como mínimo y comprobar la legibilidad con zoom al 200 %. | H-07 | C-07 | **P4** | 1 · Cosmético | Bajo | Julio Jacho | [#31](https://github.com/Sebasjach21/Ape6-IHC/issues/31) |
| **B-09** | Mostrar «Máximo 9 por producto» y anunciarlo a lectores de pantalla. | H-09 | C-09 | **P4** | 1 · Cosmético | Bajo | Julio Jacho | [#33](https://github.com/Sebasjach21/Ape6-IHC/issues/33) |
| **B-10** | Escribir «Sánduche» en el catálogo y en todos los documentos, y combinarlo con la búsqueda sin tildes. | H-10 | C-10 | **P4** | 1 · Cosmético | Bajo | Oscar Riofrio | [#34](https://github.com/Sebasjach21/Ape6-IHC/issues/34) |

Elaborado por: Oscar Riofrio · Fecha: 18/11/2026
