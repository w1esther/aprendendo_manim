from manim import *

class Plano(MovingCameraScene):
    def construct(self):

        # MovingCameraScene é uma subclasse de Scene (ou seja, herda absolutamente todos os métodos, atributos e comportamentos da Scene tradicional.) que adiciona a capacidade de mover e dar zoom com a câmera durante a animação.
        
        for n in range(-7, 8):
            n00 = np.array([n, 0, 0])
            dotn00 = Dot(n00)
            self.play(Create(dotn00))
        
        ponto01 = np.array([-7, 0, 0])
        ponto02 = np.array([7, 0, 0])
        linha01 = Line(ponto01, ponto02)

        self.play(Create(linha01))

        for i in range(-4, 5):
            n11 = np.array([0, i, 0])
            dotn11 = Dot(n11)
            self.play(Create(dotn11))

        ponto03 = np.array([0, -4, 0])
        ponto04 = np.array([0, 4, 0])
        linha02 = Line(ponto03, ponto04)

        self.play(Create(linha02))

        self.wait(2)

        # self.camera.frame é o objeto que representa o campo de visão da câmera 

        self.play(self.camera.frame.animate.scale(0.5).move_to(ORIGIN))

        self.wait(2)

        self.play(self.camera.frame.animate.move_to(LEFT))

        self.wait(2)