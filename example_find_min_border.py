#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from simethods.borders import find_min_border


def f(x):
    # TODO Doc
    # return x**3 - 7.5 * x**2 + 15.9 * x - 7.8
    return x ** 2 - x ** 4


def main():
    # TODO Doc
    # ----- Plot graph -----
    GRAPH_L = -1.2
    GRAPH_R = 1.2

    l_border, r_border = find_min_border(f)

    fig = plt.figure(1)
    graph1 = fig.add_subplot(1, 1, 1)
    graph1.set_xticks(np.arange(GRAPH_L, GRAPH_R, 0.5))
    graph1.set_xticks(np.arange(GRAPH_L, GRAPH_R, 0.1), minor=True)

    graph1.grid(which='minor', alpha=0.1, linestyle="-")
    graph1.grid(which='major', alpha=0.5, linestyle="-")

    graph1.axvline(x=l_border, linestyle=":", linewidth=1.5, color='g')
    graph1.axvline(x=r_border, linestyle=":", linewidth=1.5, color='g')

    X = np.arange(GRAPH_L, GRAPH_R, 0.01)
    F = f(X)

    graph1.plot(X, F)
    # graph1.plot(x_min, f_min, 'bo')
    # graph1.plot(x_max, f_max, 'ro')

    # Plot title.
    plt.title(r'$f(x) = x^2$', fontsize=12)
    plt.xlabel('x', fontsize=16, style="italic")
    plt.ylabel('f(x)', fontsize=16, style="italic")

    plt.show()


if __name__ == '__main__':
    main()
