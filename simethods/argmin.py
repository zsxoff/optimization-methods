from sympy import lambdify
from simethods.borders import find_min_border
from simethods.bisect import bisect_extremum


def compute_optimal_step(func, parameterized_vector, parameter, eps):
    function_z = lambdify(
        args=(parameter,),
        expr=func(parameterized_vector[0][0], parameterized_vector[1][0]))

    left, right = find_min_border(
        f=function_z,
        start=0.0,
        init_step=0.25,
        step_expand=1.1,
        max_iters=10)

    argmin_f = bisect_extremum(
        f=function_z, a=left, b=right, eps=eps, mode='min')

    return argmin_f
