from typing import Callable, Tuple


def find_min_border(f: Callable,
                    start: float = 0.0,
                    init_step: float = 0.25,
                    step_expand: float = 1.1,
                    max_iters: int = 10) -> Tuple[float, float]:
    """
    Looking for an approximate limit for the minimum value of the function.

    """
    x0 = start
    x1 = start
    r0 = f(x0)

    # Go right.
    iterations_count = 0
    step = init_step
    while True:
        if iterations_count == max_iters:
            return x0, x1

        x1 = x0 + step
        r1 = f(x1)

        if r1 > r0:
            break

        x0 = x1
        r0 = r1
        step *= step_expand
        iterations_count += 1
    right = x1

    # Go left.
    iterations_count = 0
    step = init_step
    while True:
        if iterations_count == max_iters:
            return x0, right

        x1 = x0 - step
        r1 = f(x1)

        if r1 > r0:
            break

        x0 = x1
        r0 = r1
        step *= step_expand
        iterations_count += 1
    left = x0

    return left, right
