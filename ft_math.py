import sys


def ft_pow(base: float | int, exponent: int) -> int | float:
    if exponent == 0:
        return 1
    if exponent < 0:
        return 1 / ft_pow(base, -exponent)
    return base * ft_pow(base, exponent - 1)


def ft_sqrt(number: int | float, epsilon=1e-14, max_iterations=2000) -> int | float:
    """ Returns an approximation of square root, using Newton-Raphson method."""

    if number == 0 or number == 1:
        return 0.0

    x = 1.

    for _ in range(max_iterations):
        x = (x + number / x) / 2

        if (x * x - number) < epsilon:
            return x

    print("ft_sqrt: no convergence")
    sys.exit(1)
