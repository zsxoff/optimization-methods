#!/usr/bin/python3

from typing import NoReturn, Union

import numpy as np

import misc
from simethods.bisect import bisect_extremum
from siplot.plot import Dot, LineXV, VectorXY
from siplot.plot_1d import plot_1d


def f(x: Union[float, np.ndarray]) -> Union[float, np.ndarray]:
    """Test function."""
    return x**3 - 7.5 * x**2 + 15.9 * x - 7.8


def main() -> NoReturn:
    """Find extremum dots f(x) by bisection method."""
    l_border = misc.inputf('left border: ')
    r_border = misc.inputf('right border: ')
    eps = misc.inputf('eps: ')

    x_min = bisect_extremum(f, l_border, r_border, eps, mode='min')
    x_max = bisect_extremum(f, l_border, r_border, eps, mode='max')

    f_min = f(x_min)
    f_max = f(x_max)

    print(f'L:   {l_border}\n' f'R:   {r_border}\n' f'eps: {eps}\n')

    print(f'x_min    = {x_min}\n'
          f'f(x_min) = {f_min}\n'
          f'x_max    = {x_max}\n'
          f'f(x_max) = {f_max}\n')

    # Plot result.
    vector_x = np.arange(l_border - 1, r_border + 1, 0.1)

    vectors = [
        VectorXY(vector_x, f(vector_x), 'slategrey', 'function'),
    ]

    dots = [
        Dot(x_min, f_min, 'bo'),
        Dot(x_max, f_max, 'ro'),
    ]

    lines_xv = [
        LineXV(l_border, 'g'),
        LineXV(r_border, 'g'),
    ]

    plot_1d(vectors=vectors, dots=dots, lines_xv=lines_xv)


if __name__ == '__main__':
    main()
