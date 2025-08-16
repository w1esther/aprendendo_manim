from manim import *

class TrianguloRetangulo(Scene):
    def construct(self):
        a = LEFT*2 + DOWN*2
        b = RIGHT*2 + DOWN*2
        c = LEFT*2 + UP*2

        triangulo_retangulo = Polygon(a, b, c, color=BLUE)

        self.play(Create(triangulo_retangulo))
        self.wait(2)
