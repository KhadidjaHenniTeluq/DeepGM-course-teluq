from common import *


def mix_score(p, centers, s=0.5):
    x = np.array(p[:2])
    w, g = [], []
    for c in centers:
        d = x - np.array(c)
        wk = np.exp(-d @ d / (2 * s * s))
        w.append(wk)
        g.append(-d / (s * s))
    w = np.array(w) + 1e-12
    w = w / w.sum()
    v = sum(wi * gi for wi, gi in zip(w, g))
    return np.array([v[0], v[1], 0])


class S11(Week):
    week = 11
    title = "Score Matching"
    keywords = "Score de Hyvärinen · Denoising SM · Langevin"
    question = "Peut-on apprendre la direction vers les régions probables\nsans normaliser la densité p(x) ?"

    def construct(self):
        self.intro()
        h = self.header("Le score : un champ de vecteurs")
        eq = MathTex(r"s(x) = \nabla_x \log p(x)", color=GOLD).move_to(LEFT * 3.5 + UP * 2.55)
        centers = [(-2.2, 0.6), (2.0, -0.4), (0.2, -1.5)]
        field = ArrowVectorField(lambda p: 0.22 * mix_score(p, centers, 0.9),
                                 x_range=[-6, 6, 0.6], y_range=[-2.4, 1.8, 0.6],
                                 colors=[BLUE, TEAL, GOLD], length_func=lambda n: min(n, 0.5))
        self.play(Write(eq))
        self.play(Create(field), run_time=2)
        self.say("En chaque point, la flèche indique où la densité augmente.", 3)
        ez = MathTex(r"\nabla_x \log \frac{e^{-E(x)}}{Z} = -\nabla_x E(x)", color=TEAL, font_size=38).move_to(RIGHT * 3.3 + UP * 2.55)
        self.play(Write(ez))
        self.say("Bonus : Z disparaît en dérivant par rapport à x !", 3, GOLD)
        # Langevin particles
        rng = np.random.default_rng(11)
        pts = [rng.uniform([-5.5, -2.3], [5.5, 1.7]) for _ in range(30)]
        dots = VGroup(*[Dot([p[0], p[1], 0], radius=0.07, color=ROSE) for p in pts])
        self.play(FadeIn(dots))
        self.say("Dynamique de Langevin : suivre le score + un peu de bruit.", 0)
        eta = 0.08
        for _ in range(22):
            for k in range(len(pts)):
                sc = mix_score(np.r_[pts[k], 0], centers, 0.9)[:2]
                pts[k] = pts[k] + eta * sc + np.sqrt(2 * eta) * 0.25 * rng.normal(size=2)
            self.play(*[d.animate.move_to([p[0], p[1], 0]) for d, p in zip(dots, pts)], run_time=0.13, rate_func=linear)
        self.wait(1)
        self.clear_all()

        h = self.header("Denoising Score Matching")
        x = Dot(LEFT * 2, color=BLUE, radius=0.12)
        xt = Dot(RIGHT * 1.5 + UP * 1.0, color=ORANGE, radius=0.12)
        lx = MathTex("x", color=BLUE).next_to(x, DOWN)
        lxt = MathTex(r"\tilde{x} = x + \sigma\varepsilon", color=ORANGE).next_to(xt, UP)
        self.play(FadeIn(x), Write(lx))
        self.play(TransformFromCopy(x, xt), Write(lxt))
        ar = Arrow(xt.get_center(), x.get_center(), color=GOLD, buff=0.15)
        tg = MathTex(r"\text{cible} = -\varepsilon / \sigma", color=GOLD).next_to(ar, DOWN, buff=0.3)
        self.play(GrowArrow(ar), Write(tg))
        self.say("On bruite les données ; le réseau apprend à pointer\nvers la version propre. Débruiter = estimer le score.", 4)
        self.outro("Semaine suivante : modèles de diffusion")


class S12(Week):
    week = 12
    title = "Modèles de diffusion"
    keywords = "Processus direct / inverse · DDPM · génération progressive"
    question = "Comment apprendre à transformer progressivement\ndu bruit aléatoire en une donnée réaliste ?"

    def construct(self):
        self.intro()
        h = self.header("Processus direct : des données vers le bruit")
        rng = np.random.default_rng(12)
        n = 160
        t = rng.uniform(0.5, 3.0 * np.pi, n)
        data = np.c_[t * np.cos(t), t * np.sin(t)] * 0.27 + rng.normal(0, 0.05, (n, 2))
        noise = rng.normal(0, 1.0, (n, 2))
        dots = VGroup(*[Dot([p[0], p[1] - 0.2, 0], radius=0.045, color=GOLD) for p in data])
        tl = MathTex(r"x_0").to_corner(UR).shift(DOWN * 0.9 + LEFT * 0.4)
        self.play(FadeIn(dots), Write(tl))
        eq = MathTex(r"x_t = \sqrt{\bar\alpha_t}\,x_0 + \sqrt{1-\bar\alpha_t}\,\varepsilon", color=FG, font_size=38).to_corner(UL).shift(DOWN * 0.9)
        self.play(Write(eq))
        for ab, lab in [(0.8, "x_{t_1}"), (0.4, "x_{t_2}"), (0.0, "x_T")]:
            new = [np.sqrt(ab) * d + np.sqrt(1 - ab) * e for d, e in zip(data, noise)]
            col = interpolate_color(ManimColor(GOLD), ManimColor(MUTED), 1 - ab)
            nl = MathTex(lab).move_to(tl)
            self.play(*[d.animate.move_to([p[0], p[1] - 0.2, 0]).set_color(col) for d, p in zip(dots, new)],
                      Transform(tl, nl), run_time=1.4)
            self.wait(0.4)
        self.say("Détruire la structure est facile : on ajoute du bruit gaussien.", 3)
        self.play(FadeOut(h))
        h = self.header("Processus inverse : apprendre à débruiter")
        self.say("Un réseau εθ(xₜ, t) apprend à prédire le bruit ajouté.", 0)
        for ab, lab in [(0.4, "x_{t_2}"), (0.8, "x_{t_1}"), (1.0, "x_0")]:
            new = [np.sqrt(ab) * d + np.sqrt(1 - ab) * e for d, e in zip(data, noise)]
            col = interpolate_color(ManimColor(GOLD), ManimColor(MUTED), 1 - ab)
            nl = MathTex(lab).move_to(tl)
            self.play(*[d.animate.move_to([p[0], p[1] - 0.2, 0]).set_color(col) for d, p in zip(dots, new)],
                      Transform(tl, nl), run_time=1.4)
            self.wait(0.3)
        self.say("Génération : partir de xT ∼ N(0, I) et remonter pas à pas.\nTrès bonne qualité… mais de nombreuses étapes (DDIM accélère).", 4)
        self.clear_all()
        h = self.header("La perte DDPM")
        loss = MathTex(r"\mathcal{L} = \mathbb{E}_{x_0,t,\varepsilon}\left\| \varepsilon - \varepsilon_\theta(x_t, t)\right\|^2", color=TEAL).shift(UP * 0.4)
        self.play(Write(loss), run_time=2)
        self.say("Une simple régression du bruit — et le lien direct avec le score.", 3)
        self.outro("Semaine suivante : modèles hiérarchiques")


class S13(Week):
    week = 13
    title = "Modèles hiérarchiques"
    keywords = "Latents multi-niveaux · multi-échelle · StyleGAN"
    question = "Comment générer une donnée complexe en organisant\nses facteurs latents à plusieurs niveaux ?"

    def construct(self):
        self.intro()
        h = self.header("Du global vers le local")
        levels = []
        L = 4
        y0 = 2.3
        cols = [GOLD, ORANGE, TEAL, BLUE]
        for l in range(L):
            k = 2 ** l
            xs = np.linspace(-5.5, 5.5, 2 * k + 1)[1::2]
            levels.append(VGroup(*[Circle(0.22 if l < 3 else 0.17, color=cols[l], fill_opacity=0.45).move_to([x, y0 - 1.2 * l, 0]) for x in xs]))
        edges = VGroup()
        anims = []
        self.play(GrowFromCenter(levels[0][0]))
        for l in range(1, L):
            e = VGroup()
            for i, c in enumerate(levels[l]):
                e.add(Line(levels[l - 1][i // 2].get_bottom(), c.get_top(), color=MUTED, stroke_width=1.5))
            edges.add(e)
            self.play(Create(e), LaggedStart(*[GrowFromCenter(c) for c in levels[l]], lag_ratio=0.1), run_time=1.0)
        lab = VGroup(T("latent racine : structure globale", 20, GOLD).next_to(levels[0], RIGHT, buff=0.4),
                     T("feuilles : détails locaux observés", 20, BLUE).next_to(levels[3], DOWN, buff=0.3))
        self.play(FadeIn(lab))
        self.say("Random Hierarchy Model : un latent haut placé\ncontrôle un bloc de s^L feuilles.", 3.5)
        self.play(Indicate(levels[1][0], color=ROSE), *[Indicate(levels[3][i], color=ROSE) for i in range(4)], run_time=1.5)
        self.clear_all()

        h = self.header("Génération multi-échelle")
        rng = np.random.default_rng(13)
        base = rng.random((8, 8))
        img = np.kron(np.array([[0.2, 0.8], [0.7, 0.3]]), np.ones((4, 4)))
        img = 0.7 * img + 0.3 * base

        def grid(res):
            bl = 8 // res
            g = VGroup()
            for i in range(res):
                for j in range(res):
                    v = img[i * bl:(i + 1) * bl, j * bl:(j + 1) * bl].mean()
                    g.add(Square(4.0 / res, stroke_width=0.5, stroke_color=BG,
                                 fill_color=interpolate_color(ManimColor("#1d3b55"), ManimColor(GOLD), v), fill_opacity=1))
            return g.arrange_in_grid(res, res, buff=0)

        g = grid(1).shift(DOWN * 0.2)
        rl = T("1 × 1", 26, MUTED).next_to(g, RIGHT, buff=0.6)
        self.play(FadeIn(g), FadeIn(rl))
        for r in [2, 4, 8]:
            ng = grid(r).move_to(g)
            nr = T(f"{r} × {r}", 26, MUTED).move_to(rl)
            self.play(FadeOut(g), FadeIn(ng), Transform(rl, nr), run_time=1.2)
            g = ng
            self.wait(0.6)
        self.say("StyleGAN : le style w agit du grossier au fin (AdaIN),\nle bruit injecté ajoute la variation locale.", 4)
        self.outro("Semaine suivante : hybridation et modèles modernes")


class S14(Week):
    week = 14
    title = "Hybridation & modèles modernes"
    keywords = "LDM · Flow Matching · Scaling laws · Foundation models"
    question = "Comment combiner les forces de plusieurs modèles\net passer à grande échelle ?"

    def construct(self):
        self.intro()
        h = self.header("Latent Diffusion : diffuser dans un espace compressé")
        img = Square(2.2, color=FG, fill_color="#28445e", fill_opacity=1).move_to(LEFT * 5)
        il = T("512×512×3", 20, MUTED).next_to(img, DOWN)
        enc = T("Encodeur", 24, BLUE)
        lat = Square(0.9, color=GOLD, fill_opacity=0.35)
        ll = T("64×64×4", 20, MUTED).next_to(lat, DOWN)
        dif = T("diffusion", 24, TEAL)
        dec = T("Décodeur", 24, BLUE)
        out = Square(2.2, color=FG, fill_color="#3f6a5f", fill_opacity=1).move_to(RIGHT * 5)
        row = VGroup(enc, VGroup(lat, ll), dif, dec).arrange(RIGHT, buff=0.6).shift(DOWN * 0.0)
        row.move_to(ORIGIN)
        self.play(FadeIn(img), FadeIn(il))
        a1 = Arrow(img.get_right(), enc.get_left(), color=MUTED, buff=0.1)
        a2 = Arrow(dec.get_right(), out.get_left(), color=MUTED, buff=0.1)
        self.play(GrowArrow(a1), FadeIn(enc), FadeIn(row[1]))
        loop = CurvedArrow(lat.get_top() + UP * 0.05, dif.get_top() + UP * 0.05, angle=-PI / 2, color=TEAL)
        self.play(Create(loop), FadeIn(dif))
        self.play(FadeIn(dec), GrowArrow(a2), FadeIn(out))
        self.say("Environ 48 fois moins de valeurs à débruiter :\nc'est l'idée de Stable Diffusion.", 3.5)
        self.clear_all()

        h = self.header("Flow Matching : des trajectoires droites")
        rng = np.random.default_rng(14)
        x0 = rng.normal(0, 0.5, (24, 2)) + np.array([-4, 0])
        ang = rng.uniform(0, 2 * np.pi, 24)
        x1 = np.c_[1.4 * np.cos(ang), 1.4 * np.sin(ang)] + np.array([3.5, 0]) + rng.normal(0, 0.06, (24, 2))
        d0 = VGroup(*[Dot([p[0], p[1], 0], radius=0.06, color=MUTED) for p in x0])
        lines = VGroup(*[DashedLine([a[0], a[1], 0], [b[0], b[1], 0], color=TEAL, stroke_width=1.2, stroke_opacity=0.6) for a, b in zip(x0, x1)])
        l0 = MathTex(r"z_0 \sim \mathcal{N}(0,I)", color=MUTED).move_to(LEFT * 4 + DOWN * 2)
        l1 = MathTex(r"z_1 \sim p_{\text{data}}", color=GOLD).move_to(RIGHT * 3.5 + DOWN * 2)
        self.play(FadeIn(d0), Write(l0), Write(l1))
        self.play(Create(lines), run_time=1.5)
        eq = MathTex(r"z_t = (1-t)z_0 + t z_1,\qquad v_\theta(z_t,t) \approx z_1 - z_0", font_size=36).to_edge(UP, buff=1.1)
        self.play(Write(eq))
        self.play(*[d.animate.move_to([b[0], b[1], 0]).set_color(GOLD) for d, b in zip(d0, x1)], run_time=2.5)
        self.say("Une régression d'un champ de vitesse, puis on intègre une EDO.", 3)
        self.clear_all()

        h = self.header("Scaling laws")
        ax = Axes(x_range=[0, 5], y_range=[0, 4], x_length=6.5, y_length=3.8,
                  axis_config={"color": MUTED, "stroke_width": 1.2}, tips=False).shift(UP * 0.3)
        xl = T("log (calcul, paramètres, données)", 20, MUTED).next_to(ax, DOWN)
        yl = T("log (perte)", 20, MUTED).rotate(PI / 2).next_to(ax, LEFT)
        self.play(Create(ax), FadeIn(xl), FadeIn(yl))
        pts = VGroup(*[Dot(ax.c2p(x, 3.5 - 0.6 * x + 0.08 * rng.normal()), color=GOLD) for x in np.linspace(0.4, 4.6, 9)])
        self.play(LaggedStart(*[FadeIn(p, scale=2) for p in pts], lag_ratio=0.15))
        self.play(Create(ax.plot(lambda x: 3.5 - 0.6 * x, x_range=[0.2, 4.8], color=TEAL)))
        self.say("Des relations empiriques (pas des lois universelles)\nqui guident les modèles fondation génératifs.", 4)
        self.outro("Semaine suivante : projet final et synthèse")


class S15(Week):
    week = 15
    title = "Projet & synthèse"
    keywords = "Comparer · Expérimenter · Défendre"
    question = "Comment mobiliser les modèles étudiés pour concevoir,\ncomparer et défendre un projet génératif complet ?"

    def construct(self):
        self.intro()
        h = self.header("La carte du cours")
        nodes = {
            "Représentations": (-5.2, 2.0, MUTED), "Auto-régressifs": (-5.2, 0.5, BLUE),
            "AE": (-2.6, 2.0, BLUE), "VAE": (-2.6, 0.5, TEAL), "Flows": (-2.6, -1.0, TEAL),
            "EBM": (0.2, 2.0, ORANGE), "GAN": (0.2, 0.5, ORANGE), "Score": (0.2, -1.0, GOLD),
            "Diffusion": (2.9, 0.5, GOLD), "Hiérarchiques": (2.9, 2.0, ROSE),
            "LDM": (5.3, 1.3, ROSE), "Flow Matching": (5.3, -0.4, ROSE),
        }
        mobs = {}
        for name, (x, y, c) in nodes.items():
            t = T(name, 20, c, weight=BOLD)
            r = RoundedRectangle(width=t.width + 0.4, height=0.6, corner_radius=0.15, color=c, fill_color=BG, fill_opacity=1)
            mobs[name] = VGroup(r, t).move_to([x, y, 0])
        edges = [("Représentations", "AE"), ("AE", "VAE"), ("Représentations", "Auto-régressifs"), ("VAE", "Flows"),
                 ("EBM", "Score"), ("EBM", "GAN"), ("Score", "Diffusion"), ("Diffusion", "LDM"), ("VAE", "LDM"),
                 ("Diffusion", "Flow Matching"), ("Flows", "Flow Matching"), ("Hiérarchiques", "LDM")]
        order = list(nodes.keys())
        self.play(LaggedStart(*[FadeIn(mobs[n], scale=0.8) for n in order], lag_ratio=0.15), run_time=3)
        ar = VGroup(*[Line(mobs[a].get_center(), mobs[b].get_center(), color=MUTED, stroke_width=1.5, stroke_opacity=0.6) for a, b in edges])
        ar.set_z_index(-1)
        self.play(Create(ar), run_time=2)
        self.say("Quinze semaines, une seule question : quels compromis entre\nqualité, diversité, vitesse, vraisemblance et stabilité ?", 4)
        self.clear_all()

        h = self.header("Votre projet final")
        steps = VGroup(*[
            VGroup(Circle(0.32, color=c, fill_opacity=0.3), T(str(i + 1), 24, FG, weight=BOLD)).arrange(ORIGIN)
            for i, c in enumerate([BLUE, TEAL, GOLD, ORANGE, ROSE])
        ]).arrange(RIGHT, buff=1.6).shift(UP * 0.6)
        labels = ["Question", "Protocole", "Modèles", "Évaluation", "Analyse critique"]
        tl = VGroup(*[T(l, 22, FG).next_to(s, DOWN, buff=0.3) for l, s in zip(labels, steps)])
        conn = VGroup(*[Line(steps[i].get_right(), steps[i + 1].get_left(), color=MUTED) for i in range(4)])
        self.play(LaggedStart(*[AnimationGroup(FadeIn(s, scale=0.6), FadeIn(t)) for s, t in zip(steps, tl)], lag_ratio=0.3), Create(conn), run_time=3)
        self.say("Un échec bien diagnostiqué vaut mieux qu'un grand modèle mal analysé.", 3.5, GOLD)
        self.outro("Consultez la page « Projet final » pour les consignes")
