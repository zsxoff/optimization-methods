from typing import Callable
from sympy.utilities.lambdify import lambdastr
from sympy import Symbol


def inputf(text):
    # TODO Doc
    try:
        return float(input(text))

    except SystemExit:
        print("\nError: system exit\n")
        exit(-1)

    except KeyboardInterrupt:
        print("\nError: keyboard interrupt\n")
        exit(-1)

    except ValueError:
        print("\nError: invalid values specified")
        exit(-1)

    except TypeError:
        print("\nError: type error")
        exit(-1)


def func2d_to_string(f: Callable) -> str:
    s_x = Symbol('x')
    s_y = Symbol('y')
    f_print = lambdastr((s_x, s_y), f(s_x, s_y))

    f_print = f_print.replace('lambda x,y:', '').replace('**', '^').strip()

    return f_print[1:len(f_print) - 1]
