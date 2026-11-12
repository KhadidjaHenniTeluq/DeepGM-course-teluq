# Animations d'introduction (Manim)

Les 15 vidéos de `static/videos/` sont générées par ces scripts [Manim Community](https://www.manim.community/).

- `common.py` : palette, carte de titre, sous-titres et écran de fin communs.
- `weeks_a.py` (S01–S05), `weeks_b.py` (S06–S10), `weeks_c.py` (S11–S15) : une scène par semaine.

Pour régénérer une vidéo (ex. semaine 7) en 720p :

```bash
cd outils/animations
manim -qm weeks_b.py S07
cp media/videos/weeks_b/720p30/S07.mp4 ../../static/videos/semaine-07.mp4
# image d'aperçu (affiche) :
ffmpeg -y -ss 4 -i ../../static/videos/semaine-07.mp4 -frames:v 1 ../../static/videos/semaine-07.jpg
```

Utilisez `-qh` pour du 1080p. Le texte des sous-titres se modifie dans les appels `self.say("...")`.
