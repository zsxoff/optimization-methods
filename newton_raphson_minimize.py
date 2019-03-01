#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from simethods.newton_raphson_2d import newton_raphson_2d
from simethods.misc import inputf
from sympy import Symbol, sin, cos, exp, lambdify


def f(x, y):
    return y**4 + x * y**3 + 2 * (y**2) * (x**2) + y + x**4 - x


def _f_numpy():
    x = Symbol('x')
    y = Symbol('y')
    return lambdify((x, y), f(x, y), modules='numpy')


def f_numpy(x, y):
    return _f_numpy()(x, y)


def main():
    start_x = inputf('Enter start X: ')
    start_y = inputf('Enter start Y: ')
    eps = inputf('eps: ')

    x_min, y_min = newton_raphson_2d(f, start_x, start_y, eps)
    f_min = f_numpy(x_min, y_min)

    print(f'x_min           = {x_min}\n'
          f'y_min           = {y_min}\n'
          f'f(x_min, y_min) = {f_min}\n')

    # ----- Plot graph -----
    graph_x_min, graph_x_max = -4, 4
    graph_y_min, graph_y_max = -4, 4

    if x_min < graph_x_min:
        graph_x_min = x_min

    if x_min > graph_x_max:
        graph_x_max = x_min

    if y_min < graph_y_min:
        graph_y_min = y_min

    if y_min > graph_y_max:
        graph_y_max = y_min

    fig = plt.figure(1)
    g = fig.add_subplot(1, 1, 1)

    x = np.arange(graph_x_min, graph_x_max, 0.1)
    y = np.arange(graph_y_min, graph_y_max, 0.1)
    X, Y = np.meshgrid(x, y)
    F = f_numpy(X, Y)

    plt.imshow(
        F,
        vmin=F.min(),
        vmax=F.max(),
        origin='lower',
        extent=[X.min(), X.max(), Y.min(), Y.max()],
        cmap='viridis')

    g.plot(x_min, y_min, 'bo')
    plt.show()


if __name__ == '__main__':
    main()
