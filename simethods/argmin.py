from sympy import lambdify
from simethods.borders import find_min_border
from simethods.bisect import bisect_extremum
from numpy import ndarray
from typing import Callable
from sympy.core.symbol import Symbol


def compute_optimal_step(func: Callable, parameterized_vector: ndarray,
                         parameter: Symbol, eps: float) -> float:
    """
    Compute minimal (optimal) step for func(parameterized_vector)

    """
    function_z = lambdify(
        args=(parameter,),
        expr=func(parameterized_vector[0][0], parameterized_vector[1][0]))

    left, right = find_min_border(
        f=function_z, start=0.0, init_step=0.25, step_expand=1.1, max_iters=10)

    argmin_f = bisect_extremum(
        f=function_z, a=left, b=right, eps=eps, mode='min')

    return argmin_f
