from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

tiny = 12
small = 24
normal = 48
large = 96

class Recall(VoiceoverScene):
    def clear(self, d):
        self.play(
            *[FadeOut(mob) for mob in self.mobjects], run_time=d
            # All mobjects in the screen are saved in self.mobjects
        )

    def construct(self):
        self.interactive_embed()
        self.set_speech_service(GTTSService(lang="en", tld="com.hk"))
        preamble = TexTemplate()
        preamble.add_to_preamble(r"""
            \usepackage{ragged2e}
        """)

        with self.voiceover(text="I want to talk a little bit about this thing called the function field analogy.") as tracker:
            self.play(Create(Text("Function Field Analogy", color=ORANGE).to_corner(corner=LEFT+UP)),
                      FadeIn(Tex(r"\justify{Geer, G. van der, Moonen, B., \& Schoof, R. (Eds.). (2005). Number fields and function fields: Two parallel worlds.}", font_size=1.5*small, tex_template=preamble).scale(0.75)),
                      run_time=tracker.duration/4.)
            self.wait(tracker.duration/2.)
            self.clear(tracker.duration/4.)
        with self.voiceover(text="But first, let's start by recalling some algebraic number theory. Here are some of the fields one encounter often in arithmetics.") as tracker:
            self.play(FadeIn(Tex(r"\justify{Neukirch, J. (2013). Algebraic number theory (Vol. 322). Springer Science \& Business Media.}", font_size=1.5*small, tex_template=preamble).scale(0.75)), run_time=tracker.duration/4.)
            self.wait(tracker.duration/2.)
            self.clear(tracker.duration/4.)

        r = MathTex(r"\mathbb{R}", font_size=normal)
        c = MathTex(r"\mathbb{C}", font_size=normal)
        Group(r, c)
        q = MathTex(r"K/\mathbb{Q}", font_size=normal)
        qpx = MathTex(r"K/\mathbb{Q}_p", font_size=normal)
        fpx = MathTex(r"K/\mathbb{F}_p(X)", font_size=normal)
        fplx = MathTex(r"\mathbb{F}_p((X))", font_size=normal)
        gg = VGroup(
            r, c, qpx, fplx, fpx, q
        ).arrange(RIGHT, buff=1)
        with self.voiceover(text="the real numbers,") as tracker:
            self.play(FadeIn(r), run_time=tracker.duration)
        with self.voiceover(text="the complex numbers,") as tracker:
            self.play(FadeIn(c), run_time=tracker.duration)
        with self.voiceover(text="the algebraic extensions of p-adic numbers") as tracker:
            self.play(FadeIn(qpx), run_time=tracker.duration)
        with self.voiceover(text="the fields of Laurent series over finite fields,") as tracker:
            self.play(FadeIn(fplx), run_time=tracker.duration)
        with self.voiceover(text="the function fields for a curve over finite fields") as tracker:
            self.play(FadeIn(fpx), run_time=tracker.duration)
        with self.voiceover(text="and the most classic of them all, the algebraic number fields") as tracker:
            self.play(FadeIn(q), run_time=tracker.duration)

        with self.voiceover(text="Based on observed properties of these fields and appropriate analogies that will be discussed later, one classifies them into these categories:") as tracker:
            for anim in [mob.animate.to_edge(DOWN) for mob in gg.submobjects]:
                self.play(anim, run_time=tracker.duration/6.)
        with self.voiceover(text="These are the global fields.") as tracker:
            self.play(Circumscribe(Group(fpx, q)), run_time=tracker.duration)
        
        with self.voiceover(text="One observes that there are multiple valuations, or places, that can be associated to these, one for each prime ideal in their respective rings of integers.") as tracker:
            eg = Group(
                qv := MathTex(r"\mathbb{Q}\leadsto v_{\mathfrak{p}}\text{ for }\mathfrak{p}\in\mathbb{Z}"),
                fpv := MathTex(r"\mathbb{F}_p(X)\leadsto v_{\mathfrak{p}}\text{ for }\mathfrak{p}\in\mathbb{F}_p[X]")
            ).arrange(DOWN, buff=.5).to_edge(UP)
            self.play(FadeIn(qv), run_time=tracker.duration/2.)
            self.play(FadeIn(fpv), run_time=tracker.duration/2.)
        p1 = [-3, 1, 0] 
        p1b=  p1 + 3 * RIGHT
        p2 = [3, -1, 0] 
        p2b = p2 + 3 * LEFT 
        c = [0, 0, 0]
        curve = CubicBezier(p1, p1b, p2b, p2, color=ORANGE)
        p = Circle(.1, RED, fill_opacity=1, stroke_color=RED).shift(c)
        text = MathTex(r"\text{prime ideal associated to closed point }P\leadsto v_P", font_size=small)
        text.next_to(curve, direction=DOWN)
        arr = Arrow(start=text.get_center() + .1*UP, end=c + .1*DOWN, color=GOLD)
        with self.voiceover(text="For example, for this function field, such prime ideals corresponds to closed points") as tracker:
            self.play(FadeOut(qv), Flash(fpv), run_time=tracker.duration/7.)
            self.play(Create(curve), Transform(fpv, fpv_ := MathTex(r"\left(K:=\mathbb{F}_p(X,Y)/P(X,Y)\right)/\mathbb{F}_p(X)\leadsto v_{\mathfrak{p}}\text{ for }\mathfrak{p}\in\mathbb{F}_p[X]").to_edge(UP)), run_time=2*tracker.duration/7.)
            self.play(FadeIn(p), run_time=2*tracker.duration/7.)
            self.play(Create(arr), FadeIn(text), run_time=2*tracker.duration/7.)

        with self.voiceover(text="Plus one special \"place-at-infinity\", which, under chosen isomorphism to an algebraic extension of the standard function field, corresponds to the prime ideal one over X.") as tracker:
            self.wait_for_voiceover() # TODO

        with self.voiceover(text="Let's go back and compare this picture to that of the algebraic number fields.") as tracker:
            self.wait_for_voiceover() # TODO

        # TODO completion at places of the global fields leads to local fields
        # TODO local rings, arithmetic schemes
        #

class Zeta():
    def construct(self):
        pass
        # TODO
        # zeta = MathTex(r"\zeta(K, s) := \prod_{\mathfrak{p}} \frac{1}{1-N \mathfrak{p}^{-s}}", font_size=normal)
        # with self.voiceover(text="Recall that zeta functions reveal important arithmetic information on global fields.") as tracker:
        #     self.play(Create(zeta), run_time=tracker.duration)
