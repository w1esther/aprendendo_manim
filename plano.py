from manim import *

class Plano(MovingCameraScene):
    def construct(self):

        # MovingCameraScene é uma subclasse de Scene (ou seja, herda absolutamente todos os métodos, atributos e comportamentos da Scene tradicional.) que adiciona a capacidade de mover e dar zoom com a câmera durante a animação.
        
        for n in range(-7, 8):
            n00 = np.array([n, 0, 0])
            dotn00 = Dot(n00)
            self.play(FadeIn(dotn00))
        
        ponto01 = np.array([-7, 0, 0])
        ponto02 = np.array([7, 0, 0])
        linha01 = Line(ponto01, ponto02)

        self.play(Create(linha01))

        for i in range(-4, 5):
            n11 = np.array([0, i, 0])
            dotn11 = Dot(n11)
            self.play(FadeIn(dotn11))

        ponto03 = np.array([0, -4, 0])
        ponto04 = np.array([0, 4, 0])
        linha02 = Line(ponto03, ponto04)

        self.play(Create(linha02))

        self.wait(1)

        ponto05 = np.array([-3, 2, 0])
        funcao = Text('f(x) = -2x + 2', color=WHITE)
        funcao.move_to(ponto05)
        self.play(FadeIn(funcao))

        ponto06 = np.array([0, 2, 0])
        ponto07 = np.array([2, -2, 0])
        dot06 = Dot(ponto06, color=BLUE)
        dot07 = Dot(ponto07, color=BLUE)

        self.play(FadeIn(dot06), FadeIn(dot07))

        linha03 = Line(ponto06, ponto07, color=BLUE)
        self.play(Create(linha03))

        self.wait(4)

        # self.camera.frame é o objeto que representa o campo de visão da câmera 

        self.play(self.camera.frame.animate.scale(0.70).move_to(ORIGIN))

        self.wait(2)

        self.play(self.camera.frame.animate.move_to(RIGHT))

        ponto08 = np.array([0.5, 1, 0])
        dot08 = Dot(ponto08, color=BLUE)
        self.play(FadeIn(dot08))

        ponto09 = np.array([1.5, -1, 0])
        dot09 = Dot(ponto09, color=BLUE)
        self.play(FadeIn(dot09))

        ponto10 = np.array([1, 0, 0])
        dot10 = Dot(ponto10, color=BLUE)
        self.play(FadeIn(dot10))

        self.wait(1)

        self.play(self.camera.frame.animate.scale(2))  

        self.wait(2)

        ponto11 = np.array([-8, 0, 0])
        ponto12 = np.array([8, 0, 0])
        ponto13 = np.array([0, -5, 0])
        ponto14 = np.array([0, 5, 0])
        ponto15 = np.array([-9, 0, 0])
        ponto16 = np.array([9, 0, 0])
        ponto17 = np.array([0, -6, 0])
        ponto18 = np.array([0, 6, 0])

        dot11 = Dot(ponto11)
        dot12 = Dot(ponto12)
        dot13 = Dot(ponto13)
        dot14 = Dot(ponto14)
        dot15 = Dot(ponto15)
        dot16 = Dot(ponto16)
        dot17 = Dot(ponto17)
        dot18 = Dot(ponto18)

        self.play(self.camera.frame.animate.move_to(ORIGIN))

        self.play(FadeIn(dot11), FadeIn(dot12), FadeIn(dot13), FadeIn(dot14), FadeIn(dot15), FadeIn(dot16), FadeIn(dot17), FadeIn(dot18))

        linha04 = Line(ponto15, ponto16)
        linha05 = Line(ponto17, ponto18)

        self.play(Create(linha04), Create(linha05))

        self.wait(1)

        ponto19 = np.array([3, -4, 0])
        ponto20 = np.array([-1, 4, 0])

        dot19 = Dot(ponto19, color=BLUE)
        dot20 = Dot(ponto20, color=BLUE)

        self.play(FadeIn(dot19), FadeIn(dot20))

        linha06 = Line(ponto19, ponto20, color=BLUE)

        self.play(Create(linha06))

        self.play(linha06.animate.move_to(LEFT*4))

        self.wait(2)

        texto_ponto1 = Text('(-1; 4)', color=BLUE, font_size=20)
        ponto_texto1 = np.array([-1.5, 4, 0])
        texto_ponto1.move_to(ponto_texto1)
        
        texto_ponto2 = Text('(0; 2)', color=BLUE, font_size=20)
        ponto_texto2 = np.array([0.5, 2, 0])
        texto_ponto2.move_to(ponto_texto2)

        texto_ponto3 = Text('(0,5; 1)', color=BLUE, font_size=20)
        ponto_texto3 = np.array([1, 1, 0])
        texto_ponto3.move_to(ponto_texto3)

        texto_ponto4 = Text('(1; 0)', color=BLUE, font_size=20)
        ponto_texto4 = np.array([1.5, 0.3, 0])
        texto_ponto4.move_to(ponto_texto4)

        texto_ponto5 = Text('(1,5; -1)', color=BLUE, font_size=20)
        ponto_texto5 = np.array([2, -1, 0])
        texto_ponto5.move_to(ponto_texto5)

        texto_ponto6 = Text('(3; -4)', color=BLUE, font_size=20)
        ponto_texto6 = np.array([3.5, -4, 0])
        texto_ponto6.move_to(ponto_texto6)

        texto_ponto7 = Text('(2; -2)', color=BLUE, font_size=20)
        ponto_texto7 = np.array([2.5, -2, 0])
        texto_ponto7.move_to(ponto_texto7)

        self.play(Create(texto_ponto1), Create(texto_ponto2), Create(texto_ponto3), Create(texto_ponto4), Create(texto_ponto5), Create(texto_ponto6), Create(texto_ponto7))

        self.wait(2)