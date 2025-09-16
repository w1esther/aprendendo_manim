from manim import *

class Volumes(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        text3d = Text("This is a 3D text")
        self.add_fixed_in_frame_mobjects(text3d)
        text3d.to_corner(UL)
        self.add(axes)
        self.wait()
        
        # self.set_camera_orientation(phi=60*DEGREES, theta=30*DEGREES)

        cubo = Cube(side_length=2, fill_color=BLUE, fill_opacity=0.3)

        t1 = Text('Volume do cubo', color=BLUE)
        # t1.move_to(ORIGIN + DOWN*2.5 + LEFT*2.5)   
        # t1.rotate(180*DEGREES) 
        t1.to_corner(UL)

        self.play(FadeIn(cubo), FadeIn(t1))

        l1 = Text('1')
        l2 = Text('1')
        l3 = Text('1')

        l1.move_to(ORIGIN + RIGHT*3.5 + UP*1.5)
        l1.rotate(120*DEGREES)
        l2.move_to(ORIGIN + RIGHT*1 + DOWN*2)
        l2.rotate(120*DEGREES)
        l3.move_to(ORIGIN + RIGHT*1.5 + UP*2.5)
        l3.rotate(120*DEGREES)

        for n in [l1, l2, l3]:
            self.play(Create(n))