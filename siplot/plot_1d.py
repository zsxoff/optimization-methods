import numpy as np
import matplotlib.pyplot as plt
from misc import func1d_to_string


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

    # TODO set_yticks?

    graph1.set_xticks(np.arange(graph_x_min, graph_x_max, 0.5))
    graph1.set_xticks(np.arange(graph_x_min, graph_x_max, 0.1), minor=True)
    graph1.grid(which='minor', alpha=0.1, linestyle="-")
    graph1.grid(which='major', alpha=0.5, linestyle="-")

    # Plot some dots.
    if dots:
        for dot in dots:
            graph1.plot(dot.x, dot.y, dot.color)

            if dot.x > graph_x_max:
                graph_x_max = dot.x

            if dot.x < graph_x_min:
                graph_x_min = dot.x

    # Plot some horizontal lines.
    if lines_xh:
        for line in lines_xh:
            graph1.axhline(y=line.y,
                           linestyle=":",
                           linewidth=1.5,
                           color=line.color)

            # TODO graph_ymin graph_ymax

    # Plot some vertical lines.
    if lines_xv:
        for line in lines_xv:
            graph1.axvline(x=line.x,
                           linestyle=":",
                           linewidth=1.5,
                           color=line.color)

            if line.x > graph_x_max:
                graph_x_max = line.x

            if line.x < graph_x_min:
                graph_x_min = line.x

    # Plot function.
    X = np.arange(graph_x_min, graph_x_max, 0.01)
    graph1.plot(X, func(X))

    # Plot title.
    plt.title(r'${}$'.format(func1d_to_string(func)), fontsize=12)
    plt.xlabel('x', fontsize=16, style="italic")
    plt.ylabel('f(x)', fontsize=16, style="italic")

    plt.show()
