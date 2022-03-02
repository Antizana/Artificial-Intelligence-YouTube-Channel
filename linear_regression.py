import matplotlib.pyplot as plt
from random import randrange

from numpy import array
from numpy.linalg import inv
from numpy import linspace


def generate_linear_plots(num_points=20,
                          x_coeficient=1,
                          independent_term=5,
                          range_value=30,
                          range_divisor=10):
    """ Generate a the x and y values based on num_points data values with a 
    linear function expressed as y_value = m*x + c + random_value.

    The random value will generate a distortion in our output set of points
    
    Args:
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
            f"Parameters value for range_divisor can't be 0. Received: %s" %
            (type(range_divisor)))

    # Generate our x values and noisy y values
    x_values = [i for i in range(num_points)]
    y_values = [
        x_coeficient * x_values[i] + independent_term +
        randrange(-range_value, range_value) / range_divisor
        for i in range(num_points)
    ]

    # Calculate the b vector of y = X . b
    X = array(x_values)
    X = X.reshape(len(X), 1)
    b = inv(X.T.dot(X)).dot(X.T).dot(y_values)
    print(b)
    return (x_values, y_values)


def plot_linear():
    """ Prints the noisy dots and the linear interpolation"""
    (x_values, y_values) = generate_linear_plots()
    plt.scatter(x_values, y_values)
    plt.ylim(0, 30)
    x = linspace(0, 30)
    y = x + 5
    plt.plot(x, y, '-r', label='y=x+5')
    plt.show()


if __name__ == '__main__':
    plot_linear()