# APE 6 · Fase 1 — Plan de evaluación de usabilidad de CaféU

**Asignatura:** Interacción Humano / Computador · Quinto semestre de Software · Paralelo A
**Docente:** Ing. José Rubén Caiza Caizabuano, Mg.
**Grupo:** Ango Andrango Cristian Alonso, Jacho Ulcuango Julio Sebastian, Morales Aigaje Matias Benjamin, Riofrio Mora Oscar Adrian
**Prototipo evaluado:** CaféU v3 (construido en APE 4, repositorio [HCI2026-GV](https://github.com/AdrianMora8/HCI2026-GV), carpeta `APE4-integral/`, archivo `prototipo/cafeu-v3.html`)

## 1. Qué se evalúa

CaféU es un prototipo de aplicación web para que estudiantes, docentes y personal de la Universidad Técnica de Ambato pidan en la cafetería universitaria desde el celular, con poco tiempo entre clases, antes de llegar a recogerlo.

La versión v3 permite elegir un producto del menú del día, agregarlo al pedido, completar nombre y hora de retiro, confirmar el pedido, cambiar la hora de retiro o cancelarlo, e incluye los estados de error (campo inválido, producto agotado), procesamiento y éxito.

## 2. Pregunta de evaluación

> ¿En qué medida **CaféU** permite a **un estudiante universitario** **completar un pedido en la cafetería (elegirlo, confirmarlo y, si lo necesita, modificarlo o cancelarlo)** con eficacia, eficiencia y satisfacción, y qué problemas lo impiden?

Las tres dimensiones (eficacia, eficiencia, satisfacción) provienen de la norma ISO 9241-11.

## 3. Métodos elegidos

Se aplican dos métodos que se complementan, tal como lo pide la guía de réplica:

| Método | Tipo | Qué aporta |
| --- | --- | --- |
| Evaluación heurística (10 heurísticas de Nielsen) | Analítico | Los integrantes del grupo revisan el prototipo sin usuarios, anticipan problemas y explican qué principio se viola. |
| Prueba con usuarios y pensamiento en voz alta | Empírico | Usuarios reales ejecutan las seis tareas de la [Tabla de tareas](tareas-usabilidad.md) mientras el grupo mide y observa. |

Lo que ambos métodos encuentran en común es la evidencia más fuerte (triangulación); lo que solo encuentra uno se registra igual, pero con menor peso.

## 4. Participantes

- **Perfil:** estudiantes de la UTA que usarían CaféU para pedir en la cafetería. No participan integrantes del propio grupo.
- **Número:** 3 personas para el pilotaje de la Fase 2 (5 es el ideal si el tiempo lo permite).
- **Criterios de exclusión:** haber participado en el diseño o desarrollo del prototipo, conocer de antemano las seis tareas, ser menor de edad.
- **Identificación:** únicamente los códigos **P1, P2, P3**. Ningún nombre real se sube al repositorio; la hoja de aceptación del consentimiento (ver [Consentimiento informado](consentimiento-informado.md)) se guarda solo con el código.

## 5. Tareas

Las seis tareas, con su meta, tiempo máximo, criterio de éxito y respuesta correcta, están documentadas en [`docs/tareas-usabilidad.md`](tareas-usabilidad.md).

## 6. Métricas y reglas antes de probar

| Métrica | Dimensión | Cómo se calcula |
| --- | --- | --- |
| Tasa de éxito | Eficacia | (participantes con «Sí» / participantes) × 100 |
| Tiempo en tarea | Eficiencia | Desde que el moderador termina de leer la consigna hasta que el usuario termina o abandona la tarea. Se reporta la mediana. |
| Errores | Eficacia y eficiencia | Críticos (impiden terminar la tarea) y no críticos (el usuario se recupera solo). |
| SUS | Satisfacción | 10 ítems de 1 a 5. Impares: valor − 1. Pares: 5 − valor. Suma × 2,5 (escala de 0 a 100; referencia 68). |

Reglas fijadas antes de probar:

- **Éxito:** Sí (sin ayuda), Con ayuda (después de la pista) o No (no termina o supera el tiempo máximo). Solo «Sí» cuenta como éxito para la tasa de éxito.
- **Pista única:** «Vuelve a leer la tarea y revisa las opciones que tienes en pantalla». Se usa siempre igual, leída textualmente, nunca una distinta improvisada.
- **Reinicio entre participantes:** recargar `prototipo/cafeu-v3.html` para dejar el pedido vacío y el menú con el stock inicial (incluido el producto agotado) antes de cada sesión.

## 7. Ética y consentimiento informado

Antes de cada sesión el moderador lee en voz alta el texto de consentimiento (documento completo en [`docs/consentimiento-informado.md`](consentimiento-informado.md)): qué se evalúa (la aplicación, no la persona), cuántas tareas y minutos toma, que es voluntario y se puede detener en cualquier momento, qué se registra, que los datos se guardan únicamente con un código y si se graba la pantalla (solo con permiso explícito y sin publicarla). La aceptación se anota solo con el código del participante, nunca con su nombre.

## 8. Roles del equipo durante la Fase 2

| Rol | Qué hace | Responsable sugerido |
| --- | --- | --- |
| Moderador | Lee el guion y las tareas palabra por palabra. No ayuda ni señala la pantalla. | Cristian Ango |
| Registro de métricas | Una sola persona cronometra y anota éxito, tiempo y errores. | Julio Jacho |
| Observador | Anota frases textuales, dudas y la posible heurística violada. | Oscar Riofrio |
| Soporte técnico | Deja el prototipo en el estado inicial entre participantes y controla la grabación. | Matias Morales |

## 9. Hoja de observación

El formato de la hoja de observación por participante, con el cuestionario SUS y la pregunta de cierre, está en [`docs/hoja-observacion-sus.md`](hoja-observacion-sus.md).

## 10. Criterios de que el protocolo está listo para la Fase 2

El protocolo de la Fase 1 se considera listo para pasar a la Fase 2 (prueba con participantes reales) cuando, en el pilotaje interno:

- Nadie pide repetir una tarea porque la consigna es ambigua.
- Al menos 2 de 3 participantes terminan cada tarea antes del tiempo máximo.
- La hoja de observación permite registrar todo lo que ocurre sin improvisar casillas nuevas.
- No hay fallos técnicos del prototipo durante el recorrido completo de las seis tareas.
- La sesión completa (seis tareas + SUS + cierre) dura 20 minutos o menos.

## Lista de entrega de la Fase 1

- [x] Plan con objeto, pregunta, métodos, participantes, métricas, reglas, roles, ética y criterios de validación (este documento)
- [ ] Consentimiento informado anonimizado — `docs/consentimiento-informado.md`
- [ ] Seis tareas con meta, tiempo máximo, criterio de éxito y respuesta correcta — `docs/tareas-usabilidad.md`
- [ ] Hoja de observación con el SUS — `docs/hoja-observacion-sus.md`
- [ ] Todo subido al repositorio del grupo, con commits de cada integrante
