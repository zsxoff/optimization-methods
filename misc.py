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
    """
    Convert f: Callable function to latex-like string.

    """
    s_x = Symbol('x')
    s_y = Symbol('y')
    f_print = lambdastr((s_x, s_y), f(s_x, s_y))

    replace_dict = {
        'lambda x,y:': '',
        '**': '^',
        'numpy': '',
    }

    for key in replace_dict:
        f_print = f_print.replace(key, replace_dict[key])
    f_print = f_print.strip()

    return f_print[1:len(f_print) - 1]
