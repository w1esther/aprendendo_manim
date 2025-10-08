from manim import *

class Plano(Scene):
    def construct(self):
        
        for n in range(-7, 8):
            n00 = np.array([n, 0, 0])
            dotn00 = Dot(n00)
            self.play(Create(dotn00))
        
        ponto01 = np.array([-7, 0, 0])
        ponto02 = np.array([7, 0, 0])
        linha01 = Line(ponto01, ponto02)

        self.play(Create(linha01))

        for i in range(-4, 5):
            n11 = np.array([0, i, 0])
            dotn11 = Dot(n11)
            self.play(Create(dotn11))

        ponto03 = np.array([0, -4, 0])
        ponto04 = np.array([0, 4, 0])
        linha02 = Line(ponto03, ponto04)

        self.play(Create(linha02))