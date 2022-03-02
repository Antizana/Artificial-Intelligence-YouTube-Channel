import numpy as np

from manimlib import *
from random import randrange


class Linear_Plots(Scene):
    """ This class generate an animation of the linear regresion algorithm used
    in Machine Learning.

    Attributes:
    -----------
        _x_array: An array that stores the x coordinates of our model. 
        _y_array: An array that stores the y noisy values for our lineal model
         represented by y = mc + b
        _num_pints: Integer attrribute that stores the total dot samples for our
         animation
        _m: A float with the m calculated parameter for out linear model 
        _c: A float with the c calculated parameter for out linear model
    """
    _x_array = []
    _y_array = []
    _num_points = 20
    _m = 0.0
    _c = 0.0

    def _generate_linear_dots(num_point,
                              x_coeficient=1,
                              independent_term=5,
                              range_value=50,
                              range_divisor=10):
        """ Generate a value y based on an input x with a linear function 
        expressed as. `y_value` = m*x + c + random_value.

        The random value will generate a distortion in our output set of points
        
        Args
        ----
            num_point: x value for our output function f(x) + random.
            x_coeficient: m coeficient term of our linear function m*x + c.
            independent_term: represents the independente term c in our linear
             function m*x + c.
            range_value: range in which our random value will be generated as
             [-range_value, range_value].
            range_divisor: value used to normalize the random number generated.

        Returns: 
        --------
            A float with the result value of a noisy y of m*x + c + random
        """
        if not range_divisor:
            raise ValueError(
                f"Parameters value for range_divisor can't be 0. Received: %s"
                % (type(range_divisor)))

        x_value = num_point
        y_value = x_coeficient * x_value + independent_term + randrange(
            -range_value, range_value) / range_divisor
        return y_value

    def _generate_linear(num_point,
                         x_coeficient=1,
                         independent_term=5) -> float:
        """ 
        Generate a value y based on an input x with a linear function expressed 
        as: `y_value` = m*x + c 

        Args:
        -----
            num_point: x value for our output function f(x)
            x_coeficient: m coeficient term of our linear function m*x + c
            independent_term: represents the independente term c in our linear 
             function m*x + c

        Returns: 
        --------
            A float with the result value of the linear function m*x + c 
        """
        x_value = num_point
        y_value = x_coeficient * x_value + independent_term
        return y_value

    def _set_values():
        """ Calculate the values for x_array and y_array with the coordinates of 
        random noisy datapoints. 
        Set the values to our class attributes _x_array and _y_array
        """
        Linear_Plots._x_array = [x for x in range(Linear_Plots._num_points)]
        Linear_Plots._y_array = [
            Linear_Plots._generate_linear_dots(i)
            for i in range(Linear_Plots._num_points)
        ]

    def _calculate_linear_parameters():
        """ Generate the linear regresion parameters fiting a line y = mx + c,
        through some noisy data-points.
        Set the values to our class attributes _m and _c which correspond to
        """
        x = np.array(Linear_Plots._x_array)
        y = np.array(Linear_Plots._y_array)

        # Our equation can be written as y = Ap, where A = [[x, 1]] and
        # p = [[m], [c]]
        A = np.vstack([x, np.ones(len(x))]).T

        # Calculate out linear regresion parameters
        Linear_Plots._m, Linear_Plots._c = np.linalg.lstsq(A, y, rcond=None)[0]

    def construct(self):
        """ Constructor to do the animation of our linear regresion model. """
        Linear_Plots._set_values()
        Linear_Plots._calculate_linear_parameters()

        # Set the axes graph
        axes = Axes(x_range=(-5, 20, 5),
                    y_range=(-5, 30, 5),
                    width=12,
                    height=7,
                    axis_config={
                        "font_size": 28,
                        "include_numbers": False,
                        "tips": True,
                    })
        axes.set_color(GREY_B)

        # Attach title and axes labels to our graph
        graph_label = Text("LINEAR REGRESION",
                           font_size=48,
                           slant=ITALIC,
                           color=WHITE)
        x_label = Text("Experience (years)",
                       font_size=18,
                       slant=NORMAL,
                       color=WHITE)
        y_label = Text("Salary (USD$)",
                       font_size=18,
                       slant=NORMAL,
                       color=WHITE)
        function_label = Tex(
            f"y = {Linear_Plots._m:.2}x + {Linear_Plots._c:.2} + ",
            r"\epsilon",
            font_size=18,
            slant=NORMAL,
            color=RED_C)
        error_label = Text("----- Errors",
                           font_size=18,
                           slant=NORMAL,
                           color=WHITE)

        axes.x_axis.add(x_label.to_edge(DOWN + RIGHT, LARGE_BUFF))
        axes.y_axis.add(y_label.to_edge(LEFT + UP, LARGE_BUFF * 2))

        # Generates the noisy dots for our linear regresion model
        # linear_dots = axes.get_graph(
        #     lambda x: Linear_Plots._generate_linear_dots(x), )
        linear_dots = axes.get_graph(
            lambda x: Linear_Plots._y_array[int(x)]
            if x in range(Linear_Plots._num_points) else 0, )

        # Generates the linear regresion line
        line = axes.get_graph(
            lambda x: Linear_Plots._generate_linear(x, Linear_Plots._m,
                                                    Linear_Plots._c), )
        line.set_stroke(RED_C, 2)

        # Generates the error dashed lines
        error_lines = []
        for i in range(Linear_Plots._num_points):
            y_line_plot = Linear_Plots._generate_linear(
                Linear_Plots._x_array[i], Linear_Plots._m, Linear_Plots._c)
            x1 = Linear_Plots._x_array[i]
            y1 = Linear_Plots._y_array[i]
            error_lines.append(
                DashedLine(axes.c2p(x1, y1),
                           axes.c2p(x1, y_line_plot),
                           stroke_width=2,
                           color=WHITE))
        self.add(axes)

        # Animate the noisy dots
        dots = VGroup(*[
            Dot(axes.input_to_graph_point(x, linear_dots))
            for x in range(0, Linear_Plots._num_points)
        ])
        dots.set_color(YELLOW)

        # Animate the linear regresion
        self.play(Write(graph_label.to_edge(UP)))
        kw = {"lag_ratio": 0.5}
        self.play(LaggedStartMap(FadeIn, dots, lambda m: (m, UP), **kw), )
        self.add(line, *dots)
        self.play(ShowCreation(line), run_time=3)
        self.play(
            ShowCreation(
                function_label.next_to(line,
                                       UP + RIGHT).shift(DOWN * 2.5).align_to(
                                           line, RIGHT)))

        self.play(AnimationGroup(*[ShowCreation(VGroup(*error_lines))]),
                  lag_ratio=0.15,
                  run_time=6)
        self.play(
            ShowCreation(
                error_label.next_to(function_label,
                                    DOWN).align_to(function_label, RIGHT)))
        self.wait(2)