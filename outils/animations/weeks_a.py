from common import *


class S01(Week):
    week = 1
    title = "Rappels NN & Représentations"
    keywords = "CNN · RNN · Attention & Transformers"
    question = "Comment représenter les données de manière utile\navec un réseau de neurones ?"

    def construct(self):
        self.intro()
        h = self.header("x  →  z  →  ŷ : le réseau fabrique une représentation")
        # Image d'entrée (grille de pixels)
        rng = np.random.default_rng(1)
        grid = VGroup(*[Square(0.22, stroke_width=0.5, stroke_color=MUTED,
                               fill_color=interpolate_color(ManimColor(BG), ManimColor(FG), rng.random()),
                               fill_opacity=1) for _ in range(36)]).arrange_in_grid(6, 6, buff=0)
        grid.move_to(LEFT * 5 + UP * 0.4)
        xl = MathTex("x").next_to(grid, DOWN)
        # Couches
        layers = VGroup()
        for k, n in enumerate([5, 4, 2]):
            col = VGroup(*[Circle(0.16, color=BLUE if k < 2 else GOLD, fill_opacity=0.35) for _ in range(n)])
            col.arrange(DOWN, buff=0.18)
            layers.add(col)
        layers.arrange(RIGHT, buff=1.1).move_to(LEFT * 0.8 + UP * 0.4)
        zl = MathTex("z", color=GOLD).next_to(layers[2], DOWN, buff=0.4)
        edges = VGroup()
        for a, b in zip(layers[:-1], layers[1:]):
            for u in a:
                for v in b:
                    edges.add(Line(u.get_right(), v.get_left(), stroke_width=0.8, color=MUTED, stroke_opacity=0.5))
        out = MathTex(r"\hat{y} = \text{chat}", color=TEAL).next_to(layers, RIGHT, buff=0.8)
        arr = Arrow(grid.get_right(), layers[0].get_left(), buff=0.2, color=MUTED)
        self.play(FadeIn(grid), Write(xl))
        self.play(GrowArrow(arr), LaggedStart(*[FadeIn(c) for c in layers], lag_ratio=0.3), Create(edges), run_time=1.6)
        self.play(Write(zl), Indicate(layers[2], color=GOLD))
        self.play(Write(out))
        self.say("Un réseau ne fait pas que prédire ŷ :\nil construit une représentation interne z (l'espace latent).", 3)
        self.say("CNN, RNN et Transformers diffèrent surtout\npar la manière de construire z.", 3)
        self.play(FadeOut(VGroup(grid, xl, layers, zl, edges, out, arr)))

        # Espace latent : nuage de points structuré
        ax = Axes(x_range=[-3, 3], y_range=[-2.2, 2.2], x_length=6.5, y_length=4.4,
                  axis_config={"color": MUTED, "stroke_width": 1.5}).shift(UP * 0.3)
        lab = T("espace latent z", 22, MUTED).next_to(ax, UP, buff=0.1).align_to(ax, RIGHT)
        self.play(Create(ax), FadeIn(lab))
        clouds = VGroup()
        for c, col, name in [((-1.6, 0.9), BLUE, "chats"), ((1.5, 1.0), TEAL, "chiens"), ((0.0, -1.2), ORANGE, "voitures")]:
            g, _ = gauss_cloud(ax.c2p(*c), 22, 0.28, rng, col)
            nm = T(name, 20, col).next_to(g, RIGHT, buff=0.1)
            clouds.add(VGroup(g, nm))
        self.play(LaggedStart(*[FadeIn(c) for c in clouds], lag_ratio=0.4), run_time=2)
        self.say("Un embedding est une géométrie apprise :\nles exemples semblables deviennent voisins.", 3)

        # Reconstruire ≠ générer
        z = Dot(ax.c2p(2.3, -1.6), color=ROSE, radius=0.1)
        q = T("?", 40, ROSE, weight=BOLD).next_to(z, UP, buff=0.1)
        self.say("Mais prendre un z au hasard tombe souvent\ndans une zone vide…", 0)
        self.play(FadeIn(z, scale=2), Write(q))
        self.wait(2.2)
        self.say("Reconstruire ≠ générer : c'est le fil rouge de tout le cours.", 3, GOLD)
        self.outro("Semaine suivante : discriminatif vs génératif")


class S02(Week):
    week = 2
    title = "Discriminatif vs Génératif"
    keywords = "p(y|x) · p(x) · explicite · implicite"
    question = "Quelle distribution veut-on modéliser :\np(y | x), p(x) ou p(x, y) ?"

    def construct(self):
        self.intro()
        rng = np.random.default_rng(2)
        ax = Axes(x_range=[-4, 4], y_range=[-3, 3], x_length=7, y_length=5,
                  axis_config={"color": MUTED, "stroke_width": 1.2}).shift(UP * 0.4)
        a, pa = gauss_cloud(ax.c2p(-1.5, 0.6), 30, 0.45, rng, BLUE)
        b, pb = gauss_cloud(ax.c2p(1.4, -0.5), 30, 0.45, rng, ORANGE)
        self.play(Create(ax), FadeIn(a), FadeIn(b))
        self.say("Mêmes données, deux questions différentes.", 2)

        # Discriminatif : frontière
        h = self.header("Discriminatif : modéliser p(y | x)")
        line = Line(ax.c2p(-1.2, -3), ax.c2p(1.0, 3), color=GOLD, stroke_width=4)
        self.play(Create(line))
        self.say("On apprend seulement à décider :\nde quel côté de la frontière se trouve x ?", 3)
        self.play(FadeOut(line), FadeOut(h))

        # Génératif : densités
        h = self.header("Génératif : modéliser p(x) ou p(x, y)")
        self.say("On décrit toute la distribution des données…", 0)
        ells = VGroup()
        for c, col in [((-1.5, 0.6), BLUE), ((1.4, -0.5), ORANGE)]:
            for r in [0.5, 0.9, 1.3]:
                ells.add(Ellipse(width=r * 1.6, height=r * 1.6, color=col, stroke_width=2,
                                 stroke_opacity=1.2 - r * 0.6).move_to(ax.c2p(*c)))
        self.play(LaggedStart(*[Create(e) for e in ells], lag_ratio=0.15), run_time=2)
        self.wait(1)
        new, _ = gauss_cloud(ax.c2p(-1.5, 0.6), 8, 0.4, rng, GOLD, radius=0.08)
        new2, _ = gauss_cloud(ax.c2p(1.4, -0.5), 8, 0.4, rng, GOLD, radius=0.08)
        self.play(LaggedStart(*[FadeIn(d, scale=3) for d in [*new, *new2]], lag_ratio=0.08), run_time=2)
        self.say("…ce qui permet d'échantillonner de nouveaux x.", 2.5, GOLD)
        self.clear_all()

        # Explicite vs implicite
        h = self.header("Deux façons de générer")
        left = VGroup(T("Explicite", 34, TEAL, weight=BOLD), MathTex(r"p_\theta(x)\ \text{calculable}"),
                      T("autorégressifs · flows · VAE", 22, MUTED)).arrange(DOWN, buff=0.35)
        right = VGroup(T("Implicite", 34, ORANGE, weight=BOLD), MathTex(r"z \;\rightarrow\; G_\theta(z) \;\rightarrow\; x"),
                       T("GAN : échantillonner sans densité", 22, MUTED)).arrange(DOWN, buff=0.35)
        VGroup(left, right).arrange(RIGHT, buff=2).shift(UP * 0.3)
        sep = DashedLine(UP * 2, DOWN * 1.5, color=MUTED)
        self.play(FadeIn(left, shift=RIGHT * 0.3), Create(sep), FadeIn(right, shift=LEFT * 0.3), run_time=1.5)
        self.say("Cette taxonomie organisera toutes les familles\nque nous étudierons (AR, VAE, flows, GAN, diffusion).", 4)
        self.outro("Semaine suivante : maximum de vraisemblance")


class S03(Week):
    week = 3
    title = "Maximum de vraisemblance"
    keywords = "Vraisemblance · NLL · Règle de la chaîne · MLE"
    question = "Comment apprendre une distribution pθ(x)\nà partir des données observées ?"

    def construct(self):
        self.intro()
        h = self.header("Observer, puis ajuster θ")
        obs = [1, 1, 0, 1, 0, 1, 1, 1, 0, 1]
        coins = VGroup(*[VGroup(Circle(0.28, color=TEAL if o else ORANGE, fill_opacity=0.35),
                                T(str(o), 24, FG, weight=BOLD)) for o in obs]).arrange(RIGHT, buff=0.18)
        coins.shift(UP * 2.5)
        self.play(LaggedStart(*[FadeIn(c, shift=DOWN * 0.3) for c in coins], lag_ratio=0.1), run_time=1.6)
        lik = MathTex(r"L(\theta) = \theta^{7}(1-\theta)^{3}").next_to(coins, DOWN, buff=0.4)
        self.play(Write(lik))
        ax = Axes(x_range=[0, 1, 0.1], y_range=[0, 0.0025, 0.0005], x_length=7, y_length=2.6,
                  axis_config={"color": MUTED, "stroke_width": 1.2},
                  x_axis_config={"numbers_to_include": [0, 0.5, 1]}).shift(DOWN * 0.7)
        xl = MathTex(r"\theta").next_to(ax.x_axis, RIGHT)
        curve = ax.plot(lambda t: t ** 7 * (1 - t) ** 3, x_range=[0, 1], color=GOLD, stroke_width=4)
        self.play(Create(ax), Write(xl))
        tr = ValueTracker(0.2)
        dot = always_redraw(lambda: Dot(ax.c2p(tr.get_value(), tr.get_value() ** 7 * (1 - tr.get_value()) ** 3), color=ROSE, radius=0.09))
        self.play(Create(curve), FadeIn(dot), run_time=1.5)
        self.say("La vraisemblance mesure à quel point θ explique les données.", 0)
        self.play(tr.animate.set_value(0.7), run_time=2.5)
        v = DashedLine(ax.c2p(0.7, 0), ax.c2p(0.7, 0.7 ** 7 * 0.3 ** 3), color=ROSE)
        mle = MathTex(r"\hat\theta_{\text{MLE}} = 7/10", color=ROSE).next_to(ax.c2p(0.7, 0.0023), RIGHT)
        self.play(Create(v), Write(mle))
        self.say("Le maximum de vraisemblance choisit le θ le plus compatible\n— ici la fréquence observée 0,7.", 3.5)
        self.clear_all()

        h = self.header("En pratique : minimiser la NLL")
        eq = MathTex(r"\log \prod_i p_\theta(x^{(i)})", r"=", r"\sum_i \log p_\theta(x^{(i)})").shift(UP * 1.2)
        nll = MathTex(r"\mathrm{NLL}(\theta) = -\sum_i \log p_\theta(x^{(i)})", color=TEAL).next_to(eq, DOWN, buff=0.6)
        self.play(Write(eq[0]))
        self.play(Write(eq[1:]))
        self.say("Le log transforme le produit en somme, plus stable à optimiser.", 0)
        self.play(Write(nll))
        self.wait(2.5)
        self.play(FadeOut(eq), FadeOut(nll), FadeOut(h))

        h = self.header("Haute dimension : factoriser p(x)")
        chain = MathTex(r"p(x) =", r"p(x_1)", r"\,p(x_2\mid x_1)", r"\,p(x_3\mid x_1,x_2)", r"\cdots", r"\,p(x_n\mid x_{<n})").shift(UP * 0.5)
        cols = [FG, BLUE, TEAL, GOLD, FG, ORANGE]
        for part, c in zip(chain, cols):
            part.set_color(c)
        self.play(Write(chain[0]))
        self.play(LaggedStart(*[Write(p) for p in chain[1:]], lag_ratio=0.5), run_time=3)
        self.say("La règle de la chaîne est exacte : une loi jointe énorme\ndevient une suite de prédictions conditionnelles.", 4)
        self.outro("Semaine suivante : variables latentes et inférence")


class S04(Week):
    week = 4
    title = "Variables latentes & inférence"
    keywords = "Latents · Posterior · Inférence exacte / approximée · VI"
    question = "Comment inférer une variable latente z non observée\nà partir d'une observation x ?"

    def construct(self):
        self.intro()
        rng = np.random.default_rng(4)
        ax = Axes(x_range=[-5, 5], y_range=[-2.5, 2.5], x_length=8, y_length=4,
                  axis_config={"color": MUTED, "stroke_width": 1.2}).shift(UP * 0.6)
        g1, _ = gauss_cloud(ax.c2p(-2, 0), 40, 0.55, rng, FG)
        g2, _ = gauss_cloud(ax.c2p(2, 0), 40, 0.55, rng, FG)
        self.play(Create(ax), FadeIn(g1), FadeIn(g2))
        self.say("On observe seulement x… mais un facteur caché\na décidé d'où vient chaque point.", 3)
        self.play(g1.animate.set_color(BLUE), g2.animate.set_color(ORANGE), run_time=1.5)
        zlab = VGroup(MathTex("z=0", color=BLUE).next_to(g1, UP), MathTex("z=1", color=ORANGE).next_to(g2, UP))
        self.play(Write(zlab))
        self.say("Ce facteur non observé est la variable latente z.", 2.5)
        mix = MathTex(r"p(x) = \sum_z p(x\mid z)\,p(z)").to_edge(UP, buff=0.3)
        self.play(Write(mix))
        self.wait(1.5)

        # posterior bar for moving point
        tr = ValueTracker(-3.5)

        def post(x):
            a = np.exp(-(x + 2) ** 2 / (2 * 0.55 ** 2 * 4))
            b = np.exp(-(x - 2) ** 2 / (2 * 0.55 ** 2 * 4))
            return a / (a + b)

        probe = always_redraw(lambda: Dot(ax.c2p(tr.get_value(), 0), color=GOLD, radius=0.12))
        bars = always_redraw(lambda: VGroup(
            Rectangle(width=0.5, height=2 * post(tr.get_value()) + 0.01, fill_color=BLUE, fill_opacity=0.9, stroke_width=0),
            Rectangle(width=0.5, height=2 * (1 - post(tr.get_value())) + 0.01, fill_color=ORANGE, fill_opacity=0.9, stroke_width=0),
        ).arrange(RIGHT, buff=0.2, aligned_edge=DOWN).move_to(RIGHT * 5.6 + DOWN * 1.2, aligned_edge=DOWN))
        bl = MathTex(r"p(z\mid x)", font_size=34).move_to(RIGHT * 5.6 + DOWN * 1.6)
        self.play(FadeIn(probe), FadeIn(bars), Write(bl))
        self.say("L'inférence : pour un x donné, quelle est la probabilité de chaque z ?", 0)
        self.play(tr.animate.set_value(3.5), run_time=5, rate_func=linear)
        self.wait(0.5)
        self.clear_all()

        h = self.header("Le problème : le posterior est souvent intractable")
        bayes = MathTex(r"p(z\mid x) = \frac{p(x\mid z)\,p(z)}{", r"\int p(x\mid z)\,p(z)\,dz", r"}").shift(UP * 0.8)
        self.play(Write(bayes))
        self.play(bayes[1].animate.set_color(ORANGE), Circumscribe(bayes[1], color=ORANGE))
        self.say("Avec un réseau profond, cette intégrale est hors de portée.", 3)
        # VI : q approx p
        ax2 = Axes(x_range=[-4, 4], y_range=[0, 0.6], x_length=6, y_length=2.2,
                   axis_config={"color": MUTED, "stroke_width": 1}).shift(DOWN * 1.4)
        p = ax2.plot(lambda t: 0.6 * np.exp(-(t - 0.6) ** 2 / 0.8) + 0.25 * np.exp(-(t + 1.6) ** 2 / 0.5), color=ORANGE)
        mu = ValueTracker(-2.5)
        q = always_redraw(lambda: ax2.plot(lambda t: 0.55 * np.exp(-(t - mu.get_value()) ** 2 / 1.0), color=TEAL))
        lg = VGroup(MathTex(r"p(z\mid x)", color=ORANGE, font_size=32), MathTex(r"q_\phi(z\mid x)", color=TEAL, font_size=32)).arrange(DOWN).next_to(ax2, RIGHT)
        self.play(Create(ax2), Create(p), FadeIn(lg))
        self.add(q)
        self.say("Inférence variationnelle : on approxime p(z|x)\npar une loi simple qφ, ajustée par optimisation.", 0)
        self.play(mu.animate.set_value(0.45), run_time=3)
        self.wait(2)
        self.outro("Semaine suivante : modèles auto-régressifs")


class S05(Week):
    week = 5
    title = "Modèles auto-régressifs"
    keywords = "Règle de la chaîne · NADE / MADE · PixelRNN / PixelCNN"
    question = "Comment modéliser une distribution complexe p(x)\ncomposante par composante ?"

    def construct(self):
        self.intro()
        h = self.header("Générer une image pixel par pixel")
        n = 6
        rng = np.random.default_rng(5)
        # motif : un « 7 » stylisé
        target = np.zeros((n, n))
        target[0, 1:5] = 1
        for i in range(1, 6):
            target[i, 4 - (i - 1) // 2 if 4 - (i - 1) // 2 >= 1 else 1] = 1
        cells = VGroup(*[Square(0.6, stroke_color=MUTED, stroke_width=1, fill_color=BG, fill_opacity=1) for _ in range(n * n)])
        cells.arrange_in_grid(n, n, buff=0.04).shift(LEFT * 2.6 + DOWN * 0.2)
        self.play(FadeIn(cells))
        formula = MathTex(r"p(x) = \prod_{i} p(x_i \mid x_{<i})").next_to(cells, RIGHT, buff=0.9).shift(UP * 1.2)
        self.play(Write(formula))
        self.say("Ordre raster : chaque pixel est tiré conditionnellement\naux pixels déjà générés.", 0)
        cur = SurroundingRectangle(cells[0], color=GOLD, buff=0.02)
        self.play(Create(cur), run_time=0.3)
        for k in range(n * n):
            i, j = divmod(k, n)
            ctx = [cells[m] for m in range(k)]
            anims = [cur.animate.move_to(cells[k])]
            col = FG if target[i, j] else "#22313F"
            anims.append(cells[k].animate.set_fill(col, 1))
            rt = 0.22 if k > 8 else 0.4
            self.play(*anims, run_time=rt)
        self.play(FadeOut(cur))
        self.say("Vraisemblance exacte… mais génération séquentielle (lente).", 3, GOLD)
        self.clear_all()

        h = self.header("PixelCNN : convolution masquée")
        grid = VGroup(*[Square(0.55, stroke_color=MUTED, stroke_width=1) for _ in range(25)]).arrange_in_grid(5, 5, buff=0.03).shift(UP * 0.1)
        for k in range(25):
            if k < 12:
                grid[k].set_fill(TEAL, 0.55)
            elif k == 12:
                grid[k].set_fill(GOLD, 0.9)
            else:
                grid[k].set_fill(BG, 1)
        lab = VGroup(
            VGroup(Square(0.3, fill_color=TEAL, fill_opacity=0.55, stroke_width=0), T("contexte visible (passé)", 22)).arrange(RIGHT),
            VGroup(Square(0.3, fill_color=GOLD, fill_opacity=0.9, stroke_width=0), T("pixel prédit", 22)).arrange(RIGHT),
            VGroup(Square(0.3, fill_color=BG, fill_opacity=1, stroke_color=MUTED, stroke_width=1), T("futur masqué", 22)).arrange(RIGHT),
        ).arrange(DOWN, aligned_edge=LEFT).next_to(grid, RIGHT, buff=0.8)
        self.play(FadeIn(grid), FadeIn(lab))
        self.say("Le masque interdit de regarder le futur :\nl'entraînement est parallèle, la génération reste séquentielle.", 4)
        self.outro("Semaine suivante : autoencodeurs profonds")
