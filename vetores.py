from manim import *

class Vetores(Scene):
    def construct(self):
        
        #testando duas formas de criar linhas

        # criando linhas
        linha01 = Line(2*RIGHT, LEFT)
        self.play(Create(linha01))
        self.wait(2)

        #criando linhas por pontos, usando eles como referencia

        ponto01 = np.array([1, 2, 0])
        ponto02 = np.array([-1, 3, 0])
        linha02 = Line(ponto01, ponto02)

        self.play(Create(linha02))

        #criando novos pontos 
        ponto03 = np.array([-2, -1, 0])
        ponto04 = np.array([3, -2, 0])

        # A função Dot cria o ponto na tela
        dot03 = Dot(ponto03)
        dot04 = Dot(ponto04)

        #criando linha que vai do ponto 03 ao ponto 04 

        linha03 = Line(ponto03, ponto04)
        self.play(Create(dot03), Create(dot04),Create(linha03))