from manim import *
import manim as mn
from manim.animation import creation as cr
from manim.mobject import geometry as geom
from manim.mobject.svg import tex_mobject as txt
from manim.mobject.geometry import ArrowTriangleTip


class Pith(Scene):

    def construct(self):

        sq = Square(side_length=5,
                    stroke_color=GREEN,
                    fill_color=BLUE,
                    fill_opacity=0.75)
        self.play(Create(sq), run_time=3)
        self.wait()


class Testing(Scene):

    def construct(self):
        name = txt.Tex("Antizana").to_edge(UL, buff=0.5)
        sq = geom.Square(side_length=0.5, fill_color=GREEN,
                         fill_opacity=0.75).shift(LEFT * 3)
        tri = geom.Triangle().scale(0.6).to_edge(DR)

        self.play(cr.Write(name))
        self.play(cr.DrawBorderThenFill(sq), run_time=2)
        self.play(cr.Create(tri))
        self.wait()

        self.play(name.animate.to_edge(UR), run_time=2)
        self.play(sq.animate.scale(2), tri.animate.to_edge(DL), run_time=3)
        self.wait()


class Errors(Scene):

    def construct(self):
        c = Circle(radius=2)
        self.play(Write(c))


class Getters(Scene):

    def construct(self):
        rect = Rectangle(color=WHITE, height=3, width=2.5).to_edge(UL)
        circ = Circle().to_edge(DOWN)
        arrow = always_redraw(lambda: Line(
            start=rect.get_bottom(), end=circ.get_top(), buff=0.2).add_tip())
        self.play(Create(VGroup(rect, circ, arrow)))
        self.wait()
        self.play(rect.animate.to_edge(UR),
                  circ.animate.scale(0.5),
                  run_time=4)


class Updaters(Scene):

    def construct(self):
        num = MathTex("ln(2)")
        box = SurroundingRectangle(num,
                                   color=BLUE,
                                   fill_opacity=0.4,
                                   fill_color=RED,
                                   buff=2)
        name = Tex("Amazonas").next_to(box, DOWN, buff=0.25)
        self.play(Create(VGroup(num, box, name)))
        self.wait()


class Updaters1(Scene):

    def construct(self):
        num = MathTex("ln(2)")
        box = SurroundingRectangle(num,
                                   color=BLUE,
                                   fill_opacity=0.4,
                                   fill_color=RED,
                                   buff=0.5)
        name = Tex("Amazonas").next_to(box, DOWN, buff=0.25)
        self.play(Create(VGroup(num, box, name)))
        self.play(num.animate.shift(RIGHT * 2), run_time=2)
        self.wait()


class Updaters2(Scene):

    def construct(self):
        num = MathTex("ln(2)")
        box = always_redraw(lambda: SurroundingRectangle(
            num, color=BLUE, fill_opacity=0.4, fill_color=RED, buff=0.5))
        name = always_redraw(
            lambda: Tex("Amazonas").next_to(box, DOWN, buff=0.25))
        self.play(Create(VGroup(num, box, name)))
        self.play(num.animate.shift(RIGHT * 2), run_time=2)
        self.wait()


class ValueTrackers(Scene):

    def construct(self):
        # k = ValueTracker(0)
        k = ValueTracker(5)
        num = always_redraw(lambda: DecimalNumber().set_value(k.get_value()))

        self.play(FadeIn(num))
        self.wait()
        # self.play(k.animate.set_value(0), run_time=5, rate_func=linear)
        self.play(k.animate.set_value(0), run_time=5, rate_func=smooth)


class Graphing(Scene):

    def construct(self):
        # plane = NumberPlane(x_range=[-4, 4, 2],
        #                     x_length=7,
        #                     y_range=[0, 16, 4],
        #                     y_length=8).to_edge(DOWN)
        plane = NumberPlane(x_range=[-4, 4, 2],
                            x_length=7,
                            y_range=[0, 16, 4],
                            y_length=6).to_edge(DOWN).add_coordinates()
        labels = plane.get_axis_labels(x_label="x", y_label="f(x)")
        parab = plane.plot(lambda x: x**2, x_range=[-4, 4], color=GREEN)
        func_label = MathTex("f(x)={x}^{2}").scale(0.6).next_to(
            parab, RIGHT, buff=0.2).set_color(GREEN)
        area = plane.get_riemann_rectangles(graph=parab,
                                            x_range=[-2, 3],
                                            dx=0.001,
                                            stroke_width=0.1,
                                            stroke_color=WHITE)
        self.play(DrawBorderThenFill(plane))
        # self.play(Create(parab))
        self.play(Create(VGroup(labels, parab, func_label)))
        self.wait()
        self.play(Create(area))
        self.wait()


class UpdaterGraphing(Scene):

    def construct(self):
        ax = Axes(x_range=[-4, 4, 1],
                  y_range=[-2, 16, 2],
                  x_length=10,
                  y_length=6).to_edge(DOWN)
        func = ax.plot(lambda x: x**2, x_range=[-4, 4], color=BLUE)
        slope = ax.get_secant_slope_group(x=3,
                                          graph=func,
                                          dx=0.01,
                                          secant_line_length=3)
        self.add(ax, func, slope)
        self.wait()


class UpdaterGraphing2(Scene):

    def construct(self):
        k = ValueTracker(-4)
        ax = (Axes(
            x_range=[-4, 4, 1], y_range=[-2, 16, 2], x_length=10,
            y_length=7).to_edge(DOWN).add_coordinates()).set_color(WHITE)
        func = ax.plot(lambda x: x**2, x_range=[-4, 4], color=BLUE)
        slope = always_redraw(
            lambda: ax.get_secant_slope_group(x=k.get_value(),
                                              graph=func,
                                              dx=0.01,
                                              secant_line_color=GREEN,
                                              secant_line_length=3))
        self.add(ax, func, slope)
        self.wait()
        self.play(k.animate.set_value(4), run_time=3)


class UpdaterGraphing3(Scene):

    def construct(self):
        k = ValueTracker(-4)
        ax = (Axes(
            x_range=[-4, 4, 1], y_range=[-2, 16, 2], x_length=10,
            y_length=7).to_edge(DOWN).add_coordinates()).set_color(WHITE)
        func = ax.plot(lambda x: x**2, x_range=[-4, 4], color=BLUE)
        slope = always_redraw(
            lambda: ax.get_secant_slope_group(x=k.get_value(),
                                              graph=func,
                                              dx=0.01,
                                              secant_line_color=GREEN,
                                              secant_line_length=3))
        pt = always_redraw(lambda: Dot().move_to(
            ax.c2p(k.get_value(), func.underlying_function(k.get_value()))))
        self.add(ax, func, slope, pt)
        self.wait()
        self.play(k.animate.set_value(4), run_time=3)


HOME1 = r"C:\Users\Dell\Documents\Marketing Digital\Youtube\TensorFlow\AI\ai_dictionary\Resources\Images"
HOME2 = r"C:\Users\Dell\Documents\Marketing Digital\Youtube\TensorFlow\AI\ai_dictionary\Resources\SVG_Images"


class SVGs(Scene):

    def construct(self):
        icon = SVGMobject(f"{HOME2}\\youtube.svg").to_edge(LEFT)
        im = ImageMobject(f"{HOME1}\\ducky.jpg").to_edge(DR).scale(0.3)
        self.play(DrawBorderThenFill(icon))
        self.wait()
        self.play(FadeIn(im))


class Test(Scene):

    def construct(self):
        ax = Axes(
            x_range=[0, 10, 2],
            y_range=[0, 10, 2],
            x_length=7,
            y_length=7,
            axis_config={
                "include_numbers": True,
                "font_size": 30,
                "include_tip": True,
                "numbers_to_exclude": [0],
                "numbers_with_elongated_ticks": [0, 2],
            },
        )
        self.add(ax)
        self.wait()


class PlotExample(Scene):

    def construct(self):
        # construct the axes
        ax_1 = Axes(
            x_range=[0.001, 6],
            y_range=[-8, 2],
            x_length=5,
            y_length=3,
            tips=False,
        )
        ax_2 = ax_1.copy()
        ax_3 = ax_1.copy()

        # position the axes
        ax_1.to_corner(UL)
        ax_2.to_corner(UR)
        ax_3.to_edge(DOWN)
        axes = VGroup(ax_1, ax_2, ax_3)

        # create the logarithmic curves
        def log_func(x):
            return np.log(x)

        # a curve without adjustments; poor interpolation.
        curve_1 = ax_1.plot(log_func, color=PURE_RED)

        # disabling interpolation makes the graph look choppy as not enough
        # inputs are available
        curve_2 = ax_2.plot(log_func, use_smoothing=False, color=ORANGE)

        # taking more inputs of the curve by specifying a step for the
        # x_range yields expected results, but increases rendering time.
        curve_3 = ax_3.plot(log_func,
                            x_range=(0.001, 6, 0.001),
                            color=PURE_GREEN)

        curves = VGroup(curve_1, curve_2, curve_3)

        self.add(axes, curves)


class ImplicitFunctionExample(Scene):

    def construct(self):
        graph = ImplicitFunction(lambda x, y: x * y**2 - x**2 * y - 2,
                                 color=YELLOW)
        self.add(NumberPlane(), graph)