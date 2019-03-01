import math
from functools import lru_cache


def compare(a, b, mode):
    """
    Compares two values and returns the result
    depending on the mode.

    """
    if mode == 'root':
        return a * b < 0

    elif mode == 'min':
        return a < b

    elif mode == 'max':
        return a > b


@lru_cache(maxsize=64)
def fib(n):
    """
    Compute Fibonacci n value.

    """
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


def bisect_root(f, a, b, eps):
    while True:
        c = (a + b) / 2

        if abs(b - a) < (2 * eps):
            return c

        if f(c) == 0:
            return c

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c


def bisect_extremum(f, a, b, eps, mode='min'):
    assert (mode in ('min', 'max')), f'No mode "{mode}"'

    if mode == 'min':
        C = 1
    else:
        C = -1

    while True:
        x = (a + b) / 2

        if abs(b - a) < (2 * eps):
            return x

        if C * f(x - eps) < C * f(x + eps):
            b = x
        else:
            a = x


def golden(f, a, b, eps, mode='min'):
    assert (mode in ('min', 'max')), f'No mode "{mode}"'

    phi = (1 + math.sqrt(5)) / 2

    while True:
        x1 = b - (b - a) / phi
        x2 = a + (b - a) / phi

        if compare(f(x1), f(x2), mode):
            b = x2
            x2 = x1
            x1 = a + (b - x2)
        else:
            a = x1
            x1 = x2
            x2 = b - (x1 - a)

        if (b - a) / 2 < eps:
            return (a + b) / 2
