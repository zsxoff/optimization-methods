from sympy import lambdify, Symbol
import numpy as np
import matplotlib.pyplot as plt
from misc import func2d_to_string


def plot_2d(func, x_min, y_min,
            graph_x_min=-4,
            graph_x_max=4,
            graph_y_min=-4,
            graph_y_max=4):
    # TODO Doc
    if x_min < graph_x_min:
        graph_x_min = x_min

    if x_min > graph_x_max:
        graph_x_max = x_min

    if y_min < graph_y_min:
        graph_y_min = y_min

    if y_min > graph_y_max:
        graph_y_max = y_min

    fig = plt.figure(1)
    graphic = fig.add_subplot(1, 1, 1)

    x = np.arange(graph_x_min, graph_x_max, 0.1)
    y = np.arange(graph_y_min, graph_y_max, 0.1)
    X, Y = np.meshgrid(x, y)

    # Get values vector.
    s_x, s_y = Symbol('x'), Symbol('y')
    F = lambdify(args=(s_x, s_y), expr=func(s_x, s_y), modules='numpy')
    F = F(X, Y)

    plt.imshow(
        F,
        vmin=F.min(),
        vmax=F.max(),
        origin='lower',
        extent=[X.min(), X.max(), Y.min(), Y.max()],
        cmap='viridis')

    plt.title(r'${}$'.format(func2d_to_string(func)), fontsize=12)
    plt.contour(X, Y, F)
    graphic.plot(x_min, y_min, 'bo')
    plt.show()
