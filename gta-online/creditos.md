# GTA Online — 3 videos tip (créditos y captions)

Gameplay 100 % real de GTA Online, tomado de creadores en Dailymotion (fragmentos de 3–8 s, sin audio original: sin música de Rockstar).
Voz: TTS es-HN (CarlosNeural) leyendo el tip original. Crédito "Clip: @handle" fijo en pantalla en cada toma.

## gta-tip-cluckin.mp4 (36.9 s)
Clips: @brijeshbaghel03 (Dailymotion)
- https://www.dailymotion.com/video/x9wsdm0 — "GTA Online : The Cluckin' Bell Farm Raid - Scene of the Crime" (13.5 s, 19 s, 44 s, 88 s)
- https://www.dailymotion.com/video/x9wpi70 — "GTA Online : The Cluckin' Bell Farm Raid - Hit and Run" (0.5 s, 41 s, 51 s, 84 s)

Caption:
> ¿Plata en GTA Online sin gastar nada? Corré el Cluckin' Bell Farm Raid solo, en invite only 🐔💸 Guardá el tip.
> Clip: @brijeshbaghel03
> #GTAOnline #GTA5 #GTAtips

## gta-tip-acidos.mp4 (40.4 s)
Clips: @tattonpattern, @casualspikeinthesystem (Dailymotion)
- https://www.dailymotion.com/video/x9nii6o — Tatton Pattern, "GTA V Online First Dose 2 - Designated Driver" (600 s, 960 s, 1120 s, 1281 s)
- https://www.dailymotion.com/video/x97tnwo — CasualSpikeInTheSystem, "GTA Online Acid Product Paperboy Sell Mission Day 1" (19 s, 70 s)
- https://www.dailymotion.com/video/x937xn4 — CasualSpikeInTheSystem, "GTA Online Acid Product Stash Sell Mission" (62 s, 300 s, 425 s)

Nota: el guion original decía que First Dose te da el Virtue. Se corrigió: First Dose desbloquea el Acid Lab; el Virtue gratis se da al completar Last Dose (fuente: GTA Wiki, "Virtue").

Caption:
> Tip del día 1 en GTA Online: hacé First Dose → Acid Lab gratis. Seguí con Last Dose → Virtue gratis. No lo comprés 🧪
> Clips: @tattonpattern · @casualspikeinthesystem
> #GTAOnline #GTA5 #GTAtips

## gta-tip-invite.mp4 (38.6 s)
Clips: @casualspikeinthesystem, @halinipaw (Dailymotion)
- https://www.dailymotion.com/video/x97tnwy — CasualSpikeInTheSystem, "GTA Online Bunker Research Mission Day 1" (1 s, 29.5 s, 194 s, 360 s, 420 s)
- https://www.dailymotion.com/video/x97tnwo — CasualSpikeInTheSystem, "GTA Online Acid Product Paperboy Sell Mission Day 1" (19 s)
- https://www.dailymotion.com/video/x6gl4vc — Halinipaw, "GTA 5 Online: How to get a Solo Public Lobby Session..." (93 s, 486 s, 491.5 s)

Caption:
> Tip anti-grief: preps y resupply en invite only, público solo para vender. Y depositá en el banco después de cada job 🏦
> Clips: @casualspikeinthesystem · @halinipaw
> #GTAOnline #GTA5 #GTAtips

## Cómo se armó
`build.py` (ffmpeg + edge-tts): baja cada toma, la pone a 1080x1920 (las horizontales sobre fondo desenfocado), crédito por toma, tip arriba y subtítulos abajo, voz normalizada a -14 LUFS, H.264 High + AAC.
