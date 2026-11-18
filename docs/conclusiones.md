# Conclusiones del APE 6 — CaféU v3

> ⚠ **DATOS DE USUARIOS SIMULADOS (P1–P3).** Los valores de las sesiones son de ejemplo, coherentes con el comportamiento real del prototipo, pero **no fueron medidos con personas**. Reemplazarlos en `datos/fase3_participantes.json` y ejecutar `python herramientas/generar_fase3_4.py` antes de presentarlos como evidencia empírica.

## Pregunta del laboratorio

> ¿Una interfaz que funciona técnicamente puede ser una mala interfaz? (Verificación vs. validación — Boehm, 1984)

**Sí.** CaféU v3 funciona: las seis tareas base se completaron sin ayuda en el 88,9 % de los intentos y el SUS promedio fue 70,0 (por encima de 68). Sin embargo, al probar funciones que el pilotaje no recorría, el éxito autónomo global bajó a 81,0 % y apareció un fallo de severidad 4 (buscador). Pasar la verificación (el código hace lo que dice) no implica pasar la validación (el usuario logra su meta).

## Conclusiones

1. **La verificación técnica es buena, la validación es parcial.** Eficacia 88,9 % en T1–T6 frente a 81,0 % en T1–T7; mediana global de 30,0 s. T7 (buscador) obtuvo 33,3 % de éxito autónomo y T4, 33,3 %.
2. **Los dos problemas más graves nacen de la prevención de errores y la tolerancia al lenguaje real.** H-01 (el buscador no ignora tildes, severidad 4) y H-02 (la empanada con «Quedan pocas unidades» se agota recién al confirmar, severidad 3) fueron confirmados por ambos métodos.
3. **La triangulación aportó más que cada método por separado.** De 10 hallazgos, 3 (30,0 %) se confirmaron por ambos métodos, 6 salieron solo de la heurística y 1 solo de las sesiones (H-08, el salto a «Mi pedido» al agregar).
4. **La satisfacción oculta la dispersión.** El SUS promedio de 70,0 supera la línea de base, pero P2 puntuó 55,0, la sesión en que el buscador falló por completo.
5. **El backlog es accionable.** Los 10 hallazgos se convirtieron en criterios técnicos verificables (C-01…C-10) y en 10 Issues priorizados: 2 P1, 2 P2, 3 P3 y 3 P4.

## Recomendaciones

- **P1 · H-01:** Normalizar la consulta y los textos del catálogo con `normalize('NFD')` y quitar marcas diacríticas antes de comparar.
- **P1 · H-02:** Avisar en «Mi pedido», antes de confirmar, que el producto puede agotarse; si se agota, mostrar el conflicto sin pasar por «Procesando» y resaltar las dos salidas.
- **P2 · H-03:** Si existe un pedido confirmado y el carrito está vacío, mostrar una tarjeta con su número y un acceso a la confirmación.
- **P2 · H-05:** Agregar un bloque con forma de pago, tiempo estimado y punto de retiro, acordado con la cafetería.
- Repetir la prueba con 5 participantes tras corregir los P1 y P2 para comprobar que T4 y T7 superan la meta.

## Limitaciones

- Evaluación formativa con 3 participantes: sirve para detectar problemas, no para estimar proporciones de la población (Faulkner, 2003).
- Las evaluaciones heurísticas están pre-llenadas a partir de la inspección del código y deben ser confirmadas por cada evaluador.
- Los datos de P1–P3 son simulados; las cifras de este documento deben recalcularse con mediciones reales.

Elaborado por: Oscar Riofrio · Fecha: 18/11/2026
