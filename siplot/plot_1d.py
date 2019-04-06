import numpy as np
import matplotlib.pyplot as plt


def plot_1d(func,
            graph_x_min=-4,
            graph_x_max=4,
            dots=None,
            lines_xh=None,
            lines_xv=None):
    """
    Plot f(x) function with additional plots.

    """
    fig = plt.figure(1)
    graph1 = fig.add_subplot(1, 1, 1)

    graph1.set_xticks(np.arange(graph_x_min, graph_x_max, 0.5))
    graph1.set_xticks(np.arange(graph_x_min, graph_x_max, 0.1), minor=True)
    graph1.grid(which='minor', alpha=0.1, linestyle="-")
    graph1.grid(which='major', alpha=0.5, linestyle="-")

    # Plot some dots.
    if dots:
        for dot in dots:
            graph1.plot(dot.x, dot.y, dot.color)

    # Plot some horizontal lines.
    if lines_xh:
        for line in lines_xh:
            graph1.axhline(y=line.y,
                           linestyle=":",
                           linewidth=1.5,
                           color=line.color)

    # Plot some vertical lines.
    if lines_xv:
        for line in lines_xv:
            graph1.axvline(x=line.x,
                           linestyle=":",
                           linewidth=1.5,
                           color=line.color)

    # Plot function.
    X = np.arange(graph_x_min, graph_x_max, 0.01)
    graph1.plot(X, func(X))

    # Plot title.
    plt.title(r'$f(x) = x^3 - 7.5x^2 + 15.9x - 7.8$', fontsize=12)
    plt.xlabel('x', fontsize=16, style="italic")
    plt.ylabel('f(x)', fontsize=16, style="italic")

    plt.show()
