from common import *


class S06(Week):
    week = 6
    title = "Autoencodeurs profonds"
    keywords = "Encodeur · Latent · Reconstruction · Manifold"
    question = "Comment apprendre une représentation compacte z\nqui conserve l'information essentielle de x ?"

    def construct(self):
        self.intro()
        h = self.header("x  →  encodeur  →  z  →  décodeur  →  x̂")
        enc = Polygon([-3.6, 1.4, 0], [-1.4, 0.5, 0], [-1.4, -0.5, 0], [-3.6, -1.4, 0], color=BLUE, fill_opacity=0.25)
        dec = Polygon([1.4, 0.5, 0], [3.6, 1.4, 0], [3.6, -1.4, 0], [1.4, -0.5, 0], color=TEAL, fill_opacity=0.25)
        z = Rectangle(width=0.5, height=1.0, color=GOLD, fill_opacity=0.5)
        x = Square(1.6, color=FG).move_to(LEFT * 5.5)
        xh = Square(1.6, color=FG).move_to(RIGHT * 5.5)
        lbl = VGroup(MathTex("x").next_to(x, DOWN), T("encodeur", 22, BLUE).next_to(enc, DOWN),
                     MathTex("z", color=GOLD).next_to(z, DOWN), T("décodeur", 22, TEAL).next_to(dec, DOWN),
                     MathTex(r"\hat{x}").next_to(xh, DOWN))
        digit = MathTex("7", font_size=110).move_to(x)
        digit2 = MathTex("7", font_size=110, color=MUTED).move_to(xh)
        self.play(FadeIn(x), Write(digit), FadeIn(enc), FadeIn(z), FadeIn(dec), FadeIn(xh), FadeIn(lbl))
        self.play(Indicate(z, color=GOLD))
        self.play(TransformFromCopy(digit, digit2), run_time=1.5)
        self.say("Le goulot d'étranglement force z à ne garder que l'essentiel.", 3)
        loss = MathTex(r"\mathcal{L} = \| x - \hat{x} \|^2", color=TEAL).shift(UP * 2.3)
        self.play(Write(loss))
        self.wait(1.5)
        self.clear_all()

        h = self.header("L'espace latent appris")
        rng = np.random.default_rng(6)
        ax = Axes(x_range=[-3, 3], y_range=[-2, 2], x_length=7, y_length=4.4,
                  axis_config={"color": MUTED, "stroke_width": 1.2}).shift(UP * 0.2)
        self.play(Create(ax))
        cl = VGroup()
        for c, col in [((-2, 1.2), BLUE), ((-0.4, 1.4), TEAL), ((1.8, 0.8), ORANGE), ((-1.5, -1.2), GOLD), ((1.2, -1.3), ROSE)]:
            g, _ = gauss_cloud(ax.c2p(*c), 18, 0.18, rng, col)
            cl.add(g)
        self.play(LaggedStart(*[FadeIn(g) for g in cl], lag_ratio=0.2), run_time=2)
        self.say("Les codes des données forment des îlots séparés.", 2.5)
        zr = Dot(ax.c2p(0.3, -0.1), color=FG, radius=0.12)
        ring = Circle(0.35, color=ROSE).move_to(zr)
        out = VGroup(Square(1.2, color=ROSE), T("?", 60, ROSE, weight=BOLD)).arrange(ORIGIN).next_to(ax, RIGHT, buff=0.3)
        arr = Arrow(zr.get_right(), out.get_left(), color=ROSE, buff=0.2)
        self.play(FadeIn(zr, scale=2), Create(ring))
        self.play(GrowArrow(arr), FadeIn(out))
        self.say("Un z tiré au hasard tombe entre les îlots :\nle décodeur produit n'importe quoi.", 3.5)
        self.say("Bonne reconstruction ≠ bon générateur → motivation du VAE.", 3, GOLD)
        self.outro("Semaine suivante : autoencodeurs variationnels (VAE)")


class S07(Week):
    week = 7
    title = "Autoencodeurs variationnels"
    keywords = "ELBO · KL · Reparametrization · β-VAE · CVAE"
    question = "Comment structurer l'espace latent pour générer\nde nouvelles données de manière cohérente ?"

    def construct(self):
        self.intro()
        h = self.header("Chaque x devient une distribution qφ(z | x)")
        ax = Axes(x_range=[-3, 3], y_range=[-2, 2], x_length=7, y_length=4.4,
                  axis_config={"color": MUTED, "stroke_width": 1.2}).shift(UP * 0.2)
        self.play(Create(ax))
        centers = [(-2, 1.2), (-0.4, 1.4), (1.8, 0.8), (-1.5, -1.2), (1.2, -1.3)]
        cols = [BLUE, TEAL, ORANGE, GOLD, ROSE]
        dots = VGroup(*[Dot(ax.c2p(*c), color=col) for c, col in zip(centers, cols)])
        self.play(FadeIn(dots))
        self.say("Un AE donne un point. Un VAE donne une gaussienne (μ, σ).", 0)
        blobs = VGroup(*[Ellipse(width=0.6, height=0.6, color=col, fill_opacity=0.25).move_to(d) for d, col in zip(dots, cols)])
        self.play(*[GrowFromCenter(b) for b in blobs], run_time=1.2)
        self.wait(1.5)
        prior = Circle(radius=1.7, color=FG, stroke_width=2).move_to(ax.c2p(0, 0))
        pl = MathTex(r"p(z)=\mathcal{N}(0,I)", font_size=32).next_to(prior, RIGHT, buff=0.1).shift(UP * 1.2)
        self.play(Create(prior), Write(pl))
        self.say("La KL rapproche ces gaussiennes de la prior N(0, I) :\nelles se recouvrent et comblent les trous.", 0)
        new_c = [(-0.8, 0.5), (-0.1, 0.7), (0.7, 0.4), (-0.6, -0.5), (0.5, -0.6)]
        self.play(*[b.animate.move_to(ax.c2p(*c)).scale(2.2) for b, c in zip(blobs, new_c)],
                  *[d.animate.move_to(ax.c2p(*c)) for d, c in zip(dots, new_c)], run_time=2.5)
        self.wait(1.5)
        self.say("Tout z ∼ N(0, I) se décode maintenant en une donnée plausible.", 3, GOLD)
        self.clear_all()

        h = self.header("L'objectif : la ELBO")
        elbo = MathTex(r"\mathrm{ELBO}", r"=", r"\mathbb{E}_{q_\phi(z|x)}[\log p_\theta(x|z)]", r"-", r"\mathrm{KL}(q_\phi(z|x)\,\|\,p(z))").shift(UP * 1.2)
        elbo[2].set_color(TEAL)
        elbo[4].set_color(ORANGE)
        self.play(Write(elbo), run_time=2)
        b1 = Brace(elbo[2], DOWN, color=TEAL)
        b2 = Brace(elbo[4], DOWN, color=ORANGE)
        t1 = T("reconstruction", 24, TEAL).next_to(b1, DOWN)
        t2 = T("régularisation du latent", 24, ORANGE).next_to(b2, DOWN)
        self.play(GrowFromCenter(b1), FadeIn(t1))
        self.play(GrowFromCenter(b2), FadeIn(t2))
        self.say("Une borne inférieure calculable de log pθ(x).", 2.5)
        rep = MathTex(r"z = \mu_\phi(x) + \sigma_\phi(x)\odot\varepsilon,\quad \varepsilon\sim\mathcal{N}(0,I)", color=GOLD).shift(DOWN * 1.8)
        self.play(Write(rep))
        self.say("Astuce de reparamétrisation : le hasard passe dans ε,\nle gradient traverse l'échantillonnage.", 3.5)
        self.outro("Semaine suivante : flots normalisants")


class S08(Week):
    week = 8
    title = "Flots normalisants"
    keywords = "Changement de variables · Jacobien · RealNVP · Glow"
    question = "Comment transformer une distribution simple en une\ndistribution complexe en gardant une vraisemblance exacte ?"

    def construct(self):
        self.intro()
        h = self.header("Déformer l'espace par une bijection f")
        plane = NumberPlane(x_range=[-3, 3], y_range=[-2, 2], x_length=6.6, y_length=4.4,
                            background_line_style={"stroke_color": BLUE, "stroke_opacity": 0.5, "stroke_width": 1.5}).shift(DOWN * 0.2)
        plane.prepare_for_nonlinear_transform()
        rng = np.random.default_rng(8)
        pts = rng.normal(0, 0.55, size=(80, 2))
        dots = VGroup(*[Dot(plane.c2p(*p), radius=0.05, color=GOLD) for p in pts])
        zl = MathTex(r"z \sim \mathcal{N}(0, I)", color=GOLD).to_corner(UL).shift(DOWN * 0.8)
        self.play(Create(plane), FadeIn(dots), Write(zl), run_time=1.5)
        self.say("On part d'une loi simple…", 1.5)

        def f(p):
            x, y = p[0], p[1] + 0.2
            return np.array([x + 0.5 * np.sin(1.3 * y), y + 0.16 * x ** 2 - 0.5, 0])

        xl = MathTex(r"x = f(z)", color=TEAL).to_corner(UR).shift(DOWN * 0.8)
        self.play(plane.animate.apply_function(f), dots.animate.apply_function(f), Write(xl), run_time=3)
        self.say("…qu'on déforme par une transformation inversible.\nLes volumes changent : le Jacobien les mesure.", 3.5)
        self.clear_all()

        h = self.header("Formule du changement de variables")
        eq = MathTex(r"\log p_X(x)", r"=", r"\log p_Z\!\left(f^{-1}(x)\right)", r"+", r"\log\left|\det \frac{\partial f^{-1}}{\partial x}\right|").shift(UP * 1.3)
        eq[2].set_color(GOLD)
        eq[4].set_color(TEAL)
        self.play(Write(eq), run_time=2.5)
        self.say("Vraisemblance exacte… si le déterminant est facile à calculer.", 2.5)
        # Jacobien triangulaire
        m = Matrix([["a", "0", "0"], ["*", "b", "0"], ["*", "*", "c"]], element_to_mobject_config={"color": FG}).shift(DOWN * 1.3 + LEFT * 2)
        for i in range(3):
            m.get_entries()[i * 3 + i].set_color(GOLD)
        det = MathTex(r"\det = a\,b\,c", color=GOLD).next_to(m, RIGHT, buff=1)
        self.play(FadeIn(m), Write(det))
        self.say("RealNVP : couches de couplage → Jacobien triangulaire,\nle déterminant est le produit de la diagonale.", 4)
        self.outro("Semaine suivante : modèles fondés sur l'énergie")


class S09(Week):
    week = 9
    title = "Modèles fondés sur l'énergie"
    keywords = "Énergie · Fonction de partition · Langevin · CD · RBM"
    question = "Comment apprendre une distribution à partir d'une énergie\nlorsque sa normalisation est difficile ?"

    def construct(self):
        self.intro()
        h = self.header("Énergie faible  ⇒  configuration plausible")
        ax = Axes(x_range=[-4, 4], y_range=[-0.5, 3], x_length=8, y_length=3.4,
                  axis_config={"color": MUTED, "stroke_width": 1.2}).shift(DOWN * 0.5 + LEFT * 1.6)

        def E(x):
            return 2.4 - 1.6 * np.exp(-(x + 1.8) ** 2 / 0.6) - 2.2 * np.exp(-(x - 1.5) ** 2 / 0.5) + 0.04 * x ** 2

        curve = ax.plot(E, x_range=[-4, 4], color=ORANGE, stroke_width=4)
        el = MathTex(r"E_\theta(x)", color=ORANGE).next_to(curve, UP).shift(LEFT * 3.5)
        self.play(Create(ax), Create(curve), Write(el), run_time=1.8)
        eq = MathTex(r"p_\theta(x) = \frac{e^{-E_\theta(x)}}{Z(\theta)}").move_to(RIGHT * 4.9 + UP * 0.6)
        self.play(Write(eq))
        self.say("Z(θ) somme sur toutes les configurations :\nintractable en haute dimension.", 3)

        # Langevin
        self.say("Échantillonner : dynamique de Langevin\n(descendre l'énergie + un peu de bruit).", 0)
        rng = np.random.default_rng(9)
        xs = [-3.5, -0.2, 3.6]
        balls = VGroup(*[Dot(ax.c2p(x, E(x)), color=GOLD, radius=0.1) for x in xs])
        self.play(FadeIn(balls))
        eta = 0.06
        for step in range(40):
            new = []
            for k, x in enumerate(xs):
                g = (E(x + 1e-3) - E(x - 1e-3)) / 2e-3
                x = x - eta * 1.2 * g + np.sqrt(2 * eta) * 0.12 * rng.normal()
                xs[k] = float(np.clip(x, -3.9, 3.9))
            self.play(*[b.animate.move_to(ax.c2p(x, E(x))) for b, x in zip(balls, xs)], run_time=0.12, rate_func=linear)
        self.wait(1)
        self.say("Les particules se rassemblent dans les vallées :\nce sont les échantillons du modèle.", 3)
        self.clear_all()

        h = self.header("Apprendre : deux forces opposées")
        g = MathTex(r"\nabla_\theta \log p_\theta(x)", r"=", r"-\nabla_\theta E_\theta(x)", r"+", r"\mathbb{E}_{x'\sim p_\theta}\left[\nabla_\theta E_\theta(x')\right]").shift(UP * 0.8)
        g[2].set_color(TEAL)
        g[4].set_color(ORANGE)
        self.play(Write(g), run_time=2.5)
        t1 = T("phase positive : baisser l'énergie des données", 24, TEAL)
        t2 = T("phase négative : remonter celle des échantillons du modèle", 24, ORANGE)
        VGroup(t1, t2).arrange(DOWN, buff=0.3).next_to(g, DOWN, buff=0.7)
        self.play(FadeIn(t1, shift=UP * 0.2))
        self.play(FadeIn(t2, shift=UP * 0.2))
        self.say("La divergence contrastive (RBM) raccourcit l'échantillonnage MCMC.", 3.5)
        self.outro("Semaine suivante : modèles implicites et GAN")


class S10(Week):
    week = 10
    title = "Modèles génératifs implicites"
    keywords = "GAN · MMD-GAN · absence de vraisemblance · évaluation"
    question = "Peut-on apprendre à générer des données réalistes\nsans jamais calculer leur vraisemblance ?"

    def construct(self):
        self.intro()
        h = self.header("Un jeu à deux joueurs")
        G = RoundedRectangle(width=2.4, height=1.2, corner_radius=0.2, color=TEAL, fill_opacity=0.25)
        D = RoundedRectangle(width=2.6, height=1.2, corner_radius=0.2, color=ORANGE, fill_opacity=0.25)
        gt = T("Générateur G", 22, TEAL).move_to(G)
        dt = T("Discriminateur D", 22, ORANGE).move_to(D)
        z = MathTex(r"z\sim\mathcal{N}(0,I)").move_to(LEFT * 5.3 + UP * 0.8)
        Gg = VGroup(G, gt).move_to(LEFT * 2 + UP * 0.8)
        Dg = VGroup(D, dt).move_to(RIGHT * 2.6)
        real = T("données réelles", 22, BLUE).move_to(LEFT * 2 + DOWN * 1.0)
        out = T("réel ou faux ?", 24, GOLD).next_to(Dg, RIGHT, buff=0.4)
        a1 = Arrow(z.get_right(), Gg.get_left(), color=MUTED)
        a2 = Arrow(Gg.get_right(), Dg.get_left(), color=TEAL)
        a3 = Arrow(real.get_right(), Dg.get_left(), color=BLUE)
        self.play(Write(z), GrowArrow(a1), FadeIn(Gg))
        self.play(FadeIn(real), FadeIn(Dg), GrowArrow(a2), GrowArrow(a3))
        self.play(FadeIn(out))
        mm = MathTex(r"\min_G \max_D\; \mathbb{E}_{x}[\log D(x)] + \mathbb{E}_{z}[\log(1-D(G(z)))]", font_size=36).shift(DOWN * 2.3)
        self.play(Write(mm))
        self.say("G apprend à tromper D ; D apprend à démasquer G.", 3)
        self.clear_all()

        h = self.header("Les faux échantillons migrent vers les vrais")
        rng = np.random.default_rng(10)
        ang = np.linspace(0, 2 * np.pi, 8, endpoint=False)
        centers = [(2.2 * np.cos(a), 2.2 * np.sin(a) * 0.85) for a in ang]
        real = VGroup()
        for c in centers:
            g, _ = gauss_cloud(np.array(c) + np.array([0, -0.2]), 12, 0.12, rng, BLUE, radius=0.05)
            real.add(g)
        self.play(FadeIn(real))
        fake_pts = rng.normal(0, 0.4, size=(48, 2)) + np.array([0, -0.2])
        fake = VGroup(*[Dot([p[0], p[1], 0], radius=0.06, color=TEAL) for p in fake_pts])
        self.play(FadeIn(fake))
        tgt = [np.array(centers[k % 8]) + rng.normal(0, 0.12, 2) + np.array([0, -0.2]) for k in range(48)]
        self.play(*[d.animate.move_to([t[0], t[1], 0]) for d, t in zip(fake, tgt)], run_time=2.5)
        self.say("Idéal : les 8 modes sont couverts.", 2)
        tgt2 = [np.array(centers[k % 2]) + rng.normal(0, 0.12, 2) + np.array([0, -0.2]) for k in range(48)]
        self.play(*[d.animate.move_to([t[0], t[1], 0]).set_color(ROSE) for d, t in zip(fake, tgt2)], run_time=2.5)
        self.say("Mode collapse : des échantillons nets… mais seulement 2 modes.\nD'où l'importance de bien évaluer (FID, précision/rappel).", 4, GOLD)
        self.outro("Semaine suivante : score matching")
