from manim import *

class Infinity(Scene):
    def construct(self):

        def leminiscate(t):
            x = np.sin(t)
            y = np.sin(t) * np.cos(t)
            return x * RIGHT + y * UP
        
        # create infinity
        infinity = ParametricFunction(leminiscate, t_range=(-PI, PI), color=BLUE)
        infinity.scale(0.8)

        # create text
        text = Text("Infinity").scale(0.8).next_to(infinity, UP)

        sigil_text = Text("James Lin = ...").scale(0.8).next_to(text, ORIGIN)

        # create dot
        dot = Dot().move_to(ORIGIN)

        # show Sigil text
        self.play(Write(sigil_text))
        self.wait(1.5)

        # transform to infinity
        self.play(Transform(sigil_text, infinity), Write(text))
        self.wait(1)

        # move dot along infinity
        self.play(MoveAlongPath(dot, infinity), run_time=2)
        self.wait(1)

if __name__ == "__main__":
    Infinity().render()

