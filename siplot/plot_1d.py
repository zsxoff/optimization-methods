import numpy as np
import matplotlib.pyplot as plt
from typing import List
from siplot.plot import Dot, LineXV, LineXH, VectorXY


def plot_1d(vectors: List[VectorXY] = None,
            dots: List[Dot] = None,
            lines_xh: List[LineXH] = None,
            lines_xv: List[LineXV] = None,
            xticks_step_major: float = 1.0,
            xticks_step_minor: float = 0.5,
            title: str = None) -> None:
    """
    Plot f(x) function with additional plots.

    """
    fig = plt.figure(1)
    graph = fig.add_subplot(1, 1, 1)
    graph.grid(which='minor', alpha=0.1, linestyle="-")
    graph.grid(which='major', alpha=0.5, linestyle="-")

    # Plot some horizontal lines.
    if lines_xh:
        for line in lines_xh:
            graph.axhline(y=line.y,
                          linestyle=":",
                          linewidth=1.5,
                          color=line.color)

    # Plot some vertical lines.
    if lines_xv:
        for line in lines_xv:
            graph.axvline(x=line.x,
                          linestyle=":",
                          linewidth=1.5,
                          color=line.color)

    graph_x_min = -4
    graph_x_max = -4

    # Plot some vectors.
    if vectors:
        for vector in vectors:
            graph.plot(vector.X, vector.Y)

            if vector.X[0] < graph_x_min:
                graph_x_min = vector.X[0]

            if vector.X[-1] > graph_x_max:
                graph_x_max = vector.X[-1]

    # Plot some dots.
    if dots:
        for dot in dots:
            graph.plot(dot.x, dot.y, dot.color)

            if dot.x > graph_x_max:
                graph_x_max = dot.x

            if dot.x < graph_x_min:
                graph_x_min = dot.x

    # Set xticks.
    graph.set_xticks(np.arange(graph_x_min, graph_x_max, xticks_step_major))
    graph.set_xticks(np.arange(graph_x_min, graph_x_max, xticks_step_minor),
                     minor=True)

    # Plot title.
    if title:
        plt.title(r'${}$'.format(title), fontsize=12)

    plt.xlabel('x', fontsize=16, style="italic")
    plt.ylabel('f(x)', fontsize=16, style="italic")

    plt.show()
