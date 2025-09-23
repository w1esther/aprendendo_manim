from manim import *

class PitagorasBloquinhos(Scene):
    def construct(self):
        # Lados do triângulo
        a, b = 3, 4
        c = (a**2 + b**2) ** 0.5

        # Triângulo retângulo
        tri = Polygon(ORIGIN, a*RIGHT, b*UP, color=WHITE)
        tri.move_to(ORIGIN + UP)
        self.play(Create(tri))

        self.wait(2)
        self.play(tri.animate.scale(0.5))


        # Quadrados nos lados
        sq_a = Square(side_length=a * 0.5, color=BLUE).next_to(tri, DOWN, buff=0, aligned_edge=LEFT)
        sq_b = Square(side_length=b * 0.5, color=GREEN).next_to(tri, LEFT, buff=0, aligned_edge=DOWN)
        sq_c = Square(side_length=c * 0.5, color=RED).move_to([a/2, b/2, 0] + LEFT*0.7 + DOWN*0.22 + RIGHT*0.25).rotate((120.0))
        #atenção no uso do rotate
        #obs usae next_to para tentar fazer alinhamento

        self.play(Create(sq_a), Create(sq_b), Create(sq_c))
        self.wait(1)

        # Criar bloquinhos nos quadrados dos catetos
        bloquinhos = VGroup()
        for i in range(a):
            for j in range(a):
                bloco = Square(side_length=0.5, fill_color=BLUE, fill_opacity=0.7, stroke_width=0)
                bloco.move_to(sq_a.get_corner(DL) + RIGHT*(i+0.5)*0.5 + UP*(j+0.5)*0.5)
                bloquinhos.add(bloco)

        #sq_a.get_corner(DL) retorna a coordenada do canto inferior-esquerdo (DL = down-left) do quadrado sq_a.

        for i in range(b):
            for j in range(b):
                bloco = Square(side_length=0.5, fill_color=GREEN, fill_opacity=0.7, stroke_width=0)
                bloco.move_to(sq_b.get_corner(DL) + RIGHT*(i+0.5) * 0.5 + UP*(j+0.5)*0.5)
                bloquinhos.add(bloco)

        self.play(LaggedStartMap(FadeIn, bloquinhos, lag_ratio=0.02))

        self.wait(2)
        
        bloquinhos2 = bloquinhos.copy().rotate(125*DEGREES)
        self.play(Transform(bloquinhos, bloquinhos2))
        # Posicionamento alvo dos bloquinhos no quadrado da hipotenusa

        destinos = VGroup()
        n = int(c)
        for i in range(n):
            for j in range(n):
                bloco = Square(side_length=0.5, stroke_width=0)
                # Criamos um quadradinho invisível (sem borda e sem preenchimento). Ele não vai aparecer na cena, mas serve como um alvo.
                pos = sq_c.get_center() + (i - n/2 + 0.5) * RIGHT + (j - n/2 + 0.5) * UP
                bloco.move_to(pos * 0.5)
                destinos.add(bloco)
                
        destinos.rotate(125* DEGREES, about_point=sq_c.get_center())

        # Animação: bloquinhos se movem até formar c^2
        anims = [bloquinhos[k].animate.move_to(destinos[k].get_center() + UP*1 + LEFT*1.55 + DOWN*1.1 + RIGHT*0.5) for k in range(len(bloquinhos))]
        self.play(*anims, run_time=4)
        self.wait(2)