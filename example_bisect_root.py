#!/usr/bin/python3

from typing import Union

import numpy as np

import misc
from simethods.bisect import bisect_root
from siplot.plot import Dot, LineXV, VectorXY
from siplot.plot_1d import plot_1d


def f(x: Union[float, np.ndarray]) -> Union[float, np.ndarray]:
    """Test function."""
    return x**3 - 7.5 * x**2 + 15.9 * x - 7.8


def main() -> None:
    """Find the root f(x) by bisection method."""
    l_border = misc.inputf('left border: ')
    r_border = misc.inputf('right border: ')
    eps = misc.inputf('eps: ')

    x_root = bisect_root(f, l_border, r_border, eps)
    f_root = f(x_root)

    print(f'L:   {l_border}\n' f'R:   {r_border}\n' f'eps: {eps}\n')

    print(f'root    = {x_root}\n' f'f(root) = {f_root}\n')

    # Plot result.
    vector_x = np.arange(l_border - 1, r_border + 1, 0.1)

    vectors = [
        VectorXY(vector_x, f(vector_x), 'slategrey', 'f'),
    ]

    dots = [
        Dot(x_root, f_root, 'ro'),
    ]

    lines_xv = [
        LineXV(l_border, 'g'),
        LineXV(r_border, 'g'),
    ]

    plot_1d(vectors=vectors, dots=dots, lines_xv=lines_xv)


if __name__ == '__main__':
    main()
