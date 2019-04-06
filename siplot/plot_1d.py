import numpy as np
import matplotlib.pyplot as plt
from misc import func1d_to_string
from typing import Callable, List
from siplot.plot import Dot, LineXV, LineXH


def plot_1d(func: Callable,
            graph_x_min: float = -4,
            graph_x_max: float = 4,
            dots: List[Dot] = None,
            lines_xh: List[LineXH] = None,
            lines_xv: List[LineXV] = None) -> None:
    """
    Plot f(x) function with additional plots.

    """
    fig = plt.figure(1)
    graph = fig.add_subplot(1, 1, 1)

    # TODO set_yticks?

    graph.set_xticks(np.arange(graph_x_min, graph_x_max, 0.5))
    graph.set_xticks(np.arange(graph_x_min, graph_x_max, 0.1), minor=True)
    graph.grid(which='minor', alpha=0.1, linestyle="-")
    graph.grid(which='major', alpha=0.5, linestyle="-")

    # Plot some dots.
    if dots:
        for dot in dots:
            graph.plot(dot.x, dot.y, dot.color)

            if dot.x > graph_x_max:
                graph_x_max = dot.x

            if dot.x < graph_x_min:
                graph_x_min = dot.x

    # Plot some horizontal lines.
    if lines_xh:
        for line in lines_xh:
            graph.axhline(y=line.y,
                          linestyle=":",
                          linewidth=1.5,
                          color=line.color)

            # TODO graph_ymin graph_ymax

    # Plot some vertical lines.
    if lines_xv:
        for line in lines_xv:
            graph.axvline(x=line.x,
                          linestyle=":",
                          linewidth=1.5,
                          color=line.color)

            if line.x > graph_x_max:
                graph_x_max = line.x

            if line.x < graph_x_min:
                graph_x_min = line.x

    # Plot function.
    X = np.arange(graph_x_min, graph_x_max, 0.01)
    graph.plot(X, func(X))

    # Plot title.
    plt.title(r'${}$'.format(func1d_to_string(func)), fontsize=12)
    plt.xlabel('x', fontsize=16, style="italic")
    plt.ylabel('f(x)', fontsize=16, style="italic")

    plt.show()
