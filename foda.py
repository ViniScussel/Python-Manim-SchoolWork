import manim
from manim import *

class AreaOfCircle(Scene):
    def construct(self):
        intro = Text("A área do circulo é dada por:")
        formula = Tex("$$A = \pi r^2$$")
        circle = Circle(radius=2)
        razao = Text("Mas... Por quê?")
        self.play(Write(intro))
        self.play(intro.animate().to_edge(UP, buff=0.5).set_run_time(3))

        self.play(Write(formula))
        self.play(DrawBorderThenFill(circle))
        self.wait(1)
        self.play(
            Write(razao).set_run_time(5),
            FadeOut(intro),
            FadeOut(circle),
            FadeOut(formula)
        )
        self.wait(1)
