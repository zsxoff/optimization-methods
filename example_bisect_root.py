#!/usr/bin/python3

from simethods.bisect import bisect_root
from misc import inputf, func1d_to_string
from siplot.plot import Dot, LineXV, VectorXY
from siplot.plot_1d import plot_1d
import numpy as np
from typing import Union


def f(x: Union[float, np.ndarray]) -> float:
    """
    Test function.

    """
    return x ** 3 - 7.5 * x ** 2 + 15.9 * x - 7.8


def main() -> None:
    """
    Example of finding the root f(x) by bisection method.

    """
    l_border = inputf('left border: ')
    r_border = inputf('right border: ')
    eps = inputf('eps: ')

    x_root = bisect_root(f, l_border, r_border, eps)
    f_root = f(x_root)

    f_print = func1d_to_string(f)

    print(f'f:   {f_print}\n'
          f'L:   {l_border}\n'
          f'R:   {r_border}\n'
          f'eps: {eps}\n')

    print(f'root    = {x_root}\n'
          f'f(root) = {f_root}\n')

    # TODO Move if border is greatest
    X = np.arange(0, 5, 0.01)

    vectors = [
        VectorXY(X, f(X), 'slategrey', 'f')
    ]

    dots = [
        Dot(x_root, f_root, 'ro'),
    ]

    lines_xv = [
        LineXV(l_border, 'g'),
        LineXV(r_border, 'g')
    ]

    plot_1d(vectors=vectors, dots=dots, lines_xv=lines_xv)


if __name__ == '__main__':
    main()
