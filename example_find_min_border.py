#!/usr/bin/python3
from typing import NoReturn, Union

import numpy as np

from simethods.borders import find_min_border
from siplot.plot import LineXV, VectorXY
from siplot.plot_1d import plot_1d


def f(x: Union[float, np.ndarray]) -> Union[float, np.ndarray]:
    """Test function."""
    return x**2 - x**4


def main() -> NoReturn:
    """Find a approximate limit of the minimum value f(x)."""

    l_border, r_border = find_min_border(f)

    print(f'L: {l_border}\n' f'R: {r_border}\n')

    # Plot result.
    vector_x = np.arange(l_border - 1, r_border + 1, 0.01)

    vectors = [
        VectorXY(vector_x, f(vector_x), 'slategrey', 'f'),
    ]

    lines_xv = [
        LineXV(l_border, 'g'),
        LineXV(r_border, 'g'),
    ]

    plot_1d(vectors=vectors, lines_xv=lines_xv)


if __name__ == '__main__':
    main()
