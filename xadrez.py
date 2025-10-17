from manim import *

class Xadrez(MovingCameraScene):
    def construct(self):

        ponto01 = np.array([-4, 4, 0])
        ponto02 = np.array([4, 4, 0])
        ponto03 = np.array([-4, -4, 0])
        ponto04 = np.array([4, -4, 0])

        linha1 = Line(ponto01, ponto02)
        linha2 = Line(ponto02, ponto04)
        linha3 = Line(ponto04, ponto03)
        linha4 = Line(ponto03, ponto01)

        self.play(Create(linha1), Create(linha2), Create(linha3), Create(linha4))

        self.wait(2)

        self.play(self.camera.frame.animate.scale(2))  

        self.wait(2)

        texto1 = Text('Crescimento exponencial:')
        ponto05 = np.array([0, 5, 0])
        texto1.move_to(ponto05)

        self.play(Create(texto1))

        # Cria os bloquinhos do tabuleiro
        bloquinhos = VGroup()
        side_length = 1  # cada quadradinho tem 1 unidade

        for i in range(8):
            for j in range(8):
                # alterna cor pra parecer tabuleiro de xadrez
                color = BLUE if (i + j) % 2 == 0 else WHITE

                bloco = Square(
                    side_length=side_length,
                    fill_color=color,
                    fill_opacity=1,
                    stroke_width=0
                )

                # posiciona o bloco no lugar certo
                x = -4 + (j + 0.5) * side_length
                y = 4 - (i + 0.5) * side_length
                bloco.move_to([x, y, 0])

                bloquinhos.add(bloco)

        self.play(FadeIn(bloquinhos))
        self.wait(2)

        self.wait(2)

        texto2 = Text('•', color=RED)
        ponto06 = np.array([-3.5, -3.5, 0])
        texto2.move_to(ponto06)

        self.play(FadeIn(texto2))

        self.wait(1)

        texto3 = Text('•', color=RED)
        ponto07 = np.array([-2.3, -3.5, 0])
        texto3.move_to(ponto07)

        texto4 = Text('•', color=RED)
        ponto08 = np.array([-2.7, -3.5, 0])
        texto4.move_to(ponto08)

        self.play(FadeIn(texto3), FadeIn(texto4))

        self.wait(1)

        texto5 = Text('•', color=RED)
        ponto09 = np.array([-1.8, -3.5, 0])
        texto5.move_to(ponto09)

        texto6 = Text('•', color=RED)
        ponto10 = np.array([-1.6, -3.5, 0])
        texto6.move_to(ponto10)

        texto7 = Text('•', color=RED)
        ponto11 = np.array([-1.4, -3.5, 0])
        texto7.move_to(ponto11)

        texto8 = Text('•', color=RED)
        ponto12 = np.array([-1.2, -3.5, 0])
        texto8.move_to(ponto12)

        self.play(FadeIn(texto5), FadeIn(texto6), FadeIn(texto7), FadeIn(texto8))

        self.wait(1)

        texto9 = Text('•', color=RED)
        ponto13 = np.array([-0.8, -3.3, 0])
        texto9.move_to(ponto13)

        texto10 = Text('•', color=RED)
        ponto14 = np.array([-0.6, -3.3, 0])
        texto10.move_to(ponto14)

        texto11 = Text('•', color=RED)
        ponto15 = np.array([-0.4, -3.3, 0])
        texto11.move_to(ponto15)

        texto12 = Text('•', color=RED)
        ponto16 = np.array([-0.2, -3.3, 0])
        texto12.move_to(ponto16)

        texto13 = Text('•', color=RED)
        ponto17 = np.array([-0.8, -3.7, 0])
        texto13.move_to(ponto17)

        texto14 = Text('•', color=RED)
        ponto18 = np.array([-0.6, -3.7, 0])
        texto14.move_to(ponto18)

        texto15 = Text('•', color=RED)
        ponto19 = np.array([-0.4, -3.7, 0])
        texto15.move_to(ponto19)

        texto16 = Text('•', color=RED)
        ponto20 = np.array([-0.2, -3.7, 0])
        texto16.move_to(ponto20)

        self.play(FadeIn(texto9), FadeIn(texto10), FadeIn(texto11), FadeIn(texto12), FadeIn(texto13), FadeIn(texto14), FadeIn(texto15), FadeIn(texto16))

        self.wait(1)

        texto17 = Text('•', color=RED)
        ponto21 = np.array([0.8, -3.4, 0])
        texto17.move_to(ponto21)

        texto18 = Text('•', color=RED)
        ponto22 = np.array([0.6, -3.4, 0])
        texto18.move_to(ponto22)

        texto19 = Text('•', color=RED)
        ponto23 = np.array([0.4, -3.4, 0])
        texto19.move_to(ponto23)

        texto20 = Text('•', color=RED)
        ponto24 = np.array([0.2, -3.4, 0])
        texto20.move_to(ponto24)

        texto21 = Text('•', color=RED)
        ponto25 = np.array([0.8, -3.6, 0])
        texto21.move_to(ponto25)

        texto22 = Text('•', color=RED)
        ponto26 = np.array([0.6, -3.6, 0])
        texto22.move_to(ponto26)

        texto23 = Text('•', color=RED)
        ponto27 = np.array([0.4, -3.6, 0])
        texto23.move_to(ponto27)

        texto24 = Text('•', color=RED)
        ponto28 = np.array([0.2, -3.6, 0])
        texto24.move_to(ponto28)

        texto25 = Text('•', color=RED)
        ponto29 = np.array([0.8, -3.2, 0])
        texto25.move_to(ponto29)

        texto26 = Text('•', color=RED)
        ponto30 = np.array([0.6, -3.2, 0])
        texto26.move_to(ponto30)

        texto27 = Text('•', color=RED)
        ponto31 = np.array([0.4, -3.2, 0])
        texto27.move_to(ponto31)

        texto28 = Text('•', color=RED)
        ponto32 = np.array([0.2, -3.2, 0])
        texto28.move_to(ponto32)

        texto29 = Text('•', color=RED)
        ponto33 = np.array([0.8, -3.8, 0])
        texto29.move_to(ponto33)

        texto30 = Text('•', color=RED)
        ponto34 = np.array([0.6, -3.8, 0])
        texto30.move_to(ponto34)

        texto31 = Text('•', color=RED)
        ponto35 = np.array([0.4, -3.8, 0])
        texto31.move_to(ponto35)

        texto32 = Text('•', color=RED)
        ponto36 = np.array([0.2, -3.8, 0])
        texto32.move_to(ponto36)

        self.play(FadeIn(texto17), FadeIn(texto18), FadeIn(texto19), FadeIn(texto20), FadeIn(texto21), FadeIn(texto22), FadeIn(texto23), FadeIn(texto24), FadeIn(texto25), FadeIn(texto26), FadeIn(texto27), FadeIn(texto28), FadeIn(texto29), FadeIn(texto30), FadeIn(texto31), FadeIn(texto32))

        # pontos = []  # Lista para guardar os textos

        # # Coordenadas de base
        # xs = [0.8, 0.6, 0.4, 0.2]   # posições no eixo x
        # ys = [-3.2, -3.4, -3.6, -3.8]  # posições no eixo y

        # # Cria os textos com um laço duplo
        # for y in ys:
        #     for x in xs:
        #         ponto = np.array([x, y, 0])
        #         texto = Text('•', color=RED)
        #         texto.move_to(ponto)
        #         pontos.append(texto)

        # # Mostra todos com FadeIn
        # self.play(*[FadeIn(t) for t in pontos])

        # self.wait(2)


        self.wait(1)

        self.play(self.camera.frame.animate.scale(0.50).move_to(ORIGIN))

        self.wait(0.5)

        self.play(self.camera.frame.animate.move_to(DOWN*3))

        self.wait(1)