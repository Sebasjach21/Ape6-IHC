# Fase 3 · Siete tareas de usabilidad (protocolo V2)

Cada consigna se lee palabra por palabra, sin nombrar botones ni pantallas. El tiempo máximo es el doble de la meta.

| ID | Consigna que se lee | Meta | Tiempo máximo | Criterio de éxito observable | Respuesta correcta |
| --- | --- | --- | --- | --- | --- |
| T1 | ¿Qué productos ofrece el menú de hoy? | 60 s | 120 s | Nombra los productos disponibles o dice cuántos hay. | Café americano, Sanduche de queso y Empanada de pollo disponibles; el jugo de naranja figura como «Agotado hoy» (3 disponibles de 4 productos). |
| T2 | Agrega un café americano a tu pedido. | 60 s | 120 s | 1 café americano queda en el pedido. | 1 café americano — $1,50. |
| T3 | Agrega también una empanada de pollo. | 60 s | 120 s | El pedido tiene 1 café americano y 1 empanada de pollo. | Café americano + empanada de pollo — $3,00. |
| T4 | Escribe tu nombre, elige una hora de retiro, confirma tu pedido y dime tu número de pedido. | 90 s | 180 s | El pedido queda confirmado y el participante dice el número que aparece en pantalla. | **#CU-104.** Al confirmar por primera vez la empanada se agota (el prototipo lo hace siempre): el participante debe quitarla (total $1,50) o cambiarla por el sánduche (total $4,25) y confirmar de nuevo. |
| T5 | Cambia la hora de retiro de tu pedido confirmado a las 12:00. | 90 s | 180 s | La hora queda en 12:00 y el pedido sigue confirmado. | Hora de retiro 12:00, mismo número de pedido. |
| T6 | Ya no quieres este pedido. Cancélalo y confirma que quedó cancelado. | 60 s | 120 s | El pedido pasa a cancelado y se ve la opción «Restaurar». | Pedido cancelado; botón «Restaurar pedido» visible. |
| T7 | Quieres pedir un café, pero no quieres recorrer toda la lista. Búscalo escribiendo «cafe» y agrégalo a tu pedido. | 60 s | 120 s | El café americano queda agregado al pedido usando el buscador. | Café americano en el pedido (cantidad 1). **Tarea de refuerzo:** el buscador no ignora tildes y «cafe» no devuelve resultados; con «café» sí. |

## Reglas

- T7 se aplica al final, con el pedido de T6 ya cancelado; el estado de la búsqueda no depende de pedidos previos.
- Solo «Sí» cuenta como éxito autónomo. «Con ayuda» es tras la pista única; «No» es abandono o superar el máximo.
- Quitar o cambiar la empanada en T4 y volver a confirmar es un error **no crítico**.

Elaborado por: Cristian Ango · Fecha: 18/11/2026
