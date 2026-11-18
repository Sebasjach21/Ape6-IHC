# Métricas de usabilidad — CaféU v3 (ISO 9241-11:2018)

> ⚠ **DATOS DE USUARIOS SIMULADOS (P1–P3).** Los valores de las sesiones son de ejemplo, coherentes con el comportamiento real del prototipo, pero **no fueron medidos con personas**. Reemplazarlos en `datos/fase3_participantes.json` y ejecutar `python herramientas/generar_fase3_4.py` antes de presentarlos como evidencia empírica.

Fuentes: `resultados/P1.md`, `P2.md` y `P3.md`. Cálculo: tasa de éxito = «Sí» ÷ participantes; mediana de tiempo por tarea; errores = suma de los tres participantes; SUS = (impares ajustados + pares ajustados) × 2,5.

## Tabla 1. Eficacia y eficiencia por tarea

| Tarea | Consigna | Meta / Máx (s) | Éxito sin ayuda | Tasa de éxito | Con ayuda | Tiempos P1 · P2 · P3 (s) | Mediana (s) | ¿Mediana ≤ meta? | Err. críticos | Err. no críticos |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **T1** | ¿Qué productos ofrece el menú de hoy? | 60 / 120 | 3/3 | 100,0 % | 0 | 16 · 22 · 27 | 22,0 | Sí | 0 | 1 |
| **T2** | Agrega un café americano a tu pedido. | 60 / 120 | 3/3 | 100,0 % | 0 | 24 · 29 · 19 | 24,0 | Sí | 0 | 0 |
| **T3** | Agrega también una empanada de pollo. | 60 / 120 | 3/3 | 100,0 % | 0 | 41 · 55 · 38 | 41,0 | Sí | 0 | 2 |
| **T4** | Escribe tu nombre, elige una hora de retiro, confirma tu … | 90 / 180 | 1/3 | 33,3 % | 2 | 134 · 102 · 141 | 134,0 | No | 0 | 5 |
| **T5** | Cambia la hora de retiro de tu pedido confirmado a las 12… | 90 / 180 | 3/3 | 100,0 % | 0 | 21 · 30 · 35 | 30,0 | Sí | 0 | 0 |
| **T6** | Ya no quieres este pedido. Cancélalo y confirma que quedó… | 60 / 120 | 3/3 | 100,0 % | 0 | 17 · 26 · 22 | 22,0 | Sí | 0 | 0 |
| **T7** | Quieres pedir un café, pero no quieres recorrer toda la l… | 60 / 120 | 1/3 | 33,3 % | 1 | 98 · 120 · 47 | 98,0 | No | 1 | 5 |

## Tabla 2. Síntesis global

| Dimensión ISO 9241-11 | T1–T6 (tareas base) | T1–T7 (con refuerzo) | Meta | Lectura |
| --- | --- | --- | --- | --- |
| Eficacia · tasa de éxito autónomo | 88,9 % (16/18) | 81,0 % (17/21) | ≥ 80 % | Se cumple en conjunto; T4 y T7 quedan por debajo. |
| Eficiencia · mediana de tiempo | 28,0 s | 30,0 s | Mediana ≤ meta de cada tarea | 5 de 7 tareas dentro de la meta. |
| Eficacia · errores críticos | 0 | 1 | 0 | El único error crítico está en el buscador (T7). |
| Eficacia · errores no críticos | 8 | 13 | ≤ 1 por tarea | Se concentran en T4 (empanada agotada), T7 (buscador) y T3 (salto a «Mi pedido»). |

## Tabla 3. Satisfacción: SUS (Brooke, 1996)

| Participante | Respuestas 1–10 | Suma impares (r−1) | Suma pares (5−r) | SUS (0–100) | Escala adjetiva | ¿≥ 68? |
| --- | --- | --- | --- | --- | --- | --- |
| P1 | 4 · 2 · 4 · 1 · 4 · 2 · 5 · 2 · 4 · 2 | 16 | 16 | 80,0 | Bueno | Sí |
| P2 | 3 · 3 · 4 · 2 · 3 · 3 · 3 · 3 · 3 · 3 | 11 | 11 | 55,0 | Aceptable bajo / regular | No |
| P3 | 4 · 2 · 5 · 2 · 4 · 2 · 4 · 2 · 4 · 3 | 16 | 14 | 75,0 | Bueno | Sí |
| **Promedio** | — | — | — | **70,0** | Bueno | Sí |

**Lectura:** el SUS promedio es 70,0, superior a la referencia de la industria (68,0). P2 dio el puntaje más bajo (55,0). La puntuación SUS no es un porcentaje.

## Tabla 4. Criterios del protocolo (Fase 1) frente a las sesiones

| Criterio | ¿Se cumplió? | Dato |
| --- | --- | --- |
| Nadie pide repetir una tarea por consigna ambigua | No | 2 solicitudes de repetir (en T4) |
| Al menos 2 de 3 terminan cada tarea antes del tiempo máximo | Sí | T1: 3/3; T2: 3/3; T3: 3/3; T4: 3/3; T5: 3/3; T6: 3/3; T7: 3/3 |
| La hoja permite registrar todo sin improvisar | Sí | Se usaron solo los campos de la hoja V2 |
| Sin fallos técnicos del prototipo | Sí | Ninguno registrado |
| Sesión completa ≤ 20 minutos | No | Duración máxima: 23 min (P1 19, P2 23, P3 21) |

Elaborado por: Julio Jacho · Fecha: 18/11/2026
