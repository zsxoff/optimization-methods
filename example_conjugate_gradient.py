#!/usr/bin/python3

from simethods.conjugate_gradient_2d import conjugate_gradient_2d
from misc import inputf
from plot_2d import plot_2d
from sympy import Symbol, cos
from sympy.utilities.lambdify import lambdastr


def f(x: float, y: float) -> float:
    # TODO Doc
    return x ** 2 + y ** 2 + 4 * cos(x)


def main() -> None:
    # TODO Doc
    start_x = inputf('Enter start X: ')
    start_y = inputf('Enter start Y: ')
    eps = inputf('eps: ')

    x_min, y_min = conjugate_gradient_2d(f, start_x, start_y, eps)
    f_min = f(x_min, y_min)

    s_x = Symbol('x')
    s_y = Symbol('y')
    f_print = lambdastr((s_x, s_y), f(s_x, s_y))

    print(f'f               = {f_print}\n'
          f'x_min           = {x_min}\n'
          f'y_min           = {y_min}\n'
          f'f(x_min, y_min) = {f_min}\n')

    plot_2d(f, x_min, y_min)


if __name__ == '__main__':
    main()
