from manim import *
class LinhaDoTempo(Scene):
    def construct(self):
        linha = NumberLine(
            x_range=[-400, 1600, 200],
            length=10,
            color=BLUE,
            include_numbers=True,
            label_direction=UP,
        )
        line_group=VGroup(linha).arrange(DOWN, buff=1)
        self.play(Write(line_group))
        self.wait()
        self.play(
            line_group.animate.scale(2).shift((-5,0,0))
        )
        self.wait(2)
        self.play(
            line_group.animate.shift((10,0,0))
        )
        self.play(
            Write(Ellipse(width=5, height=2.5).shift((0,-0.5,0)))
        )
        self.wait()