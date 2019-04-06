#!/usr/bin/python3
from misc import func1d_to_string
from simethods.borders import find_min_border
from siplot.plot import LineXV
from siplot.plot_1d import plot_1d


def f(x: float) -> float:
    """
    Test function.

    """
    return x ** 2 - x ** 4


def main() -> None:
    """
    Example of finding the approximate limit of the minimum value f(x).

    """

    l_border, r_border = find_min_border(f)

    lines_xv = [
        LineXV(l_border, 'g'),
        LineXV(r_border, 'g')
    ]

    f_plot = func1d_to_string(f)

    print(f'{f_plot}\n'
          f'L: {l_border}\n'
          f'R: {r_border}\n')

    plot_1d(f, graph_x_min=-1, graph_x_max=1, lines_xv=lines_xv)


if __name__ == '__main__':
    main()
