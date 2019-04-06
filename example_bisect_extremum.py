#!/usr/bin/python3

from simethods.bisect import bisect_extremum
from misc import inputf
from siplot.plot_1d import plot_1d
from siplot.plot import Dot, LineXV, VectorXY
from misc import func1d_to_string
import numpy as np
from typing import Union


def f(x: Union[float, np.ndarray]) -> float:
    """
    Test function.

    """
    return x ** 3 - 7.5 * x ** 2 + 15.9 * x - 7.8


def main() -> None:
    """
    Example of finding extremum dots f(x) by bisection method.

    """
    l_border = inputf('left border: ')
    r_border = inputf('right border: ')
    eps = inputf('eps: ')

    x_min = bisect_extremum(f, l_border, r_border, eps, mode='min')
    x_max = bisect_extremum(f, l_border, r_border, eps, mode='max')

    f_min = f(x_min)
    f_max = f(x_max)

    f_print = func1d_to_string(f)

    print(f'f:   {f_print}\n'
          f'L:   {l_border}\n'
          f'R:   {r_border}\n'
          f'eps: {eps}\n')

    print(f'x_min    = {x_min}\n'
          f'f(x_min) = {f_min}\n'
          f'x_max    = {x_max}\n'
          f'f(x_max) = {f_max}\n')

    # TODO Move if border is greatest
    X = np.arange(0, 5, 0.01)

    vectors = [
        VectorXY(X, f(X), 'slategrey', 'f')
    ]

    dots = [
        Dot(x_min, f_min, 'bo'),
        Dot(x_max, f_max, 'ro')
    ]

    lines_xv = [
        LineXV(l_border, 'g'),
        LineXV(r_border, 'g')
    ]

    plot_1d(vectors=vectors, dots=dots, lines_xv=lines_xv)


if __name__ == '__main__':
    main()
