# Videos 3C: Biblia y Devocional AI

| Archivo | Estado | Duración | Resolución | Códecs |
|---|---|---|---|---|
| `bible-devocional-dia.mp4` | Listo | 31.8 s | 1080×1920 | h264 / aac (pista de audio en silencio) |
| `bible-preguntas.mp4` | **Bloqueado**: no se generó | — | — | — |
| `bible-david.mp4` | **Bloqueado**: no se generó | — | — | — |

## bible-devocional-dia.mp4

Grabado de la app real publicada en web (https://bible-ai-honduras.vercel.app/hoy), contra el backend
de producción, el 25 nov 2026. Es el devocional del día tal cual sale en la app (sin login).

- 0–6 s: inicio del devocional (imagen, versículo, oración inicial). Texto: "El devocional de hoy".
- 6–17 s: scroll por introducción, pausa para hoy y oración final. Texto: "Versículo + reflexión + oración".
- 17–24 s: cierre del devocional. Texto: "Cinco minutos para arrancar el día".
- 24–32 s: CTA "3C: Biblia y Devocional AI" / "Descarga la app" / apps.apple.com/hn/app/3c-biblia-y-devocional-ai/id6807627270. Sin precio.

**Desvío del guion:** el guion decía "Un devocional hecho para vos" y "Devocional diario personalizado"
(elegir cómo me siento). Eso es la función Sentir, que exige sesión iniciada, así que no se pudo grabar.
Se cambió el texto en pantalla a frases que describen lo que de verdad se ve (el devocional del día).

### Versículos en pantalla

| Cita | Texto exacto (RV1909) | Verificación |
|---|---|---|
| Filipenses 1:3 | "Doy gracias á mi Dios en toda memoria de vosotros," | Coincide con el lector de la app (`/leer/Filipenses/1`, v. 3) |

## Por qué faltan bible-preguntas y bible-david

Preguntar y Personajes (Voces) exigen sesión: en la web de producción, enviar una pregunta devuelve
`ConvexError: No autenticado` (`convex/qa.ts`), igual que Voces. Entrar requiere código por correo,
Google o Apple, y no hay acceso a ninguno de esos desde el entorno donde se generaron los videos. El
qa-harness usa respuestas simuladas, así que no sirve (regla: nada inventado).

Para terminarlos: grabación de pantalla del celular con sesión iniciada (una pregunta real con su
respuesta citada; el chat con David sobre Goliat), o una cuenta de prueba que se pueda usar sin código
por correo. Detalle en luiscf1226/bible-ai-honduras#280.
