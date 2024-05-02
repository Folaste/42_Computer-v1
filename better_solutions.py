import sys
from colorama import Fore

from ft_math import ft_gcd, simplify_sqrt, ft_abs


def better_solution_deg1(a: float | int, b: float | int) -> None:
    print(Fore.BLUE + "BETTER SOLUTION DEGREE 1 FUNCTION", file=sys.stderr, flush=True)
    # Turn a and b into integers to write a correct fraction
    a, b = to_int(a, b)
    print(Fore.MAGENTA + f"a {a}, b {b}", file=sys.stderr, flush=True)

    # Find the greatest common divisor of a and b
    b, a = simplify_fraction(b, a)

    # Simplify the fraction
    print(Fore.MAGENTA + f"a {a}, b {b}", file=sys.stderr, flush=True)

    # Remove minus sign at denominator
    if a < 0:
        a *= -1
        b *= -1

    # Print the solution
    if a == 1:
        print(f"{b}")
    else:
        print(f"{b} / {a}")
    print()


def better_solution_deg2(a, b, discriminant, is_complex):
    print(Fore.BLUE + "BETTER SOLUTION DEGREE 2 FUNCTION", file=sys.stderr, flush=True)

    if is_complex:
        discriminant = -discriminant

    factor, root = simplify_sqrt(discriminant)
    a, b, factor = to_int(a, b, factor)

    if a < 0:
        a, b, factor = -a, -b, -factor
    factor = ft_abs(factor)

    print(Fore.MAGENTA + f"General form: {b} ± {factor}√{root} / {a}", file=sys.stderr, flush=True)

    if root == 1 and not is_complex:
        num_pos, dem_pos = simplify_fraction(b + factor, a)
        num_neg, dem_neg = simplify_fraction(b - factor, a)

        # Print the solutions
        print(f"{num_neg if dem_neg == 1 else f'{num_neg} / {dem_neg}'}")
        print(f"{num_pos if dem_pos == 1 else f'{num_pos} / {dem_pos}'}")

    else:
        b, dem_first = simplify_fraction(b, a)
        factor, dem_second = simplify_fraction(factor, a)

        first_part = str(b) if dem_first == 1 else f"({b} / {dem_first})"

        if factor == 1:
            second_part = f"√{root}" if dem_second == 1 else f"√{root} / {dem_second}"
        else:
            second_part = f"{factor}√{root}" if dem_second == 1 else f"({factor}√{root} / {dem_second})"

        if dem_first == dem_second != 1 and not is_complex:
            print(f"({b} - √{root}) / {dem_first}" if factor == 1 else f"({b} - {factor}√{root}) / {dem_first}")
            print(f"({b} + √{root}) / {dem_first}" if factor == 1 else f"({b} + {factor}√{root}) / {dem_first}")
        else:
            result_1 = first_part + " - " + second_part
            result_2 = first_part + " + " + second_part

            if is_complex:
                result_1 += 'i'
                result_2 += 'i'

            print(result_1)
            print(result_2)
    print()


def simplify_fraction(numerator, denominator):
    gcd = ft_gcd(numerator, denominator)
    return numerator // gcd, denominator // gcd


def to_int(*args):
    # Convert the arguments to a list
    args = list(args)
    max_len = 0
    # Check if all the arguments are integers
    if not all(arg.is_integer() for arg in args):
        # Iterate through the arguments
        for i in range(len(args)):
            # Convert argument to string and split it at the decimal point
            args[i] = str(args[i]).split('.')
            # If the decimal part is empty, add a '0' to it
            if len(args[i]) == 1:
                args[i].append('0')
            # Find the max length of the decimal parts
            if len(args[i][1]) > max_len:
                max_len = len(args[i][1])

        # Make the decimal part the same length
        for i in range(len(args)):
            while len(args[i][1]) != max_len:
                args[i][1] += '0'

        # Combine the integer part and the decimal part
        for i in range(len(args)):
            args[i] = int(args[i][0] + args[i][1])
            print(Fore.MAGENTA + f"{args[i]}", file=sys.stderr, flush=True)

    else:
        # Convert the arguments to integers
        args = [int(arg) for arg in args]

    return tuple(args)
