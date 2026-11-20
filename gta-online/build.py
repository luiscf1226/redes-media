#!/usr/bin/env python3
"""Build GTA Online tip shorts: 1080x1920, H.264 + AAC, voice-only audio (no game audio/music)."""
import json, os, subprocess, sys, math, re

DL = "/tmp/gta/dl"
WORK = "/tmp/gta/work"
OUT = "/tmp/gta/out"
FONT_B = "/usr/share/fonts/opentype/inter/InterDisplay-Black.otf"
FONT_S = "/usr/share/fonts/opentype/inter/Inter-Bold.otf"
VOICE = "es-HN-CarlosNeural"
os.makedirs(WORK, exist_ok=True); os.makedirs(OUT, exist_ok=True)

CREATORS = {
    "brijeshbaghel03": "brijeshbaghel03",
    "tattonpattern": "tattonpattern",
    "casualspikeinthesystem": "casualspikeinthesystem",
    "halinipaw": "halinipaw",
}
SRC = {  # id -> (handle, vertical?)
    "x9wpi70": ("brijeshbaghel03", True),
    "x9wsdm0": ("brijeshbaghel03", True),
    "x9nii6o": ("tattonpattern", False),
    "x97tnwo": ("casualspikeinthesystem", False),
    "x937xn4": ("casualspikeinthesystem", False),
    "x97tnwy": ("casualspikeinthesystem", False),
    "x6gl4vc": ("halinipaw", False),
}

VIDEOS = {
 "gta-tip-cluckin": [
  dict(slot=2, say="¿Querés plata en GTA Online sin gastar un peso?", tip="SIN GASTAR NADA",
       shots=[("x9wsdm0", 13.5)]),
  dict(slot=10, say="Corré el Cluckin' Bell Farm Raid. No pedís propiedad ni setup caro. Solo, en invite only.",
       tip="CLUCKIN' BELL · INVITE ONLY", shots=[("x9wsdm0", 19.0), ("x9wpi70", 0.5)]),
  dict(slot=13, say="Es de lo primero que podés hacer si tu cuenta está en cero. Repetilo y armá tu primer millón.",
       tip="CUENTA EN CERO|→ PRIMER MILLÓN", shots=[("x9wsdm0", 44.0), ("x9wpi70", 41.0), ("x9wpi70", 51.0)]),
  dict(slot=10, say="Guardá este tip y decime si ya lo corriste.", tip="GUARDÁ|¿YA LO CORRISTE?",
       shots=[("x9wpi70", 84.0), ("x9wsdm0", 88.0)]),
 ],
 "gta-tip-acidos": [
  dict(slot=2, say="El tip que casi nadie hace el primer día en GTA Online.", tip="TIP DEL DÍA 1",
       shots=[("x9nii6o", 1281.0)]),
  dict(slot=13, say="Hacé las misiones First Dose. Son gratis y te desbloquean el Acid Lab. Y si seguís con Last Dose, te dan el Virtue. No lo comprés: ya te lo dan.",
       tip="FIRST DOSE → ACID LAB · LAST DOSE → VIRTUE GRATIS",
       shots=[("x9nii6o", 600.0), ("x9nii6o", 960.0), ("x9nii6o", 1120.0)]),
  dict(slot=13, say="Después activás el lab y eso te financia el early game mientras seguís jugando.",
       tip="ACID LAB = EARLY GAME", shots=[("x97tnwo", 19.0), ("x937xn4", 62.0), ("x937xn4", 300.0)]),
  dict(slot=10, say="Guardá y pasáselo a alguien que recién empieza.", tip="GUARDÁ Y COMPARTÍ",
       shots=[("x937xn4", 425.0), ("x97tnwo", 70.0)]),
 ],
 "gta-tip-invite": [
  dict(slot=2, say="Si te matan la venta en público, es porque no usaste este tip.", tip="TIP ANTI-GRIEF",
       shots=[("x97tnwy", 194.0)]),
  dict(slot=12, say="Preps y resupply: siempre invite only. Público solo cuando tengás que vender.",
       tip="PREP = INVITE ONLY · VENTA = PÚBLICO",
       shots=[("x6gl4vc", 93.0), ("x97tnwy", 29.5), ("x97tnwo", 19.0)]),
  dict(slot=12, say="Y después de cada trabajo: depositá en el banco desde el celular. La plata en mano se pierde si te matan.",
       tip="DEPOSITÁ DESPUÉS|DE CADA JOB", shots=[("x6gl4vc", 486.0), ("x6gl4vc", 491.5), ("x97tnwy", 1.0)]),
  dict(slot=10, say="Guardá esto antes de tu próxima sesión.", tip="GUARDÁ EL TIP",
       shots=[("x97tnwy", 360.0), ("x97tnwy", 420.0)]),
 ],
}

def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(" ".join(cmd)); print(r.stderr[-3000:]); sys.exit(1)
    return r.stdout

def dur(f):
    return float(run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f]).strip())

def tts(text, out):
    if os.path.exists(out) and os.path.getsize(out) > 1000:
        return
    env = dict(os.environ, SSL_CERT_FILE="/root/.ccr/ca-bundle.crt")
    subprocess.run(["edge-tts", "--proxy", os.environ["HTTPS_PROXY"], "--voice", VOICE, "--rate", "+6%",
                    "--text", text, "--write-media", out], check=True, env=env, capture_output=True)

def esc_file(path, text):
    with open(path, "w") as fh:
        fh.write(text)
    return path

def wrap(text, n):
    words, lines, cur = text.split(), [], ""
    for w in words:
        if len(cur) + len(w) + 1 > n and cur:
            lines.append(cur); cur = w
        else:
            cur = (cur + " " + w).strip()
    if cur: lines.append(cur)
    return lines

def chunks(text, maxw=5):
    words = text.split()
    out, cur = [], []
    for w in words:
        cur.append(w)
        if len(cur) >= maxw or re.search(r"[.,:?!]$", w) and len(cur) >= 2:
            out.append(" ".join(cur)); cur = []
    if cur:
        if out and len(cur) == 1: out[-1] += " " + cur[0]
        else: out.append(" ".join(cur))
    return out

def render_shot(src, start, length, out):
    handle, vertical = SRC[src]
    inp = os.path.join(DL, src + ".mp4")
    credit = esc_file(out + ".credit.txt", f"Clip: @{handle}")
    cred = (f"drawtext=fontfile={FONT_S}:textfile={credit}:fontsize=40:fontcolor=white:"
            f"box=1:boxcolor=black@0.55:boxborderw=14:x=60:y=1580")
    if vertical:
        vf = (f"[0:v]scale=1088:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,fps=30,"
              f"eq=contrast=1.05:saturation=1.1,{cred}[v]")
    else:
        vf = (f"[0:v]split[a][b];"
              f"[a]scale=-2:1920,crop=1080:1920,boxblur=30:2,eq=brightness=-0.18[bg];"
              f"[b]scale=-2:820,crop=1080:820,eq=contrast=1.05:saturation=1.1[fg];"
              f"[bg][fg]overlay=0:(1920-820)/2-40,setsar=1,fps=30,{cred}[v]")
    run(["ffmpeg", "-v", "error", "-y", "-ss", f"{start}", "-t", f"{length:.3f}", "-i", inp,
         "-filter_complex", vf, "-map", "[v]", "-an", "-c:v", "libx264", "-preset", "medium", "-crf", "18",
         "-pix_fmt", "yuv420p", out])

def build(name, segs):
    wd = os.path.join(WORK, name); os.makedirs(wd, exist_ok=True)
    t = 0.0; timeline = []; shot_files = []; concat = []
    for i, s in enumerate(segs):
        a = os.path.join(wd, f"vo{i}.mp3"); tts(s["say"], a)
        ad = dur(a)
        D = max(s["slot"], ad + 0.6)
        n = len(s["shots"]); per = D / n
        for j, (src, st) in enumerate(s["shots"]):
            f = os.path.join(wd, f"s{i}_{j}.mp4")
            render_shot(src, st, per, f)
            concat.append(f)
        timeline.append(dict(start=t, dur=D, audio=a, adur=ad, say=s["say"], tip=s["tip"]))
        t += D
    total = t
    lst = os.path.join(wd, "list.txt")
    with open(lst, "w") as fh:
        fh.writelines(f"file '{f}'\n" for f in concat)
    base = os.path.join(wd, "base.mp4")
    run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", base])

    # overlays: tip (top) + subtitles (lower third)
    filters = []
    k = 0
    for seg in timeline:
        s0, s1 = seg["start"], seg["start"] + seg["dur"]
        lines = [l.strip() for part in seg["tip"].split(" · ") for l in part.split("|")]
        for li, line in enumerate(lines):
            tf = esc_file(os.path.join(wd, f"tip{k}_{li}.txt"), line)
            y = 230 + li * 100
            fs = 78 if len(line) <= 18 else (70 if len(line) <= 22 else 62)
            filters.append(f"drawtext=fontfile={FONT_B}:textfile={tf}:fontsize={fs}:fontcolor=black:"
                           f"box=1:boxcolor=0xFFD400:boxborderw=22:x=(w-text_w)/2:y={y}:"
                           f"enable='between(t,{s0:.3f},{s1:.3f})'")
        # subtitles: proportional by chars over voice duration
        cs = chunks(seg["say"])
        tot = sum(len(c) for c in cs); vt = seg["start"] + 0.15
        for ci, c in enumerate(cs):
            cd = seg["adur"] * len(c) / tot
            sub = wrap(c, 24)
            for li, line in enumerate(sub):
                tf = esc_file(os.path.join(wd, f"sub{k}_{ci}_{li}.txt"), line)
                y = 1385 + li * 86 - (len(sub) - 1) * 43
                end = vt + cd if ci < len(cs) - 1 else max(vt + cd, s1 - 0.05)
                filters.append(f"drawtext=fontfile={FONT_B}:textfile={tf}:fontsize=68:fontcolor=white:"
                               f"borderw=7:bordercolor=black:x=(w-text_w)/2:y={y}:"
                               f"enable='between(t,{vt:.3f},{end:.3f})'")
            vt += cd
        k += 1
    vf = ",".join(filters)
    # audio: voice segments placed at segment start + 0.15s
    ains = []; amix = []
    for i, seg in enumerate(timeline):
        ains += ["-i", seg["audio"]]
        d = int((seg["start"] + 0.15) * 1000)
        amix.append(f"[{i+1}:a]aresample=48000,adelay={d}|{d},apad[a{i}]")
    af = ";".join(amix) + ";" + "".join(f"[a{i}]" for i in range(len(timeline))) + \
         f"amix=inputs={len(timeline)}:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11,atrim=0:{total:.3f}[aout]"
    out = os.path.join(OUT, name + ".mp4")
    run(["ffmpeg", "-v", "error", "-y", "-i", base, *ains,
         "-filter_complex", f"[0:v]{vf}[vout];{af}", "-map", "[vout]", "-map", "[aout]",
         "-c:v", "libx264", "-profile:v", "high", "-preset", "slow", "-crf", "20", "-pix_fmt", "yuv420p",
         "-r", "30", "-c:a", "aac", "-b:a", "160k", "-ar", "48000", "-ac", "2",
         "-movflags", "+faststart", "-t", f"{total:.3f}", out])
    print(name, f"{total:.2f}s", out)
    with open(os.path.join(wd, "timeline.json"), "w") as fh:
        json.dump(timeline, fh, ensure_ascii=False, indent=1)

if __name__ == "__main__":
    names = sys.argv[1:] or list(VIDEOS)
    for n in names:
        build(n, VIDEOS[n])
