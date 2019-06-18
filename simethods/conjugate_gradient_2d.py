from typing import Callable, Tuple

import numpy as np
from numpy.linalg import norm
from sympy import Symbol

from simethods.argmin import compute_optimal_step


def conjugate_gradient_2d(f: Callable,
                          x0: float,
                          y0: float,
                          eps: float,
                          max_iters: int = 100) -> Tuple[float, float]:
    """Conjugate Gradient method for f(x, y)."""

    # Use SymPy function.
    x = Symbol('x')
    y = Symbol('y')
    _f = f(x, y)

    # Init initial X, dim 2x1.
    X_0 = np.zeros((2, 1), dtype=np.float)
    X_0[0] = x0
    X_0[1] = y0

    _f_dx = _f.diff(x, 1)
    _f_dy = _f.diff(y, 1)

    # Init S, dim 2x1.
    grad_0 = np.zeros((2, 1), dtype=np.float)
    grad_0[0] = _f_dx.subs([(x, X_0[0]), (y, X_0[1])])
    grad_0[1] = _f_dy.subs([(x, X_0[0]), (y, X_0[1])])
    S_0 = -grad_0

    iterations_count = -1

    while True:
        iterations_count += 1
        if iterations_count > max_iters:
            return float(X_0[0][0]), float(X_0[1][0])

        # Compute optimal step.
        param = Symbol('z')
        param_vector = X_0 + Symbol('z') * S_0

        optimal_step = compute_optimal_step(func=f,
                                            parameterized_vector=param_vector,
                                            parameter=param,
                                            eps=eps)

        # Compute new X, dim 2x1.
        X_1 = X_0 + optimal_step * S_0

        # Compute new gradient f(X_1), dim 2x1.
        grad_1 = np.zeros((2, 1), dtype=np.float)
        grad_1[0] = _f_dx.subs([(x, X_1[0]), (y, X_1[1])])
        grad_1[1] = _f_dy.subs([(x, X_1[0]), (y, X_1[1])])

        # Compute new S, dim 2x1.
        S_1 = -(grad_1) + norm(grad_1, 2) / norm(grad_0, 2) * S_0

        if np.linalg.norm(S_1 - S_0) < eps:
            return float(X_1[0][0]), float(X_1[1][0])

        # Set all values as previous step.
        X_0, S_0, grad_0 = X_1, S_1, grad_1
