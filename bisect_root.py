#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from simethods.bisect import bisect_root
from simethods.misc import inputf


def f(x):
    """
    Test function.

    """
    return x**3 - 7.5 * x**2 + 15.9 * x - 7.8


def main():
    # ----- Read values -----
    l_border = inputf("left border: ")
    r_border = inputf("right border: ")
    eps = inputf("eps: ")

    x_root = bisect_root(f, l_border, r_border, eps)
    f_root = f(x_root)

    print(f'L:\t{l_border}\n'
          f'R:\t{r_border}\n'
          f'eps:\t{eps}\n\n'
          f'root    = {x_root}\n'
          f'f(root) = {f_root}\n')

    # ----- Plot graph -----
    GRAPH_L = -0.5
    GRAPH_R = 5.6

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
    graph1.plot(x_root, f_root, 'go')

    # Plot title.
    plt.title(r'$f(x) = x^3 - 7.5x^2 + 15.9x - 7.8$', fontsize=12)
    plt.xlabel('x', fontsize=16, style="italic")
    plt.ylabel('f(x)', fontsize=16, style="italic")

    plt.show()


if __name__ == '__main__':
    main()
