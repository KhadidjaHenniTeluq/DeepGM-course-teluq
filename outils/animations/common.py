from manim import *
import numpy as np

# Palette (dérivée des couleurs du cours LaTeX)
BG = "#0E1A24"
FG = "#E8EEF2"
MUTED = "#8FA3B3"
BLUE = "#7FB2E5"
TEAL = "#5FB3A1"
ORANGE = "#E07A4F"
GOLD = "#E8C468"
ROSE = "#D9738F"
FONT = "Inter"

config.background_color = BG

MathTex.set_default(color=FG)
Tex.set_default(color=FG)


def T(text, size=32, color=FG, weight=NORMAL, max_width=12.5, **kw):
    t = Text(text, font=FONT, font_size=size, color=color, weight=weight, **kw)
    if t.width > max_width:
        t.scale_to_fit_width(max_width)
    return t


class Week(Scene):
    """Scène de base : carte de titre, sous-titres et conclusion communes."""

    week = 1
    title = ""
    keywords = ""
    question = ""

    def intro(self):
        badge = T(f"SEMAINE {self.week}", 26, TEAL, weight=BOLD)
        course = T("MODÈLES GÉNÉRATIFS PROFONDS", 20, MUTED)
        title = T(self.title, 54, FG, weight=BOLD)
        kw = T(self.keywords, 26, BLUE)
        line = Line(LEFT * 3, RIGHT * 3, color=TEAL, stroke_width=2)
        grp = VGroup(course, badge, title, line, kw).arrange(DOWN, buff=0.35)
        self.play(FadeIn(course, shift=DOWN * 0.2), FadeIn(badge, shift=DOWN * 0.2), run_time=0.8)
        self.play(Write(title), run_time=1.4)
        self.play(Create(line), FadeIn(kw), run_time=0.9)
        self.wait(1.6)
        self.play(FadeOut(grp), run_time=0.6)

        lab = T("QUESTION CENTRALE", 22, GOLD, weight=BOLD)
        q = Paragraph(*self.question.split("\n"), font=FONT, font_size=36, color=FG,
                      alignment="center", line_spacing=0.9)
        if q.width > 12.5:
            q.scale_to_fit_width(12.5)
        box = SurroundingRectangle(q, color=GOLD, buff=0.45, corner_radius=0.15, stroke_width=2)
        g = VGroup(lab, VGroup(q, box)).arrange(DOWN, buff=0.4)
        self.play(FadeIn(lab), Create(box), run_time=0.8)
        self.play(Write(q), run_time=2.0)
        self.wait(2.8)
        self.play(FadeOut(g), run_time=0.6)
        self.cap = None

    def say(self, text, wait=2.5, color=FG):
        """Sous-titre en bas de l'écran (narration écrite)."""
        new = Paragraph(*text.split("\n"), font=FONT, font_size=28, color=color,
                        alignment="center", line_spacing=0.8)
        if new.width > 13:
            new.scale_to_fit_width(13)
        new.to_edge(DOWN, buff=0.35)
        bg = BackgroundRectangle(new, color=BG, fill_opacity=0.85, buff=0.15)
        grp = VGroup(bg, new)
        if self.cap is None:
            self.play(FadeIn(grp, shift=UP * 0.15), run_time=0.5)
        else:
            self.play(FadeOut(self.cap, run_time=0.3), FadeIn(grp, shift=UP * 0.15, run_time=0.5))
        self.cap = grp
        if wait:
            self.wait(wait)

    def header(self, text):
        h = T(text, 30, TEAL, weight=BOLD).to_edge(UP, buff=0.4)
        self.play(FadeIn(h, shift=DOWN * 0.2), run_time=0.6)
        return h

    def clear_all(self):
        mobs = [m for m in self.mobjects]
        if mobs:
            self.play(*[FadeOut(m) for m in mobs], run_time=0.6)
        self.cap = None

    def outro(self, nxt=""):
        self.clear_all()
        t = T("À vous de jouer", 44, FG, weight=BOLD)
        steps = VGroup(
            T("1.  Téléchargez le support PDF de la semaine", 28, BLUE),
            T("2.  Réalisez le laboratoire", 28, TEAL),
            T("3.  Testez-vous avec le quiz", 28, GOLD),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        g = VGroup(t, steps).arrange(DOWN, buff=0.6)
        if nxt:
            n = T(nxt, 22, MUTED)
            g = VGroup(g, n).arrange(DOWN, buff=0.7)
        self.play(FadeIn(t, shift=UP * 0.2), run_time=0.7)
        self.play(LaggedStart(*[FadeIn(s, shift=RIGHT * 0.3) for s in steps], lag_ratio=0.4), run_time=1.8)
        if nxt:
            self.play(FadeIn(g[1]), run_time=0.6)
        self.wait(3)
        self.play(FadeOut(g), run_time=0.8)


def gauss_cloud(center, n, sigma, rng, color, radius=0.045):
    pts = rng.normal(0, sigma, size=(n, 2)) + np.array(center)[:2]
    return VGroup(*[Dot([p[0], p[1], 0], radius=radius, color=color) for p in pts]), pts
