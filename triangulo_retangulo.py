from manim import *

class TrianguloRetangulo(Scene):
# tudo que vai aparecer na tela deve estar dentro de uma Scene
    def construct(self):
    # função responsável por construir a cena

        # pitagoras = Text('Teorema de Pitágoras', color=BLUE, font_size=24)
        # pitagoras.move_to(ORIGIN + UP*3.5)

        a = LEFT*2 + DOWN*2
        b = RIGHT*2 + DOWN*2
        c = LEFT*2 + UP*3
        # definição dos pontos (vértices) do triângulo

        triangulo_retangulo = Polygon(a, b, c, color=BLUE)
        # crio o triângulo com os pontos definidos anteriormente

        self.play(Create(triangulo_retangulo))
        # self.play(FadeIn(pitagoras))
        # executa animações na cena
        self.wait(2)
        self.play(triangulo_retangulo.animate.scale(0.5))
        self.wait(2)

        numero_ab = Text('3', color=BLUE_B)
        numero_ab.move_to((a + b)/2 + RIGHT*0.1 + UP*0.4)

        numero_ac = Text('4', color=BLUE_B)
        numero_ac.move_to((a + c)/2 + RIGHT*0.5)

        numero_bc = Text('5', color=BLUE_B)
        numero_bc.move_to((b + c)/2 + RIGHT*0.8)

        self.play(FadeIn(numero_ab))
        self.play(FadeIn(numero_ac))
        self.play(FadeIn(numero_bc))
        self.wait(2)

        quadrado_ab = Square(side_length=2.0, color=BLUE_D)
        quadrado_ab.move_to((a + b)/2 + UP*0.25) 
        self.play (Create(quadrado_ab))

        quadrado_ac = Square(side_length=2.5, color=BLUE_D)
        quadrado_ac.move_to((a + c)/2 + LEFT*0.25)
        self.play(Create(quadrado_ac))

        quadrado_bc = Square(side_length=3.22, color=BLUE_D)
        quadrado_bc.rotate(-51.34 * DEGREES)
        quadrado_bc.move_to((b + c)/2 + UP*1.05 + RIGHT*1.2)
        self.play(Create(quadrado_bc))

        self.wait(2)
        self.play(FadeOut(numero_ab))
        self.play(FadeOut(numero_ac))
        self.play(FadeOut(numero_bc))
        self.wait(2)
        
        # linha1 = Line(LEFT*3.5, RIGHT*-1, color=BLUE).shift(UP*4)
        # self.play(Create(linha1))

        # linha2 = linha1.copy().shift(UP*0.8)
        # self.play(Create(linha2))

        # linha3 = linha1.copy().shift(DOWN*0.8)
        # self.play(Create(linha3))
        
        # linha4 = Line(LEFT*3.5, RIGHT*-1, color=BLUE).rotate(DEGREES*90).shift(UP*0.5)
        # self.play(Create(linha4))

        # linha5 = linha4.copy().move_to(LEFT*1.5)
        # self.play(Create(linha5))

        # linha6 = linha4.copy().move_to(RIGHT*1.5)
        # self.play(Create(linha6))

        # horizontais
        linha1 = Line(LEFT*3.5, RIGHT*-1, color=BLUE).shift(UP*0.8)
        linha2 = Line(LEFT*3.5, RIGHT*-1, color=BLUE)
        linha3 = Line(LEFT*3.5, RIGHT*-1, color=BLUE).shift(DOWN*0.8)

        # verticais
        linha4 = Line(UP*2, DOWN*2, color=BLUE).shift(LEFT*1.5)
        linha5 = Line(UP*2, DOWN*2, color=BLUE)
        linha6 = Line(UP*2, DOWN*2, color=BLUE).shift(RIGHT*1.5)

        for l in [linha1, linha2, linha3, linha4, linha5, linha6]:
            self.play(Create(l))

        self.wait(2)