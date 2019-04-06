#!/usr/bin/python3

from simethods.bisect import bisect_extremum
from misc import inputf
from siplot.plot_1d import plot_1d
from siplot.plot import Dot, LineXV


def f(x: float) -> float:
    """
    Test function.

    """
    return x ** 3 - 7.5 * x ** 2 + 15.9 * x - 7.8


def main():
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

    print(f'L:\t{l_border}\n'
          f'R:\t{r_border}\n'
          f'eps:\t{eps}\n\n'
          f'x_min    = {x_min}\n'
          f'f(x_min) = {f_min}\n'
          f'x_max    = {x_max}\n'
          f'f(x_max) = {f_max}\n')

    dots = [
        Dot(x_min, f_min, 'bo'),
        Dot(x_max, f_max, 'ro')
    ]

    lines_xv = [
        LineXV(l_border, 'g'),
        LineXV(r_border, 'g')
    ]

    plot_1d(f, graph_x_min=0, graph_x_max=4, dots=dots, lines_xv=lines_xv)


if __name__ == '__main__':
    main()
