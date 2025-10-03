from manim import *

class GeometricShapes(Scene):
    def construct(self):
        d = Dot()
        c = Circle()
        s = Square()
        t = Triangle()
        d.next_to(c, 0.00001*RIGHT)
        s.next_to(c, LEFT)
        t.next_to(c, DOWN)
        self.add(d, c, s, t)
        self.wait(10)