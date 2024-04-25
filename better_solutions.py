import sys
from ft_math import ft_gcd, ft_prime_decomposition, simplify_sqrt


def better_solution_deg1(a: float | int, b: float | int) -> None:
    a, b = to_int(a, b)
    print(a, b, file=sys.stderr, flush=True)
    gcd = ft_gcd(a, b)
    print(gcd, file=sys.stderr, flush=True)
    b //= gcd
    a //= gcd
    if a < 0:
        a *= -1
        b *= -1
    if a == 1:
        print(f"{b}")
    else:
        print(f"{b} / {a}")


def better_solution_deg2(a: float | int, b: float | int, discriminant: int, is_complex: bool) -> None:
    if is_complex is False:
        factors = ft_prime_decomposition(discriminant)
        print(factors, file=sys.stderr, flush=True)
        factor, root = simplify_sqrt(factors)
        a. b = to_int(a, b)

        pass
    else:
        pass


def to_int(a, b):
    if isinstance(a, float) or isinstance(b, float):
        # Split the float into two parts, the integer part and the decimal part
        a = str(a)
        b = str(b)
        a = a.split('.')
        b = b.split('.')
        # print(a, b, file=sys.stderr, flush=True)

        # If the decimal part is empty, add a '0' to it
        if len(a) == 1:
            a.append('0')
        if len(b) == 1:
            b.append('0')

        # Make the decimal part the same length
        while len(a[1]) != len(b[1]):
            if len(a[1]) > len(b[1]):
                b[1] += '0'
            else:
                a[1] += '0'
        # print(a, b, file=sys.stderr, flush=True)

        # Combine the integer part and the decimal part
        a = int(a[0] + a[1])
        b = int(b[0] + b[1])

    return a, b
