import numpy as np
from sympy import Symbol


def newton_raphson_2d(f, x0, y0, eps):
    """
    Newton-Raphson method for f(x, y).

    """

    # Use SymPy function.
    x = Symbol('x')
    y = Symbol('y')
    _f = f(x, y)

    # Init initial X, dim 2x1.
    X = np.zeros((2, 1), dtype=np.float)
    X[0] = x0
    X[1] = y0

    # Compute differential equations.
    _f_dx = _f.diff(x, 1)
    _f_dy = _f.diff(y, 1)
    _f_dx_dx = _f_dx.diff(x, 1)
    _f_dx_dy = _f_dx.diff(y, 1)
    _f_dy_dx = _f_dy.diff(x, 1)
    _f_dy_dy = _f_dy.diff(y, 1)

    while True:
        # Compute gradient, dim 2x1.
        grad = np.zeros((2, 1), dtype=np.float)
        grad[0] = _f_dx.subs([(x, X[0]), (y, X[1])])
        grad[1] = _f_dy.subs([(x, X[0]), (y, X[1])])

        # Compute H matrix, dim 2x2.
        H = np.zeros((2, 2), dtype=np.float)
        H[0, 0] = _f_dx_dx.subs([(x, X[0]), (y, X[1])])
        H[0, 1] = _f_dx_dy.subs([(x, X[0]), (y, X[1])])
        H[1, 0] = _f_dy_dx.subs([(x, X[0]), (y, X[1])])
        H[1, 1] = _f_dy_dy.subs([(x, X[0]), (y, X[1])])

        # Compute new X, dim 2x1 - 2x2 * 2x1.
        X_NEW = X - np.dot(np.linalg.inv(H), grad)

        # If norm(X_NEW - X, 2) < eps, return x_min and y_min.
        if np.linalg.norm(X_NEW - X, 2) < eps:
            return X[0][0], X[1][0]

        X = X_NEW
