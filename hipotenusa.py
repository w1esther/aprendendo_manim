from manim import *
from math import sqrt, atan2

class Hipotenusa(Scene):
    def construct(self):
        a, b = 3, 4
        c = sqrt(a**2 + b**2)

        tri = Polygon(ORIGIN, a*RIGHT, b*UP, color=WHITE)
        tri.move_to(ORIGIN + UP)
        self.play(Create(tri))

        self.play(tri.animate.scale(0.5))
        self.wait(2)

        sq_a = Square(side_length=a * 0.5, color=BLUE).next_to(tri, DOWN, buff=0, aligned_edge=LEFT)
        sq_b = Square(side_length=b * 0.5, color=GREEN).next_to(tri, LEFT, buff=0, aligned_edge=DOWN)
        
        #calcula o ponto médio da hipotenusa
        meio_hipotenusa = (a*RIGHT + b*UP)/2
        
        sq_c = Square(side_length=c * 0.5, color=RED).move_to(meio_hipotenusa)
       
       # cria um vetor que representa o ponto final da hiporenusa e o ponto inicial respectivamente 
        v = np.array([0, b, 0]) - np.array([a, 0, 0])
        # resultado: [-a, b, 0] (subtração de vetores)

        #v[1]-componente y do vetor v[0]-componente x do vetor 
        # atan2 é uma função matemática que calcula o ângulo entre o vetor (x, y) e o eixo x 

        #obs fazer sem o facilitador atan2
        angle = atan2(v[1], v[0])
        #vai gerar aproximadamente o ângulo 126.87
        sq_c.rotate(angle, about_point=sq_c.get_center())

        self.play(Create(sq_a), Create(sq_b), Create(sq_c))
        self.wait(1)
        
        print('Right:', RIGHT)
        print('left:', LEFT)
        print('up:', UP)
        print('down: ', DOWN)