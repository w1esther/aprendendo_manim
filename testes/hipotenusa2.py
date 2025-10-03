from manim import *
from math import sqrt, atan2

class Hipotenusa(ThreeDScene):
    def construct(self):

        # self.set_camera_orientation(phi=60*DEGREES, theta=30*DEGREES)

        # define os valores dos catetos e da hipotenusa

        a, b = 3, 3
        c = sqrt(a**2 + b**2)

        fe = 0.5

        # tri cria o triângulo retângulo 

        # vetor1 = np.array([1, 1, 1])
        # vetor2 = np.array([8, 3, 2])
        # vetor3 = np.array([2, 2, 2])
        # vetor4 = np.array([-3, 4, 6])
        # tri = Polygon(vetor1, vetor2, vetor3, vetor4, color=WHITE)
        # self.play(Create(tri))
        # self.wait(2)

        # tri cria o triângulo retângulo 

        tri = Polygon(ORIGIN, a*fe*RIGHT, b*fe*UP, color=WHITE)
        self.play(Create(tri))

        sq_a = Square(side_length=a * fe, color=BLUE).next_to(tri, DOWN, buff=0, aligned_edge=LEFT)
        sq_b = Square(side_length=b * fe, color=GREEN).next_to(tri, LEFT, buff=0, aligned_edge=DOWN) 
        sq_c = Square(side_length=c * fe, color=RED).next_to(tri, RIGHT, buff=0)

        self.play(Create(sq_a), Create(sq_b), Create(sq_c))


        self.wait(10)