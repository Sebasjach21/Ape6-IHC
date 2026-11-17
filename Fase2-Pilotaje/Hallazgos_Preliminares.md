# Hallazgos preliminares — CaféU v3 (simulado)

> ⚠ **DATOS SIMULADOS — NO SON DATOS REALES DEL PILOTAJE.** Este archivo se llenó con valores de simulación para practicar el procedimiento y el cálculo. Antes de la entrega se deben reemplazar por los datos reales de las sesiones.

Insumo para las Fases 3 y 4. **La severidad final y el backlog priorizado corresponden a las Fases 3 y 4** (no se asignan aquí). Las frases textuales no se definieron en la simulación: se marcan «no registrado».

| # | Qué se observó | Tarea afectada | N.º de participantes (de 3) | Frase textual / evidencia | Posible heurística incumplida | Fuente |
| --- | --- | --- | --- | --- | --- | --- |
| H-01 | La empanada aparece agotada recién al confirmar el pedido; hay que quitarla o sustituirla y volver a confirmar. P3 solo lo resolvió tras la pista | T4 | 3 (P1, P2, P3) | No registrado. Evidencia: P1 la quita, P2 la sustituye por el sánduche, P3 recibe pista (tiempos 54 / 68 / 96 s) | H5 Prevención de errores; H9 Recuperación de errores | Pilotaje (simulado) |
| H-02 | Un producto agotado (jugo) se cuenta como disponible al consultar el menú | T1 | 1 (P3) | No registrado. Evidencia: lo cuenta primero y luego se corrige | H1 Visibilidad del estado; H4 Consistencia | Pilotaje (simulado) |
| H-03 | Al agregar un producto se vuelve al menú después de abrir otro producto | T3 | 1 (P2) | No registrado. Evidencia: error no crítico en T3 | H3 Control y libertad; H6 Reconocimiento antes que recuerdo | Pilotaje (simulado) |
| H-04 | Se sale de la edición de la hora sin guardar, y hay que volver a entrar | T5 | 1 (P3) | No registrado. Evidencia: sale sin guardar y repite el cambio (42 s) | H1 Visibilidad del estado; H5 Prevención de errores | Pilotaje (simulado) |

## Qué aportó cada método

- Aparece en **ambos** métodos (evidencia más fuerte): pendiente, se completa con las evaluaciones heurísticas reales de los cuatro integrantes.
- Solo en el **pilotaje**: H-01 a H-04.
- Solo en la **evaluación heurística**: pendiente, depende de las evaluaciones heurísticas reales.

Elaborado por: Cristian Ango · Fecha: ______
