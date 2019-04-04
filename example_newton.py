#!/usr/bin/python3

from simethods.newton_2d import newton_2d
from misc import inputf, func2d_to_string
from plot_2d import plot_2d


def f(x: float, y: float) -> float:
    """
    Test function.

    """
    return y ** 4 + x * y ** 3 + 2 * (y ** 2) * (x ** 2) + y + x ** 4 - x


def main() -> None:
    """
    Newton-Raphson method example.

    """
    start_x = inputf('Enter start X: ')
    start_y = inputf('Enter start Y: ')
    eps = inputf('eps: ')

    x_min, y_min = newton_2d(f, start_x, start_y, eps)
    f_min = f(x_min, y_min)

    f_print = func2d_to_string(f)

    print(f'f               = {f_print}\n'
          f'x_min           = {x_min}\n'
          f'y_min           = {y_min}\n'
          f'f(x_min, y_min) = {f_min}\n')

    plot_2d(f, x_min, y_min)


if __name__ == '__main__':
    main()
