from manim import *

class TrianguloRetangulo(Scene):
# tudo que vai aparecer na tela deve estar dentro de uma Scene
    def construct(self):
    # função responsável por construir a cena

        a = LEFT*2 + DOWN*2
        b = RIGHT*2 + DOWN*2
        c = LEFT*2 + UP*3
        # definição dos pontos (vértices) do triângulo

        triangulo_retangulo = Polygon(a, b, c, color=BLUE)
        # crio o triângulo com os pontos definidos anteriormente

        self.play(Create(triangulo_retangulo))
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

        # # horizontais
        # linha1 = Line(LEFT*3.5, RIGHT*-1, color=BLUE).shift(UP*1.1)
        # linha2 = Line(LEFT*3.5, RIGHT*-1, color=BLUE).shift(UP*0.4)
        # linha3 = Line(LEFT*3.5, RIGHT*-1, color=BLUE).shift(DOWN*0.2)

        # # verticais
        # linha4 = Line(UP*1.75, DOWN*0.75, color=BLUE).shift(LEFT*2.8)
        # linha5 = Line(UP*1.75, DOWN*0.75, color=BLUE).shift(LEFT*2.2)
        # linha6 = Line(UP*1.75, DOWN*0.75, color=BLUE).shift(LEFT*1.6)

        # for l in [linha1, linha2, linha3, linha4, linha5, linha6]:
        #     self.play(Create(l))

        # self.wait(2)

        quadrado_ac.set_fill(color=BLUE, opacity=0)
        self.play(quadrado_ac.animate.set_fill(color=BLUE, opacity=1))

        quatro_quadrado = Text('4²', color=WHITE)
        quatro_quadrado.move_to(ORIGIN + LEFT*2.2 + UP*0.7 )
        self.play(FadeIn(quatro_quadrado))

        self.wait(2)

        # linha_base = Line(LEFT*3, RIGHT*3, color=BLUE).rotate(-51.34*DEGREES)

        # linha7  = linha_base.copy().shift(LEFT*-4.0)
        # linha8  = linha_base.copy().shift(LEFT*-4.4)
        # linha9  = linha_base.copy().shift(LEFT*-4.8)
        # linha10 = linha_base.copy().shift(LEFT*-5.3)

        # for n in [linha7, linha8, linha9, linha10]:
        #     self.play(Create(n))

        quadrado_ab.set_fill(color=BLUE, opacity=0)
        self.play(quadrado_ab.animate.set_fill(color=BLUE, opacity=1))

        tres_quadrado = Text('3²', color=WHITE)
        tres_quadrado.move_to(ORIGIN + RIGHT*0.2 + DOWN*1.7 )
        self.play(FadeIn(tres_quadrado))

        self.wait(2)

        quadrado_bc.set_fill(color=BLUE, opacity=0)
        self.play(quadrado_bc.animate.set_fill(color=BLUE, opacity=1))

        cinco_quadrado = Text('5²', color=WHITE)
        cinco_quadrado.move_to(ORIGIN + RIGHT*1.2 + UP*1.5 )
        self.play(FadeIn(cinco_quadrado))
        self.wait(2)

        for n in [quadrado_ab, quadrado_ac, quadrado_bc, triangulo_retangulo]:
            self.play(FadeOut(n))
        
        self.wait(2)

        tres_quadrado.move_to(ORIGIN + UP*0.7)
        self.play(FadeIn(tres_quadrado))
        self.wait(1)
        cinco_quadrado.move_to(ORIGIN + UP*0.7 + RIGHT*1.9)
        self.play(FadeIn(cinco_quadrado))
        self.wait(1)

        mais_um = Text('+', color = WHITE)
        mais_um.move_to(ORIGIN + UP*0.6+LEFT*1.2)

        igual = Text('=', color=WHITE)
        igual.move_to(ORIGIN + UP*0.6 + RIGHT*0.9)

        for l in [mais_um, igual]:
            self.play(Create(l))

        self.wait(2)

        dezesseis = Text('16', color=WHITE)
        dezesseis.move_to(ORIGIN + LEFT*2.2 + UP*0.7 )
        nove = Text('9', color=WHITE)
        nove.move_to(ORIGIN + UP*0.7)
        vinte_cinco = Text('25', color=WHITE)
        vinte_cinco.move_to(ORIGIN + UP*0.7 + RIGHT*1.9)

        self.play(Transform(quatro_quadrado, dezesseis))
        self.play(Transform(tres_quadrado, nove))
        self.play(Transform(cinco_quadrado, vinte_cinco))

        pitagoras = Text('Teorema de Pitágoras', color=BLUE, font_size=34)
        pitagoras.move_to(ORIGIN + UP*2.5)
        self.play(FadeIn(pitagoras))

        forma_geral = Text('A soma do quadro dos catetos ' \
        'é igual ao quadrado da hipotenusa', color=BLUE, font_size=24)
        forma_geral.move_to(ORIGIN + DOWN*0.5)

        self.play(Create(forma_geral))

        a = Text('a', color=WHITE)
        a.move_to(ORIGIN + LEFT*2.2 + UP*0.7 )
        b = Text('b', color=WHITE)
        b.move_to(ORIGIN + UP*0.7)
        c = Text('c', color=WHITE)
        c.move_to(ORIGIN + UP*0.7 + RIGHT*1.9)
        
        for n in [quatro_quadrado, tres_quadrado, cinco_quadrado]:
            self.play(FadeOut(n))

        self.play(FadeIn(a))
        self.play(FadeIn(b))
        self.play(FadeIn(c))

        self.wait(2)