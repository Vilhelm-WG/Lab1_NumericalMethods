"""Own implementations of bracketing root-finding methods: bisection and chord."""
from typing import Callable, List, Tuple


def bisect_sf(
    f: Callable[[float], float],
    a: float,
    b: float,
    eps: float = 1e-3,
    maxiter: int = 100,
) -> Tuple[float, int, float, List[float]]:
    """Find a root of f on [a, b] via the bisection method.
    Returns (root, iterations, residual, history of |f(x_n)|).
    """
    if f(a) * f(b) >= 0:
        raise ValueError("f(a) and f(b) must have opposite signs")

    history: List[float] = []
    c = (a + b) / 2
    iterations = 0

    for iterations in range(1, maxiter + 1):
        c = (a + b) / 2
        history.append(abs(f(c)))

        if abs(b - a) < 2 * eps:
            break

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return c, iterations, abs(f(c)), history


def chord_sf(
    f: Callable[[float], float],
    a: float,
    b: float,
    eps: float = 1e-3,
    maxiter: int = 500,
) -> Tuple[float, int, float, List[float]]:
    """Find a root of f on [a, b] via the chord (regula falsi) method.
    Returns (root, iterations, residual, history of |f(x_n)|).
    """
    if f(a) * f(b) >= 0:
        raise ValueError("f(a) and f(b) must have opposite signs")

    history: List[float] = []
    c_prev = a
    c = b
    iterations = 0

    for iterations in range(1, maxiter + 1):
        c = b - f(b) * (b - a) / (f(b) - f(a))
        fc = f(c)
        history.append(abs(fc))

        if abs(fc) < eps or abs(c - c_prev) < eps:
            break

        if f(a) * fc < 0:
            b = c
        else:
            a = c
        c_prev = c

    return c, iterations, abs(f(c)), history
