from manim import *
import numpy as np
from math import sqrt, atan2

class Hipotenusa(Scene):
    def construct(self):
        a, b = 3, 4
        c = sqrt(a**2 + b**2)

        sf = 0.5           # mesmo fator de escala que você usava
        shift = UP         # onde você queria posicionar o triângulo

        # --- triângulo já com escala aplicada (evita confusão com move_to+scale) ---
        tri = Polygon(ORIGIN, a*sf*RIGHT, b*sf*UP, color=WHITE)
        tri.shift(shift)
        self.play(Create(tri))

        # quadrados dos catetos (usar a mesma escala)
        sq_a = Square(side_length=a*sf, color=BLUE).next_to(tri, DOWN, buff=0, aligned_edge=LEFT)
        sq_b = Square(side_length=b*sf, color=GREEN).next_to(tri, LEFT, buff=0, aligned_edge=DOWN)

        # --- coordenadas dos vértices (em coordenadas de cena) ---
        O = np.array([0, 0, 0]) + shift
        P_x = np.array([a*sf, 0, 0]) + shift   # vértice no cateto x
        P_y = np.array([0, b*sf, 0]) + shift   # vértice no cateto y

        A = P_y.copy()   # um extremo da hipotenusa (0, b*sf) + shift
        B = P_x.copy()   # outro extremo (a*sf, 0) + shift

        # vetor e unidade ao longo da hipotenusa
        AB = B - A
        length_AB = np.linalg.norm(AB[:2])
        u = AB / length_AB   # direção unitária ao longo da hipotenusa (2D)

        # ponto médio da hipotenusa
        M = (A + B) / 2

        # normal unitária (rotaciona u em +90º): n = (-u_y, u_x)
        n = np.array([-u[1], u[0], 0])

        # queremos que n aponte PARA FORA do triângulo; checamos o centróide do triângulo
        centroid = (O + P_x + P_y) / 3
        if np.dot(n, centroid - M) > 0:
            n = -n   # inverte se estiver apontando para o interior

        # side do quadrado (com escala)
        s = c * sf

        # centro do quadrado: desloca o ponto médio pela normal em s/2
        center_sq_c = M + n * (s/2)

        # criar, rotacionar (lado paralelo a hipotenusa) e colocar no centro calculado
        sq_c = Square(side_length=s, color=RED)
        angle = atan2(u[1], u[0])   # ângulo da hipotenusa
        sq_c.rotate(angle, about_point=sq_c.get_center())
        sq_c.move_to(center_sq_c)

        # animações finais
        self.play(Create(sq_a), Create(sq_b), Create(sq_c))
        self.wait(2)
