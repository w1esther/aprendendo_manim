from manim import *

class Volumes(ThreeDScene):
    def construct(self):
        
        self.set_camera_orientation(phi=60*DEGREES, theta=30*DEGREES)

        cubo = Cube(side_length=2, fill_color=BLUE, fill_opacity=0.3)

        t1 = Text('Volume do cubo', color=BLUE)
        t1.move_to(ORIGIN + DOWN*2.5 + LEFT*2.5)   
        t1.rotate(180*DEGREES) 

        self.play(FadeIn(cubo), FadeIn(t1))

        