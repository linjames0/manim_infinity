from manim import *

class CircleToSquare(Scene):
    def construct(self):
        # create a circe and text
        circle = Circle(color=BLUE)
        text = Text("This is a circle").next_to(circle, UP)
        
        # show circle and text
        self.play(Create(circle), Write(text))

        # wait for a moment
        self.wait(1)

        # transform circle to square
        square = Square(color=RED)
        self.play(Transform(circle, square), ReplacementTransform(text, Text("Now this is a square").next_to(square, UP)))

        # wait for a moment
        self.wait(1)

def main():
    # create a scene
    scene = CircleToSquare()

    # render the scene
    scene.render()

if __name__ == "__main__":
    main()