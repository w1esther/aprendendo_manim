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