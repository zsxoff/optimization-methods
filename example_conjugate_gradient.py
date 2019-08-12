#!/usr/bin/env python

from sympy import cos

from misc import inputf
from simethods.conjugate_gradient_2d import conjugate_gradient_2d
from siplot.plot import Dot
from siplot.plot_2d import plot_2d


def f(x: float, y: float) -> float:
    """Test function."""
    return x**2 + y**2 + 4 * cos(x)


def main() -> None:
    """Conjugate gradient method example."""
    start_x = inputf('Enter start X: ')
    start_y = inputf('Enter start Y: ')
    eps = inputf('eps: ')

    x_min, y_min = conjugate_gradient_2d(f, start_x, start_y, eps)
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
