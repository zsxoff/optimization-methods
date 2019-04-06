from sympy import lambdify, Symbol
import numpy as np
import matplotlib.pyplot as plt
from misc import func2d_to_string
from typing import Callable, Tuple
from siplot.plot import Dot


def plot_2d(func: Callable,
            graph_x_min: float = -4,
            graph_x_max: float = 4,
            graph_y_min: float = -4,
            graph_y_max: float = 4,
            dots: Tuple[Dot] = None) -> None:
    """
    Plot f(x, y) function with additional plots.

    """
    fig = plt.figure(1)
    graph = fig.add_subplot(1, 1, 1)

    x = np.arange(graph_x_min, graph_x_max, 0.1)
    y = np.arange(graph_y_min, graph_y_max, 0.1)
    X, Y = np.meshgrid(x, y)

    # Get values vector.
    s_x, s_y = Symbol('x'), Symbol('y')
    F = lambdify(args=(s_x, s_y), expr=func(s_x, s_y), modules='numpy')
    F = F(X, Y)

    # Plot some dots.
    if dots:
        for dot in dots:
            graph.plot(dot.x, dot.y, dot.color)

            if dot.x > graph_x_max:
                graph_x_max = dot.x

            if dot.x < graph_x_min:
                graph_x_min = dot.x

            if dot.y > graph_y_max:
                graph_y_max = dot.y

            if dot.y < graph_y_min:
                graph_y_min = dot.y

    plt.imshow(
        F,
        vmin=F.min(),
        vmax=F.max(),
        origin='lower',
        extent=[X.min(), X.max(), Y.min(), Y.max()],
        cmap='viridis')

    plt.title(r'${}$'.format(func2d_to_string(func)), fontsize=12)
    plt.contour(X, Y, F)
    plt.show()
