from manim import *

class Test(Scene):
    def construct(self):
        circle = Circle(radius=1, color=BLUE)
        circle.set_fill(BLUE)


        square = Square(side_length=2, color=RED)
        square.set_fill(RED)

        test = Text("test")
        test2 = Text(r'\lambda')

        self.play(Create(circle))
        self.play(Transform(circle, square))
        self.play(Transform(square, test2))
        self.wait(1)
