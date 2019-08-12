#!/usr/bin/env python

import misc
from simethods.newton_raphson_2d import newton_raphson_2d
from siplot.plot import Dot
from siplot.plot_2d import plot_2d


def f(x: float, y: float) -> float:
    """Test function."""
    return y**4 + x * y**3 + 2 * (y**2) * (x**2) + y + x**4 - x


def main() -> None:
    """Newton-Raphson method example."""
    start_x = misc.inputf('Enter start X: ')
    start_y = misc.inputf('Enter start Y: ')
    eps = misc.inputf('eps: ')

    x_min, y_min = newton_raphson_2d(f, start_x, start_y, eps)
    f_min = f(x_min, y_min)

    print(f'x_min           = {x_min}\n'
          f'y_min           = {y_min}\n'
          f'f(x_min, y_min) = {f_min}\n')

    # Plot result.
    dots = [
        Dot(x_min, y_min, 'ro'),
    ]

    plot_2d(f, dots=dots)


if __name__ == '__main__':
    main()
