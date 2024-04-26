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
        pass
    else:
        pass


def to_int(*args):
    # Convert the arguments to a list
    args = list(args)
    # Check if all the arguments are integers
    if not all(arg.is_integer() for arg in args):
        # Iterate through the arguments
        for arg in args:
            # Convert argument to string
            arg = str(arg)
            # Split the float into two parts, the integer part and the decimal part
            arg = arg.split('.')
            # If the decimal part is empty, add a '0' to it
            if len(arg) == 1:
                arg.append('0')

        # Find the max length of the decimal parts
        max_len = max(len(arg[1]) for arg in args)

        # Make the decimal part the same length
        for i in range(len(args)):
            while len(args[i][1]) != max_len:
                args[i][1] += '0'

        # Combine the integer part and the decimal part
        for i in range(len(args)):
            args[i] = int(args[i][0] + args[i][1])

    return tuple(args)
