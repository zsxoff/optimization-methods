#!/usr/bin/python3

from simethods.bisect import bisect_root
from misc import inputf
from siplot.plot import Dot, LineXV
from siplot.plot_1d import plot_1d


def f(x: float) -> float:
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

    # TODO Print function
    print(f'L:\t{l_border}\n'
          f'R:\t{r_border}\n'
          f'eps:\t{eps}\n\n'
          f'root    = {x_root}\n'
          f'f(root) = {f_root}\n')

    dots = [
        Dot(x_root, f_root, 'ro'),
    ]

    lines_xv = [
        LineXV(l_border, 'g'),
        LineXV(r_border, 'g')
    ]

    plot_1d(f, graph_x_min=0, graph_x_max=4, dots=dots, lines_xv=lines_xv)


if __name__ == '__main__':
    main()
