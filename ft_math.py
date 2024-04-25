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


def ft_gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


def ft_prime_decomposition(n: int) -> list[int]:
    factors = []
    i = 2
    while i <= n:
        if n % i == 0:
            factors.append(i)
            n //= i
        else:
            i += 1

    return factors


def simplify_sqrt(factors: list[int]):
    factor = 1
    root = 1
    i = 0
    while i < len(factors) and len(factors) > 1:
        if factors[i] == factors[i + 1]:
            factor *= factors[i]
            factors.pop(i)
            factors.pop(i)
        else:
            i += 1
    for i in factors:
        root *= i

    return factor, root