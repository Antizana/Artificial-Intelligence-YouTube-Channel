from manim import *
from manim.utils.unit import Pixels
from random import randrange


class SpiralToCircle(Scene):

    def construct(self):
        vertices1 = range(50)
        vertices2 = range(50)
        edges = [(48, 49), (3, 4)]
        g1 = Graph(vertices1, edges, layout="spiral")
        g2 = Graph(vertices2, edges, layout="circular")

        self.play(Create(g1))
        self.wait(5)
        self.play(*[g1[i].animate.move_to(g2[i]) for i in vertices1])
        self.wait()


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

        func_1 = ax.plot(
            f1,
            color=ORANGE,
        )

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


class Paradox(Scene):

    def construct(self):
        axes = (Axes(
            x_range=[0, 10, 1],
            x_length=9,
            y_range=[0, 20, 5],
            y_length=6,
            axis_config={
                "include_numbers": True,
                "include_tip": False
            },
        ).to_edge(DL).set_color(GREY))
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")

        func = axes.plot(lambda x: 0.1 * (x - 2) * (x - 5) * (x - 7) + 7,
                         x_range=[0, 10],
                         color=BLUE)

        x = ValueTracker(7)
        dx = ValueTracker(2)

        secant = always_redraw(lambda: axes.get_secant_slope_group(
            x=x.get_value(),
            graph=func,
            dx=dx.get_value(),
            dx_line_color=YELLOW,
            dy_line_color=ORANGE,
            dx_label="dx",
            dy_label="dy",
            secant_line_color=GREEN,
            secant_line_length=8,
        ))
        dot1 = always_redraw(lambda: Dot().scale(0.7).move_to(
            axes.c2p(x.get_value(), func.underlying_function(x.get_value()))))
        dot2 = always_redraw(lambda: Dot().scale(0.7).move_to(
            axes.c2p(
                (x).get_value() + dx.get_value(),
                func.underlying_function(x.get_value() + dx.get_value()),
            )))

        self.add(axes, axes_labels, func)
        self.play(Create(VGroup(dot1, dot2, secant)))
        self.play(dx.animate.set_value(0.001), run_time=8)
        self.wait(2)
        self.play(x.animate.set_value(1), run_time=5)
        self.wait()
        self.play(x.animate.set_value(7), run_time=5)
        self.wait()
        self.play(x.animate.set_value(2), run_time=5)
        self.wait()


class SubstitutionSystem(Scene):

    def construct(self):
        depth = 6
        base_s = Square(side_length=config["pixel_height"] * Pixels,
                        fill_color=WHITE,
                        fill_opacity=1,
                        stroke_width=0)
        self.add(base_s)
        fractal = VGroup(base_s)
        old_fractal = VGroup()

        for _ in range(depth):
            old_fractal = fractal.copy()
            print(fractal)
            fractal = VGroup()
            color = random_bright_color()
            for s in old_fractal:
                s_g = VGroup(*[s.copy().scale(0.5)
                               for _ in range(4)]).arrange_in_grid(cols=2,
                                                                   rows=2,
                                                                   buff=0)
                s_g[0].set_fill(color, 1)
                fractal.add(s_g)

            self.play(FadeTransform(old_fractal, fractal))


class Pith(Scene):

    def construct(self):

        sq = Square(side_length=5,
                    stroke_color=GREEN,
                    fill_color=BLUE,
                    fill_opacity=0.75)
        self.play(Create(sq), run_time=3)
        self.wait()


class SquareExample(Scene):

    def construct(self):
        square_1 = Square(side_length=2.0).shift(DOWN)
        square_2 = Square(side_length=1.0).next_to(square_1, direction=UP)
        square_3 = Square(side_length=0.5).next_to(square_2, direction=UP)
        self.add(square_1, square_2, square_3)
