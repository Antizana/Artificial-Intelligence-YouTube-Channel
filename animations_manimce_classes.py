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


class SquareToCircle(Scene):

    def construct(self):
        circle = Circle()
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        circle.set_fill(PINK, opacity=0.5)

        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))


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


class Formula(Scene):
    """ MathTex example """

    def construct(self):
        t = MathTex(r"\int_a^b f'(x) dx = f(b)- f(a)")
        self.add(t)

        self.play(cr.Create(t), run_time=5)
        self.wait()
        self.play(cr.Write(t), run_time=5)


class BulletedListExample(Scene):
    """ BulletedList example """

    def construct(self):
        blist = BulletedList("Item 1", "Item 2", "Item 3", height=2, width=2)
        blist.set_color_by_tex("Item 1", RED)
        blist.set_color_by_tex("Item 2", GREEN)
        blist.set_color_by_tex("Item 3", BLUE)
        self.add(blist)

        self.play(cr.Write(blist), run_time=5)


class TitleExample(Scene):
    """ Title example """

    def construct(self):
        banner = ManimBanner()
        title = Title(f"Manim version {mn.__version__}")
        # self.add(banner, title)

        self.play(cr.Create(banner), run_time=5)
        self.play(cr.Write(title))
        self.wait()


class DarkThemeBanner(Scene):
    """ ManimBanner example DarkTheme """

    def construct(self):
        banner = ManimBanner()
        self.play(banner.create())
        self.play(banner.expand())
        self.wait()
        self.play(Unwrite(banner))
        self.wait()


class LightThemeBanner(Scene):
    """ ManimBanner example LightThemeBanner """

    def construct(self):
        self.camera.background_color = "#ece6e2"
        banner = ManimBanner(dark_theme=False)
        self.play(banner.create())
        self.play(banner.expand())
        self.wait()
        self.play(Unwrite(banner))
        self.wait()


class ExpandDirections(Scene):
    """ Expand Manim Logo example """

    def construct(self):
        banners = [ManimBanner().scale(0.5).shift(UP * x) for x in [-2, 0, 2]]
        self.play(
            banners[0].expand(direction="right"),
            banners[1].expand(direction="center"),
            banners[2].expand(direction="left"),
        )
        self.wait()


class UsefulAnnotations(Scene):
    """ Geometry Module Examples """

    def construct(self):
        m0 = Dot()
        m1 = AnnotationDot()
        m2 = LabeledDot("ii")
        m3 = LabeledDot(MathTex(r"\alpha").set_color(ORANGE))
        m4 = CurvedArrow(2 * LEFT, 2 * RIGHT, radius=-5)
        m5 = CurvedArrow(2 * LEFT, 2 * RIGHT, radius=8)
        m6 = CurvedDoubleArrow(ORIGIN, 2 * RIGHT)

        self.add(m0, m1, m2, m3, m4, m5, m6)
        for i, mobj in enumerate(self.mobjects):
            mobj.shift(DOWN * (i - 3))


class ArcExample(Scene):
    """ Geometry Arc Example """

    def construct(self):
        self.add(Arc(angle=PI))


class ArcBetweenPointsExample(Scene):
    """ Arc Between Points Example """

    def construct(self):
        circle = Circle(radius=2, stroke_color=GREY)
        dot_1 = Dot(color=GREEN).move_to([2, 0, 0]).scale(0.5)
        dot_1_text = Tex("(2,0)").scale(0.5).next_to(dot_1,
                                                     RIGHT).set_color(BLUE)
        dot_2 = Dot(color=GREEN).move_to([0, 2, 0]).scale(0.5)
        dot_2_text = Tex("(0,2)").scale(0.5).next_to(dot_2, UP).set_color(BLUE)
        arc = ArcBetweenPoints(start=2 * RIGHT,
                               end=2 * UP,
                               stroke_color=YELLOW)
        self.add(circle, dot_1, dot_2, dot_1_text, dot_2_text)
        self.play(Create(arc))


class CircleExample(Scene):
    """ Circle Example """

    def construct(self):
        circle_1 = Circle(radius=1.0)
        circle_2 = Circle(radius=1.5, color=GREEN)
        circle_3 = Circle(radius=1.0, color=BLUE_B, fill_opacity=1)

        circle_group = Group(circle_1, circle_2, circle_3).arrange(buff=1)
        self.add(circle_group)
        self.wait(3)
        self.remove(circle_group)
        self.wait()

        circle_vgroup = VGroup(circle_1, circle_2, circle_3).arrange(buff=1)

        self.play(cr.Create(circle_vgroup, run_time=5))
        self.wait()


class CircleSurround(Scene):
    """ CircleSurround Example """

    def construct(self):
        triangle1 = Triangle()
        circle1 = Circle().surround(triangle1)
        group1 = Group(triangle1, circle1)  # treat the two mobjects as one

        line2 = Line()
        circle2 = Circle().surround(line2, buffer_factor=2.0)
        # circle2 = Circle().surround(line2)
        group2 = Group(line2, circle2)

        # buffer_factor < 1, so the circle is smaller than the square
        square3 = Square()
        circle3 = Circle().surround(square3, buffer_factor=0.5)
        group3 = Group(square3, circle3)

        group = Group(group1, group2, group3).arrange(buff=1)

        self.wait()
        self.add(group)
        self.wait(3)
        self.remove(group)
        self.wait()

        vgroup = VGroup(triangle1, circle1, line2, circle2, square3, circle3)
        self.play(cr.Create(vgroup), run_time=7)
        self.wait()


class PointAtAngleExample(Scene):
    """ PointAtAngle Example """

    def construct(self):
        circle = Circle(radius=2.0)
        p1 = circle.point_at_angle(PI / 2)
        p2 = circle.point_at_angle(270 * DEGREES)

        s1 = Square(side_length=0.25).move_to(p1)
        s2 = Square(side_length=0.25).move_to(p2)
        vgroup = VGroup(circle, s1, s2)

        self.wait()
        self.add(circle, s1, s2)
        self.wait(2)
        self.remove(circle, s1, s2)

        self.wait()
        self.play(cr.Create(vgroup), run_time=5)
        self.wait()


class CircleFromPointsExample(Scene):
    """" CircleFromPoints Example"""

    def construct(self):
        circle = Circle.from_three_points(LEFT, LEFT + UP, UP * 2, color=RED)
        dots = VGroup(
            Dot(LEFT),
            Dot(LEFT + UP),
            Dot(UP * 2),
        )
        vgroup = VGroup(dots, circle)
        # self.add(NumberPlane(), circle, dots)
        self.wait()
        self.remove(NumberPlane(), circle, dots)
        self.wait()
        self.play(cr.Create(NumberPlane()))
        self.play(cr.Create(vgroup), run_time=5)
        self.wait()


class DotExample(Scene):
    """ Dot Example """

    def construct(self):
        # dot1 = Dot(point=LEFT, radius=0.08)
        dot1 = Dot(point=LEFT, radius=0.25)
        dot2 = Dot(point=ORIGIN)
        dot3 = Dot(point=RIGHT)
        self.add(dot1, dot2, dot3)


class SeveralLabeledDots(Scene):
    """ LaveledDot Example """

    def construct(self):
        sq = Square(fill_color=RED, fill_opacity=1)
        self.add(sq)
        dot1 = LabeledDot(Tex("42", color=RED))
        dot2 = LabeledDot(MathTex("a", color=GREEN))
        dot3 = LabeledDot(Text("ii", color=BLUE))
        dot4 = LabeledDot("3")
        dot1.next_to(sq, UL)
        dot2.next_to(sq, UR)
        dot3.next_to(sq, DL)
        dot4.next_to(sq, DR)
        self.add(dot1, dot2, dot3, dot4)


class EllipseExample(Scene):
    """ Ellipse Example """

    def construct(self):
        ellipse_1 = Ellipse(width=2.0, height=4.0, color=BLUE_B)
        ellipse_2 = Ellipse(width=4.0, height=1.0, color=BLUE_D)
        ellipse_group = Group(ellipse_1, ellipse_2).arrange(buff=1)
        self.add(ellipse_group)


class AnnularSectorExample(Scene):
    """ AnularSector Example """

    def construct(self):
        # Changes background color to clearly visualize changes in fill_opacity.
        # self.camera.background_color = WHITE

        # The default parameter start_angle is 0, so the AnnularSector starts from the +x-axis.
        s1 = AnnularSector(color=YELLOW).move_to(2 * UL)

        # Different inner_radius and outer_radius than the default.
        s2 = AnnularSector(inner_radius=1.5,
                           outer_radius=2,
                           angle=45 * DEGREES,
                           color=RED).move_to(2 * UR)

        # fill_opacity is typically a number > 0 and <= 1. If fill_opacity=0, the AnnularSector is transparent.
        s3 = AnnularSector(inner_radius=1,
                           outer_radius=1.5,
                           angle=PI,
                           fill_opacity=0.25,
                           color=BLUE).move_to(2 * DL)

        # With a negative value for the angle, the AnnularSector is drawn clockwise from the start value.
        s4 = AnnularSector(inner_radius=1,
                           outer_radius=1.5,
                           angle=-3 * PI / 2,
                           color=GREEN).move_to(2 * DR)

        self.add(s1, s2, s3, s4)


class ExampleSector(Scene):
    """ Sector Example """

    def construct(self):
        sector = Sector(outer_radius=2, inner_radius=1)
        sector2 = Sector(outer_radius=2.5,
                         inner_radius=0.8).move_to([-3, 0, 0])
        sector.set_color(RED)
        sector2.set_color(PINK)
        self.add(sector, sector2)


class AnnulusExample(Scene):
    """ Anulus Example """

    def construct(self):
        annulus_1 = Annulus(inner_radius=0.5, outer_radius=1).shift(UP)
        annulus_2 = Annulus(inner_radius=0.3, outer_radius=0.6,
                            color=RED).next_to(annulus_1, DOWN)
        self.add(annulus_1, annulus_2)


class LineExample(Scene):
    """ Line Example """

    def construct(self):
        d = VGroup()
        for i in range(0, 10):
            d.add(Dot())
        d.arrange_in_grid(buff=1)
        self.add(d)
        l = Line(d[0], d[1])
        self.add(l)
        self.wait()
        l.put_start_and_end_on(d[1].get_center(), d[2].get_center())
        self.wait()
        l.put_start_and_end_on(d[4].get_center(), d[7].get_center())
        self.wait()


class ExampleBoxes(Scene):
    """ arrange_in_grid Example """

    def construct(self):
        boxes = VGroup(*[Square() for s in range(0, 6)])
        boxes.arrange_in_grid(rows=2, buff=0.1)
        self.add(boxes)


class ArrangeInGrid(Scene):
    """ arrange_in_grid Example """

    def construct(self):
        #Add some numbered boxes:
        np.random.seed(3)
        boxes = VGroup(*[
            Rectangle(WHITE,
                      np.random.random() + .5,
                      np.random.random() +
                      .5).add(Text(str(i + 1)).scale(0.5)) for i in range(22)
        ])
        self.add(boxes)

        boxes.arrange_in_grid(buff=(0.25, 0.5),
                              col_alignments="lccccr",
                              row_alignments="uccd",
                              col_widths=[2, *[None] * 4, 2],
                              flow_order="dr")


class DashedLineExample(Scene):
    """ DashedLine Example """

    def construct(self):
        # dash_length increased
        dashed_0 = DashedLine(config.left_side,
                              config.right_side,
                              dash_length=0.5).shift(UP * 2.5)
        dashed_1 = DashedLine(config.left_side,
                              config.right_side,
                              dash_length=2.0).shift(UP * 2)
        # normal
        dashed_2 = DashedLine(config.left_side, config.right_side)
        # dashed_ratio decreased
        dashed_3 = DashedLine(config.left_side,
                              config.right_side,
                              dashed_ratio=0.1).shift(DOWN * 2)
        dashed_4 = DashedLine(config.left_side,
                              config.right_side,
                              dashed_ratio=0.2).shift(DOWN * 2.5)
        self.add(dashed_0, dashed_1, dashed_2, dashed_3, dashed_4)


class TangentLineExample(Scene):
    """ TangentLine Example """

    def construct(self):
        circle = Circle(radius=2)
        line_1 = TangentLine(circle, alpha=0.0, length=4,
                             color=BLUE_D)  # right
        line_2 = TangentLine(circle, alpha=0.4, length=4,
                             color=GREEN)  # top left
        self.add(circle, line_1, line_2)


class ElbowExample(Scene):
    """ Elbow Example """

    def construct(self):
        elbow_1 = Elbow()
        elbow_2 = Elbow(width=2.0)
        elbow_3 = Elbow(width=2.0, angle=5 * PI / 4)

        elbow_group = Group(elbow_1, elbow_2, elbow_3).arrange(buff=1)
        self.add(elbow_group)


class ArrowExample(Scene):
    """ Arrow Example """

    def construct(self):
        arrow_1 = Arrow(start=RIGHT, end=LEFT, color=GOLD)
        arrow_2 = Arrow(start=RIGHT,
                        end=LEFT,
                        color=GOLD,
                        tip_shape=ArrowSquareTip).shift(DOWN)
        g1 = Group(arrow_1, arrow_2)

        # the effect of buff
        square = Square(color=MAROON_A)
        arrow_3 = Arrow(start=LEFT, end=RIGHT)
        arrow_4 = Arrow(start=LEFT, end=RIGHT, buff=0).next_to(arrow_1, UP)
        g2 = Group(arrow_3, arrow_4, square)

        # a shorter arrow has a shorter tip and smaller stroke width
        arrow_5 = Arrow(start=ORIGIN, end=config.top).shift(LEFT * 4)
        arrow_6 = Arrow(start=config.top + DOWN,
                        end=config.top).shift(LEFT * 3)
        g3 = Group(arrow_5, arrow_6)

        self.add(Group(g1, g2, g3).arrange(buff=2))


class ArrowExample2(Scene):
    """" Arrow Example """

    def construct(self):
        left_group = VGroup()
        # As buff increases, the size of the arrow decreases.
        for buff in np.arange(0, 2.2, 0.45):
            left_group += Arrow(buff=buff, start=2 * LEFT, end=2 * RIGHT)
        # Required to arrange arrows.
        left_group.arrange(DOWN)
        left_group.move_to(4 * LEFT)

        middle_group = VGroup()
        # As max_stroke_width_to_length_ratio gets bigger,
        # the width of stroke increases.
        for i in np.arange(0, 5, 0.5):
            middle_group += Arrow(max_stroke_width_to_length_ratio=i)
        middle_group.arrange(DOWN)

        UR_group = VGroup()
        # As max_tip_length_to_length_ratio increases,
        # the length of the tip increases.
        for i in np.arange(0, 0.3, 0.1):
            UR_group += Arrow(max_tip_length_to_length_ratio=i)
        UR_group.arrange(DOWN)
        UR_group.move_to(4 * RIGHT + 2 * UP)

        DR_group = VGroup()
        DR_group += Arrow(start=LEFT,
                          end=RIGHT,
                          color=BLUE,
                          tip_shape=ArrowSquareTip)
        DR_group += Arrow(start=LEFT,
                          end=RIGHT,
                          color=BLUE,
                          tip_shape=ArrowSquareFilledTip)
        DR_group += Arrow(start=LEFT,
                          end=RIGHT,
                          color=YELLOW,
                          tip_shape=ArrowCircleTip)
        DR_group += Arrow(start=LEFT,
                          end=RIGHT,
                          color=YELLOW,
                          tip_shape=ArrowCircleFilledTip)
        DR_group.arrange(DOWN)
        DR_group.move_to(4 * RIGHT + 2 * DOWN)

        self.add(left_group, middle_group, UR_group, DR_group)


class VectorExample(Scene):
    """ Vector Example """

    def construct(self):
        plane = NumberPlane()
        vector_1 = Vector([1, 2])
        vector_2 = Vector([-5, -2])
        self.add(plane, vector_1, vector_2)


class VectorCoordinateLabel(Scene):

    def construct(self):
        plane = NumberPlane()

        vec_1 = Vector([1, 2])
        vec_2 = Vector([-3, -2])
        label_1 = vec_1.coordinate_label()
        label_2 = vec_2.coordinate_label(color=YELLOW)

        self.add(plane, vec_1, vec_2, label_1, label_2)


class DoubleArrowExample(Scene):

    def construct(self):
        circle = Circle(radius=2.0)
        d_arrow = DoubleArrow(start=circle.get_left(), end=circle.get_right())
        d_arrow_2 = DoubleArrow(tip_shape_end=ArrowCircleFilledTip,
                                tip_shape_start=ArrowCircleFilledTip)
        group = Group(Group(circle, d_arrow), d_arrow_2).arrange(UP, buff=1)
        self.add(group)


class DoubleArrowExample2(Scene):

    def construct(self):
        box = Square()
        p1 = box.get_left()
        p2 = box.get_right()
        d1 = DoubleArrow(p1, p2, buff=0)
        d2 = DoubleArrow(p1, p2, buff=0, tip_length=0.2, color=YELLOW)
        d3 = DoubleArrow(p1, p2, buff=0, tip_length=0.4, color=BLUE)
        Group(d1, d2, d3).arrange(DOWN)
        self.add(box, d1, d2, d3)


class BezierSplineExample(Scene):

    def construct(self):
        p1 = np.array([-3, 1, 0])
        p1b = p1 + [1, 0, 0]
        d1 = Dot(point=p1).set_color(BLUE)
        l1 = Line(p1, p1b, stroke_color=YELLOW)
        p2 = np.array([3, -1, 0])
        p2b = p2 - [1, 0, 0]
        d2 = Dot(point=p2).set_color(RED)
        l2 = Line(p2, p2b, stroke_color=YELLOW)
        bezier = CubicBezier(p1b,
                             p1b + 3 * RIGHT,
                             p2b - 3 * RIGHT,
                             p2b,
                             stroke_color=WHITE)
        self.add(l1, d1, l2, d2, bezier)


class PolygramExample(Scene):

    def construct(self):
        hexagram = Polygram(
            [[0, 2, 0], [-np.sqrt(3), -1, 0], [np.sqrt(3), -1, 0]],
            [[-np.sqrt(3), 1, 0], [0, -2, 0], [np.sqrt(3), 1, 0]],
        )
        self.add(hexagram)

        dot = Dot()
        self.play(MoveAlongPath(dot, hexagram), run_time=5, rate_func=linear)
        self.remove(dot)
        self.wait()


class PolygramRoundCorners(Scene):

    def construct(self):
        star = Star(outer_radius=2)

        shapes = VGroup(star)
        shapes.add(star.copy().round_corners(radius=0.1))
        shapes.add(star.copy().round_corners(radius=0.25))

        shapes.arrange(RIGHT)
        self.add(shapes)


class PolygonExample(Scene):

    def construct(self):
        isosceles = Polygon([-5, 1.5, 0], [-2, 1.5, 0], [-3.5, -2, 0])
        position_list = [
            [4, 1, 0],  # middle right
            [4, -2.5, 0],  # bottom right
            [0, -2.5, 0],  # bottom left
            [0, 3, 0],  # top left
            [2, 1, 0],  # middle
            [4, 3, 0],  # top right
        ]
        square_and_triangles = Polygon(*position_list, color=PURPLE_B)
        self.add(isosceles, square_and_triangles)


class RegularPolygramExample(Scene):

    def construct(self):
        pentagram = RegularPolygram(5, radius=2)
        decagram = RegularPolygram(10, radius=1)
        self.add(pentagram.move_to(LEFT * 2))
        self.wait()
        self.add(decagram.move_to(RIGHT * 2))
        self.wait()


class RegularPolygonExample(Scene):

    def construct(self):
        poly_1 = RegularPolygon(n=6)
        poly_2 = RegularPolygon(n=6, start_angle=30 * DEGREES, color=GREEN)
        poly_3 = RegularPolygon(n=10, color=RED)

        poly_group = Group(poly_1, poly_2, poly_3).scale(1.5).arrange(buff=1)
        self.add(poly_group)


class StarExample(Scene):

    def construct(self):
        pentagram = RegularPolygram(5, radius=2)
        star = Star(outer_radius=2, color=RED)

        self.add(pentagram)
        self.play(Create(star), run_time=3)
        self.play(FadeOut(star), run_time=2)


class DifferentDensitiesExample(Scene):

    def construct(self):
        density_2 = Star(7, outer_radius=2, density=2, color=RED)
        density_3 = Star(7, outer_radius=2, density=3, color=PURPLE)

        self.add(VGroup(density_2, density_3).arrange(RIGHT))


class SeveralArcPolygons(Scene):

    def construct(self):
        a = [0, 0, 0]
        b = [2, 0, 0]
        c = [0, 2, 0]
        ap1 = ArcPolygon(a, b, c, radius=2)
        ap2 = ArcPolygon(a, b, c, angle=45 * DEGREES)
        ap3 = ArcPolygon(a, b, c, arc_config={'radius': 1.7, 'color': RED})
        ap4 = ArcPolygon(a,
                         b,
                         c,
                         color=RED,
                         fill_opacity=1,
                         arc_config=[{
                             'radius': 1.7,
                             'color': RED
                         }, {
                             'angle': 20 * DEGREES,
                             'color': BLUE
                         }, {
                             'radius': 1
                         }])
        ap_group = VGroup(ap1, ap2, ap3, ap4).arrange()
        self.play(*[Create(ap) for ap in [ap1, ap2, ap3, ap4]])
        self.wait()


class ArcPolygonExample(Scene):

    def construct(self):
        arc_conf = {"stroke_width": 0}
        poly_conf = {
            "stroke_width": 10,
            "stroke_color": BLUE,
            "fill_opacity": 1,
            "color": PURPLE
        }
        a = [-1, 0, 0]
        b = [1, 0, 0]
        c = [0, np.sqrt(3), 0]
        arc0 = ArcBetweenPoints(a, b, radius=2, **arc_conf)
        arc1 = ArcBetweenPoints(b, c, radius=2, **arc_conf)
        arc2 = ArcBetweenPoints(c, a, radius=2, **arc_conf)
        reuleaux_tri = ArcPolygonFromArcs(arc0, arc1, arc2, **poly_conf)
        self.play(FadeIn(reuleaux_tri))
        self.wait(2)


class ArcPolygonExample2(Scene):

    def construct(self):
        arc_conf = {
            "stroke_width": 3,
            "stroke_color": BLUE,
            "fill_opacity": 0.5,
            "color": GREEN
        }
        poly_conf = {"color": None}
        a = [-1, 0, 0]
        b = [1, 0, 0]
        c = [0, np.sqrt(3), 0]
        arc0 = ArcBetweenPoints(a, b, radius=2, **arc_conf)
        arc1 = ArcBetweenPoints(b, c, radius=2, **arc_conf)
        arc2 = ArcBetweenPoints(c, a, radius=2, stroke_color=RED)
        reuleaux_tri = ArcPolygonFromArcs(arc0, arc1, arc2, **poly_conf)
        self.play(FadeIn(reuleaux_tri))
        self.wait(2)


class TriangleExample(Scene):

    def construct(self):
        triangle_1 = Triangle()
        triangle_2 = Triangle().scale(2).rotate(60 * DEGREES)
        tri_group = Group(triangle_1, triangle_2).arrange(buff=1)
        self.add(tri_group)


class RectangleExample(Scene):

    def construct(self):
        rect1 = Rectangle(width=4.0,
                          height=2.0,
                          grid_xstep=1.0,
                          grid_ystep=0.5)
        rect2 = Rectangle(width=1.0, height=4.0)

        rects = Group(rect1, rect2).arrange(buff=1)
        self.add(rects)


class SquareExample(Scene):

    def construct(self):
        square_1 = Square(side_length=2.0).shift(DOWN)
        square_2 = Square(side_length=1.0).next_to(square_1, direction=UP)
        square_3 = Square(side_length=0.5).next_to(square_2, direction=UP)
        self.add(square_1, square_2, square_3)


class RoundedRectangleExample(Scene):

    def construct(self):
        rect_1 = RoundedRectangle(corner_radius=0.5)
        rect_2 = RoundedRectangle(corner_radius=1.5, height=4.0, width=4.0)

        rect_group = Group(rect_1, rect_2).arrange(buff=1)
        self.add(rect_group)


class ArrowTipsShowcase(Scene):

    def construct(self):
        a00 = Arrow(start=[-2, 3, 0], end=[2, 3, 0], color=YELLOW)
        a11 = Arrow(start=[-2, 2, 0],
                    end=[2, 2, 0],
                    tip_shape=ArrowTriangleTip)
        a12 = Arrow(start=[-2, 1, 0], end=[2, 1, 0])
        a21 = Arrow(start=[-2, 0, 0], end=[2, 0, 0], tip_shape=ArrowSquareTip)
        a22 = Arrow([-2, -1, 0], [2, -1, 0], tip_shape=ArrowSquareFilledTip)
        a31 = Arrow([-2, -2, 0], [2, -2, 0], tip_shape=ArrowCircleTip)
        a32 = Arrow([-2, -3, 0], [2, -3, 0], tip_shape=ArrowCircleFilledTip)
        b11 = a11.copy().scale(0.5, scale_tips=True).next_to(a11, RIGHT)
        b12 = a12.copy().scale(0.5, scale_tips=True).next_to(a12, RIGHT)
        b21 = a21.copy().scale(0.5, scale_tips=True).next_to(a21, RIGHT)
        self.add(a00, a11, a12, a21, a22, a31, a32, b11, b12, b21)


class CutoutExample(Scene):

    def construct(self):
        s1 = Square().scale(2.5)
        s2 = Triangle().shift(DOWN + RIGHT).scale(0.5)
        s3 = Square().shift(UP + RIGHT).scale(0.5)
        s4 = RegularPolygon(5).shift(DOWN + LEFT).scale(0.5)
        s5 = RegularPolygon(6).shift(UP + LEFT).scale(0.5)
        c = Cutout(s1,
                   s2,
                   s3,
                   s4,
                   s5,
                   fill_opacity=1,
                   color=BLUE,
                   stroke_color=RED)
        self.play(Write(c), run_time=4)
        self.wait()


class RightArcAngleExample(Scene):

    def construct(self):
        line1 = Line(LEFT, RIGHT)
        line2 = Line(DOWN, UP)
        rightarcangles = [
            Angle(line1, line2, dot=True),
            Angle(line1,
                  line2,
                  radius=0.4,
                  quadrant=(1, -1),
                  dot=True,
                  other_angle=True),
            Angle(line1,
                  line2,
                  radius=0.5,
                  quadrant=(-1, 1),
                  stroke_width=8,
                  dot=True,
                  dot_color=YELLOW,
                  dot_radius=0.04,
                  other_angle=True),
            Angle(line1,
                  line2,
                  radius=0.7,
                  quadrant=(-1, -1),
                  color=RED,
                  dot=True,
                  dot_color=GREEN,
                  dot_radius=0.08),
        ]
        plots = VGroup()
        for angle in rightarcangles:
            plot = VGroup(line1.copy(), line2.copy(), angle)
            plots.add(plot)
        plots.arrange(buff=1.5)
        self.add(plots)


class AngleExample(Scene):

    def construct(self):
        line1 = Line(LEFT + (1 / 3) * UP, RIGHT + (1 / 3) * DOWN)
        line2 = Line(DOWN + (1 / 3) * RIGHT, UP + (1 / 3) * LEFT)
        angles = [
            Angle(line1, line2),
            Angle(line1, line2, radius=0.4, quadrant=(1, -1),
                  other_angle=True),
            Angle(line1,
                  line2,
                  radius=0.5,
                  quadrant=(-1, 1),
                  stroke_width=8,
                  other_angle=True),
            Angle(line1, line2, radius=0.7, quadrant=(-1, -1), color=RED),
            Angle(line1, line2, other_angle=True),
            Angle(line1, line2, radius=0.4, quadrant=(1, -1)),
            Angle(line1, line2, radius=0.5, quadrant=(-1, 1), stroke_width=8),
            Angle(line1,
                  line2,
                  radius=0.7,
                  quadrant=(-1, -1),
                  color=RED,
                  other_angle=True),
        ]
        plots = VGroup()
        for angle in angles:
            plot = VGroup(line1.copy(), line2.copy(), angle)
            plots.add(VGroup(plot, SurroundingRectangle(plot, buff=0.3)))
        plots.arrange_in_grid(rows=2, buff=1)
        self.add(plots)


class FilledAngle(Scene):

    def construct(self):
        l1 = Line(ORIGIN, 2 * UP + RIGHT).set_color(GREEN)
        l2 = (Line(ORIGIN,
                   2 * UP + RIGHT).set_color(GREEN).rotate(-20 * DEGREES,
                                                           about_point=ORIGIN))
        norm = l1.get_length()
        a1 = Angle(l1, l2, other_angle=True,
                   radius=norm - 0.5).set_color(GREEN)
        a2 = Angle(l1, l2, other_angle=True, radius=norm).set_color(GREEN)
        q1 = a1.points  #  save all coordinates of points of angle a1
        q2 = a2.reverse_direction(
        ).points  #  save all coordinates of points of angle a1 (in reversed direction)
        pnts = np.concatenate([
            q1, q2, q1[0].reshape(1, 3)
        ])  # adds points and ensures that path starts and ends at same point
        mfill = VMobject().set_color(ORANGE)
        mfill.set_points_as_corners(pnts).set_fill(GREEN, opacity=1)
        self.add(l1, l2)
        self.add(mfill)


class GetValueExample(Scene):

    def construct(self):
        line1 = Line(LEFT + (1 / 3) * UP, RIGHT + (1 / 3) * DOWN)
        line2 = Line(DOWN + (1 / 3) * RIGHT, UP + (1 / 3) * LEFT)

        angle = Angle(line1, line2, radius=0.4)

        value = DecimalNumber(angle.get_value(degrees=True), unit="^{\\circ}")
        value.next_to(angle, UR)

        self.add(line1, line2, angle, value)


class RightAngleExample(Scene):

    def construct(self):
        line1 = Line(LEFT, RIGHT)
        line2 = Line(DOWN, UP)
        rightangles = [
            RightAngle(line1, line2),
            RightAngle(line1, line2, length=0.4, quadrant=(1, -1)),
            RightAngle(line1,
                       line2,
                       length=0.5,
                       quadrant=(-1, 1),
                       stroke_width=8),
            RightAngle(line1, line2, length=0.7, quadrant=(-1, -1), color=RED),
        ]
        plots = VGroup()
        for rightangle in rightangles:
            plot = VGroup(line1.copy(), line2.copy(), rightangle)
            plots.add(plot)
        plots.arrange(buff=1.5)
        self.add(plots)


config.background_color = WHITE


class ChangedDefaultTextcolor(Scene):

    def construct(self):
        Text.set_default(color=BLACK)
        self.add(Text("Changing default values is easy!"))

        # we revert the colour back to the default to prevent a bug in the docs.
        Text.set_default(color=WHITE)


config.background_color = BLACK


class AnimateExample(Scene):

    def construct(self):
        s = Square()
        self.play(Create(s))
        self.play(s.animate.shift(RIGHT))
        self.play(s.animate.scale(2))
        self.play(s.animate.rotate(PI / 2))
        self.play(Uncreate(s))


class AnimateChainExample(Scene):

    def construct(self):
        s = Square()
        self.play(Create(s))
        self.play(s.animate.shift(RIGHT).scale(2).rotate(PI / 2))
        self.play(Uncreate(s))


class AnimateWithArgsExample(Scene):

    def construct(self):
        s = Square()
        c = Circle()

        VGroup(s, c).arrange(RIGHT, buff=2)
        self.add(s, c)

        self.play(
            s.animate(run_time=2).rotate(PI / 2),
            c.animate(rate_func=there_and_back).shift(RIGHT),
        )


class WidthExample(Scene):

    def construct(self):
        decimal = DecimalNumber().to_edge(UP)
        rect = Rectangle(color=BLUE)
        rect_copy = rect.copy().set_stroke(GRAY, opacity=0.5)

        decimal.add_updater(lambda d: d.set_value(rect.width))

        self.add(rect_copy, rect, decimal)
        self.play(rect.animate.set(width=7))
        self.wait()


class HeightExample(Scene):

    def construct(self):
        decimal = DecimalNumber().to_edge(UP)
        rect = Rectangle(color=BLUE)
        rect_copy = rect.copy().set_stroke(GRAY, opacity=0.5)

        decimal.add_updater(lambda d: d.set_value(rect.height))

        self.add(rect_copy, rect, decimal)
        self.play(rect.animate.set(height=5))
        self.wait()


class NextToUpdater(Scene):

    def construct(self):

        def dot_position(mobject):
            mobject.set_value(dot.get_center()[0])
            mobject.next_to(dot)

        dot = Dot(RIGHT * 3)
        label = DecimalNumber()
        label.add_updater(dot_position)
        self.add(dot, label)

        self.play(
            Rotating(dot,
                     about_point=ORIGIN,
                     angle=TAU,
                     run_time=TAU,
                     rate_func=linear))


class DtUpdater(Scene):

    def construct(self):
        line = Square()

        #Let the line rotate 90° per second
        line.add_updater(lambda mobject, dt: mobject.rotate(dt * 90 * DEGREES))
        self.add(line)
        self.wait(2)


class MobjectScaleExample(Scene):

    def construct(self):
        f1 = Text("F")
        f2 = Text("F").scale(2)
        f3 = Text("F").scale(0.5)
        f4 = Text("F").scale(-1)

        vgroup = VGroup(f1, f2, f3, f4).arrange(6 * RIGHT)
        self.add(vgroup)


class FlipExample(Scene):

    def construct(self):
        s = Line(LEFT, RIGHT + UP).shift(4 * LEFT)
        self.add(s)
        s2 = s.copy().flip()
        self.add(s2)


class ApplyFuncExample(Scene):

    def construct(self):
        circ = Circle().scale(1.5)
        circ_ref = circ.copy()
        circ.apply_complex_function(lambda x: np.exp(x * 1j))
        t = ValueTracker(0)
        circ.add_updater(
            lambda x: x.become(circ_ref.copy().apply_complex_function(
                lambda x: np.exp(x + t.get_value() * 1j))).set_color(BLUE))
        self.add(circ_ref)
        self.play(TransformFromCopy(circ_ref, circ))
        self.play(t.animate.set_value(TAU), run_time=3)


class GeometricShapes(Scene):

    def construct(self):
        d = Dot()
        c = Circle()
        s = Square()
        t = Triangle()
        d.next_to(c, RIGHT)
        s.next_to(c, LEFT)
        t.next_to(c, DOWN)
        self.add(d, c, s, t)


class AngleMidPoint(Scene):

    def construct(self):
        line1 = Line(ORIGIN, 2 * RIGHT)
        line2 = Line(ORIGIN, 2 * RIGHT).rotate_about_origin(80 * DEGREES)

        a = Angle(line1, line2, radius=1.5, other_angle=False)
        d = Dot(a.get_midpoint()).set_color(RED)

        self.add(line1, line2, a, d)
        self.wait()


class SortsExample(Scene):

    def construct(self):
        s1 = Square()
        s2 = Square()
        s3 = Square()
        s4 = Square()
        x = VGroup(s1, s2, s3, s4).set_x(0).arrange(buff=1.0)
        self.add(x)


class InvertSumobjectsExample(Scene):

    def construct(self):
        s = VGroup(*[Dot().shift(i * 0.1 * RIGHT) for i in range(-20, 20)])
        s2 = s.copy()
        s2.invert()
        s2.shift(DOWN)
        self.play(Write(s), Write(s2))


class ArrangeSumobjectsExample(Scene):

    def construct(self):
        s = VGroup(*[
            Dot().shift(i * 0.1 * RIGHT * np.random.uniform(-1, 1) +
                        UP * np.random.uniform(-1, 1)) for i in range(0, 15)
        ])
        s.shift(UP).set_color(BLUE)
        s2 = s.copy().set_color(RED)
        s2.arrange_submobjects()
        s2.shift(DOWN)
        self.add(s, s2)


class ShuffleSubmobjectsExample(Scene):

    def construct(self):
        s = VGroup(*[Dot().shift(i * 0.1 * RIGHT) for i in range(-20, 20)])
        s2 = s.copy()
        s2.shuffle_submobjects()
        s2.shift(DOWN)
        self.play(Write(s), Write(s2))


class DotInterpolation(Scene):

    def construct(self):
        dotR = Dot(color=DARK_GREY)
        # dotR.shift(2 * RIGHT)
        dotR.shift(2 * UR)
        dotL = Dot(color=WHITE)
        dotL.shift(2 * LEFT)

        dotMiddle = VMobject().interpolate(dotL, dotR, alpha=0.3)

        self.add(dotL, dotR, dotMiddle)


class BecomeScene(Scene):

    def construct(self):
        circ = Circle(fill_color=RED, fill_opacity=0.8)
        square = Square(fill_color=BLUE, fill_opacity=0.2)
        self.add(circ)
        self.wait(0.5)
        circ.become(square)
        self.wait(0.5)


class MatchPointsScene(Scene):

    def construct(self):
        circ = Circle(fill_color=RED, fill_opacity=0.8)
        square = Square(fill_color=BLUE, fill_opacity=0.2)
        self.add(circ)
        self.wait(0.5)
        self.play(circ.animate.match_points(square))
        self.wait(0.5)


class SetZIndex(Scene):

    def construct(self):
        text = Text('z_index = 3', color=PURE_RED).shift(UP).set_z_index(3)
        square = Square(2, fill_opacity=1).set_z_index(2)
        tex = Tex(r'zIndex = 1', color=PURE_BLUE).shift(DOWN).set_z_index(1)
        circle = Circle(radius=1.7, color=GREEN, fill_opacity=1)  # z_index = 0

        # Displaying order is now defined by z_index values
        self.add(text)
        self.add(square)
        self.add(tex)
        self.add(circle)


class CircleWithContent(VGroup):

    def __init__(self, content):
        super().__init__()
        self.circle = Circle()
        self.content = content
        self.add(self.circle, content)
        content.move_to(self.circle.get_center())

    def clear_content(self):
        self.remove(self.content)
        self.content = None

    @override_animate(clear_content)
    def _clear_content_animation(self, anim_args=None):
        if anim_args is None:
            anim_args = {}
        anim = Uncreate(self.content, **anim_args)
        self.clear_content()
        return anim


class AnimationOverrideExample(Scene):

    def construct(self):
        t = Text("hello!")
        my_mobject = CircleWithContent(t)
        self.play(Create(my_mobject))
        self.play(my_mobject.animate.clear_content())
        self.wait()
