from manim import *
from math import sqrt, atan2

class Hipotenusa(Scene):
    def construct(self):

        # define os valores dos catetos e da hipotenusa

        a, b = 3, 4
        c = sqrt(a**2 + b**2)

        fe = 0.5

        # tri cria o triângulo retângulo 

        tri = Polygon(ORIGIN, a*fe*RIGHT, b*fe*UP, color=WHITE)
        self.play(Create(tri))

        

        # cria os quadrados adjacentes ao catetos

        sq_a = Square(side_length=a * fe, color=BLUE).next_to(tri, DOWN, buff=0, aligned_edge=LEFT)
        sq_b = Square(side_length=b * fe, color=GREEN).next_to(tri, LEFT, buff=0, aligned_edge=DOWN) 

        # define os pontos da hipotenusa

        O = np.array([0, 0, 0]) 
        p_y= np.array([0, b*fe, 0])
        p_x = np.array([a*fe, 0, 0]) 

        # define os extremos da hipotenusa

        A = p_y.copy()
        B = p_x.copy()

        # vetor da hipotenusa, aponta de A até B

        v = B - A

        # comprimento da hipotenusa, fazer sem o artifício

        length_v = np.linalg.norm(v[:2])

        # vetor unitário na direção da hipotenusa

        u = v / length_v 

        # calcula ponto médio da hipotenusa

        meio_hipotenusa = (A + B)/2

        # vetor perpendicular à hipotenusa

        n = np.array([-u[1], u[0], 0])

        # centro do triângulo

        centro_tri = (O + p_x + p_y)/3

        # se o vetor apontar para dentro ele é invertido

        if np.dot(n, centro_tri - meio_hipotenusa) > 0:
            n = -n

        # define lado do quadrado da hipotenusa

        s = c * fe

        # define centro do quadrado da hipotenusa no meio dela

        centro_sq_c = meio_hipotenusa + n * (s/2)

        # calcula o ângulo da hipotenusa com o eixo x.

        angle = atan2(v[1], v[0])
        
        # cria o quadrado adjacente à hipotenusa e o posiciona adequadamemte

        sq_c = Square(side_length=s, 
        color=RED)
        sq_c.rotate(angle, about_point=sq_c.get_center())
        sq_c.move_to(centro_sq_c)
        
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
        lado_bloco = s / n

        for i in range(n):
            for j in range(n):
                bloco = Square(side_length=lado_bloco, stroke_width=0)
                # Criamos um quadradinho invisível (sem borda e sem preenchimento). Ele não vai aparecer na cena, mas serve como um alvo.
                pos = ((i - n/2 + 0.5) *lado_bloco)* RIGHT + ((j - n/2 + 0.5) *lado_bloco) * UP
                bloco.move_to(centro_sq_c + pos)
                destinos.add(bloco)
                
        destinos.rotate(angle, about_point=centro_sq_c)

        # Animação: bloquinhos se movem até formar c^2
        anims = [bloquinhos[k].animate.move_to(destinos[k].get_center()) for k in range(len(bloquinhos))]
        self.play(*anims, run_time=4)
        self.wait(2)

        print(RIGHT)