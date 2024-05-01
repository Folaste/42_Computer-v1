import sys

from complex import Complex


def ft_pow(base: float | int | Complex, exponent: int) -> int | float | Complex:
    """ Returns base raised to the power of exponent. """
    if isinstance(base, Complex):
        return base.ft_pow(exponent)

    if exponent == 0:
        return 1
    if exponent < 0:
        return 1 / ft_pow(base, -exponent)
    return base * ft_pow(base, exponent - 1)


def ft_sqrt(number: int | float, epsilon=1e-10, max_iterations=8000) -> int | float:
    """ Returns an approximation of square root, using Newton-Raphson method."""

    if number == 0:
        return 0.0

    x = 1.

    for _ in range(max_iterations):
        x = (x + number / x) / 2

        if (x * x - number) < epsilon:
            return x

    print("ft_sqrt: no convergence")
    sys.exit(1)


def ft_gcd(a: int, b: int) -> int:
    """ Returns the greatest common divisor of a and b. """
    a = ft_abs(a)
    b = ft_abs(b)
    while b:
        a, b = b, a % b
    return a


def ft_prime_decomposition(n: int) -> list[int]:
    """ Returns the prime decomposition of n. """
    factors = []
    i = 2
    while i <= n:
        if n % i == 0:
            factors.append(i)
            n //= i
        else:
            i += 1

    return factors


def simplify_sqrt(n: int) -> tuple[float, int]:
    """ Returns the simplified form of the square root of n as a tuple (factor, root) using prime decomposition."""
    factor = 1
    root = 1
    i = 0

    factors = ft_prime_decomposition(n)
    while i < len(factors) - 1:
        if factors[i] == factors[i + 1]:
            factor *= factors[i]
            factors.pop(i)
            factors.pop(i)
        else:
            i += 1

    for i in factors:
        root *= i

    return float(factor), root


def ft_abs(n: int | float) -> int | float:
    """ Returns the absolute value of n. """
    if n < 0:
        return -n
    return n
