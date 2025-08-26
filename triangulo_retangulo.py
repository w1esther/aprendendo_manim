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

        # horizontais
        linha1 = Line(LEFT*3.5, RIGHT*-1, color=BLUE).shift(UP*1.1)
        linha2 = Line(LEFT*3.5, RIGHT*-1, color=BLUE).shift(UP*0.4)
        linha3 = Line(LEFT*3.5, RIGHT*-1, color=BLUE).shift(DOWN*0.2)

        # verticais
        linha4 = Line(UP*1.75, DOWN*0.75, color=BLUE).shift(LEFT*2.8)
        linha5 = Line(UP*1.75, DOWN*0.75, color=BLUE).shift(LEFT*2.2)
        linha6 = Line(UP*1.75, DOWN*0.75, color=BLUE).shift(LEFT*1.6)

        for l in [linha1, linha2, linha3, linha4, linha5, linha6]:
            self.play(Create(l))

        self.wait(2)

        quadrado_ac.set_fill(color=BLUE, opacity=0)
        self.play(quadrado_ac.animate.set_fill(color=BLUE, opacity=1))

        quatro_quadrado = Text('4^4', color=WHITE)
        quatro_quadrado.move_to(ORIGIN + LEFT*2.2 + UP*0.7 )
        self.play(FadeIn(quatro_quadrado))

        self.wait(2)

        # linha7 = Line(LEFT*2.1, RIGHT*1.22, color=BLUE).rotate(-51.34*DEGREES)
        # linha7.move_to(UP*2.9 + RIGHT*1.5)

        # linha8 = Line(LEFT*2.1, RIGHT*1.22, color=BLUE).rotate(-51.34*DEGREES)
        # linha8.move_to(UP*1.9 + RIGHT*1.9)

        # linha9 = Line(LEFT*2.1, RIGHT*1.22, color=BLUE).rotate(-51.34*DEGREES)
        # linha9.move_to(UP*1.8 + RIGHT*1.6)

        # linha10 = Line(LEFT*2.1, RIGHT*1.22, color=BLUE).rotate(-51.34*DEGREES)
        # linha10.move_to(UP*1.4 + RIGHT*2.7)

        # for n in [linha7, linha8, linha9, linha10]:
        #     self.play(Create(n))

                # altura do quadrado
        h = 3.22  

        # número de linhas internas
        n = 4  

        # linha base (bem comprida), já rotacionada
        base_line = Line(LEFT*2.5, RIGHT*2.5, color=BLUE).rotate(-51.34*DEGREES)

        # centro do quadrado
        centro = quadrado_bc.get_center()

        linhas = []
        for i in range(1, n+1):
            desloc = (h/(n+1)) * (i - (n+1)/2)  # deslocamento relativo ao centro
            linha = base_line.copy().move_to(centro + desloc * UP)  
            linhas.append(linha)

        for l in linhas:
            self.play(Create(l))


        self.wait(2)
