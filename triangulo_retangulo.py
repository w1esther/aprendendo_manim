from manim import *

class TrianguloRetangulo(Scene):
# tudo que vai aparecer na tela deve estar dentro de uma Scene
    def construct(self):
    # função responsável por construir a cena
        pitagoras = Text('Teorema de Pitágoras', color=BLUE)
        pitagoras.move_to(ORIGIN + UP*3)

        a = LEFT*2 + DOWN*2
        b = RIGHT*2 + DOWN*2
        c = LEFT*2 + UP*2
        # definição dos pontos (vértices) do triângulo

        triangulo_retangulo = Polygon(a, b, c, color=BLUE)
        # crio o triângulo com os pontos definidos anteriormente

        self.play(Create(triangulo_retangulo))
        self.play(FadeIn(pitagoras))
        # executa animações na cena
        self.wait(2)
        self.play(triangulo_retangulo.animate.scale(0.75))
        self.wait(2)

        numero_ab = Text('3', color=BLUE_B)
        numero_ab.move_to((a + b)/2 + RIGHT*0.2)

        numero_ac = Text('4', color=BLUE_B)
        numero_ac.move_to((a + c)/2 + LEFT*0.1)

        numero_bc = Text('5', color=BLUE_B)
        numero_bc.move_to((b + c)/2 + RIGHT*0.8)

        self.play(FadeIn(numero_ab))
        self.play(FadeIn(numero_ac))
        self.play(FadeIn(numero_bc))
        self.wait(2)

        quadrado_ab = Square(side_length=3, color=BLUE_D)
        quadrado_ab.move_to((a + b)/2 + UP*1.5)
        self.play (Create(quadrado_ab))

        quadrado_ac = Square(side_length=4, color=BLUE_D)
        quadrado_ac.move_to((a + c)/2 + LEFT*1.5)
        self.play(Create(quadrado_ac))

        quadrado_bc = Square(side_length=5, color=BLUE_D)
        quadrado_bc.rotate(-45 * DEGREES)
        quadrado_bc.move_to((b + c)/2 + UP*0.7)
        self.play(Create(quadrado_bc))

        self.wait(2)