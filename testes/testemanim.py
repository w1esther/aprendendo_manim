from manim import *

class HelloWorld(Scene):
    def construct(self):
        text = Text('olá, manim!')
        self.play(Write(text))
        self.wait(2)