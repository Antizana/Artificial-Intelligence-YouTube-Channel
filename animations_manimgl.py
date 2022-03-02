from manimlib import *


class Begin(Scene):

    def construct(self):
        ax = Axes(x_range=[-2, 5, 1],
                  y_range=[-5, 5, 1],
                  x_length=12,
                  y_length=7,
                  x_axis_config={"numbers_to_include": np.arange(-2, 6, 1)},
                  y_axis_config={"numbers_to_include": np.arange(-5, 6, 1)},
                  tips=False)

        labels = ax.get_axis_labels()

        f1 = lambda x: x**3 - 4 * x**2 + 3 * x + 1

        func_1 = ax.get_graph(f1, color=ORANGE)
        # func_1 = ax.get_graph(lambda x: x**3 - 4 * x**2 + 3 * x + 1, )

        t_0 = ValueTracker(0)
        t_1 = ValueTracker(1)

        dot_0 = Dot(point=ax.coords_to_point(t_0.get_value(),
                                             f1(t_0.get_value())),
                    color=PURPLE)
        dot_1 = Dot(point=ax.coords_to_point(t_1.get_value(),
                                             f1(t_1.get_value())),
                    color=PURPLE)

        dot_0.add_updater(
            lambda x: x.move_to(ax.c2p(t_0.get_value(), f1(t_0.get_value()))))
        dot_1.add_updater(
            lambda x: x.move_to(ax.c2p(t_1.get_value(), f1(t_1.get_value()))))

        line_0 = Line(dot_0.get_center(), dot_1.get_center(),
                      color=PURPLE).scale(4)
        line_0.add_updater(lambda z: z.become(
            Line(dot_0.get_center(), dot_1.get_center()).scale(4)))

        self.play(FadeIn(ax, func_1, dot_0, dot_1, line_0))
        self.play(t_1.animate.set_value(0.5))
        self.wait()


class Pith(Scene):

    def construct(self):

        sq = Square(side_length=1,
                    stroke_color=GREEN,
                    fill_color=BLUE,
                    fill_opacity=0.75)
        self.play(ShowCreation(sq), run_time=5)
        self.wait()
