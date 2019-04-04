from sympy import lambdify, Symbol
import numpy as np
import matplotlib.pyplot as plt
from sympy.utilities.lambdify import lambdastr


def plot_2d(func, x_min, y_min,
            graph_x_min=-4,
            graph_x_max=4,
            graph_y_min=-4,
            graph_y_max=4):
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

    s_x = Symbol('x')
    s_y = Symbol('y')
    f_print = lambdastr((s_x, s_y), func(s_x, s_y))
    f_print = f_print.replace('lambda x,y:', '')
    f_print = f_print.replace('**', '^')

    plt.title(r'${}$'.format(f_print), fontsize=12)
    plt.contour(X, Y, F)
    graphic.plot(x_min, y_min, 'bo')
    plt.show()
