import sys
from colorama import Fore

from ft_math import ft_gcd, simplify_sqrt, ft_abs
from fraction import Fraction


def better_solutions(a, b, discriminant, is_complex):
    print(Fore.BLUE + "BETTER SOLUTION DEGREE 2 FUNCTION", file=sys.stderr, flush=True)

    if is_complex:
        discriminant = -discriminant
    factor, root = simplify_sqrt(discriminant)

    # print(Fore.MAGENTA + f"General form: {b} ± {factor}√{root} / {a}", file=sys.stderr, flush=True)

    if root == 1 and not is_complex:
        x1 = Fraction(b.result() - factor, a.result())
        x2 = Fraction(b.result() + factor, a.result())

        print(x1)
        print(x2)

    else:
        first_part = Fraction(b.result(), a.result())
        second_part = Fraction(factor, a.result())

        num_first = first_part.numerator
        dem_first = first_part.denominator
        num_second = second_part.numerator
        dem_second = second_part.denominator

        if num_second == 1:
            second_part = f"√{root}" if dem_second == 1 else f"√{root} / {dem_second}"
        else:
            second_part = f"{num_second}√{root}" if dem_second == 1 else f"({num_second}√{root} / {dem_second})"

        if dem_first == dem_second != 1 and not is_complex:
            print(f"({num_first} - √{root}) / {dem_first}" if factor == 1
                  else f"({num_first} - {factor}√{root}) / {dem_first}")
            print(f"({num_first} + √{root}) / {dem_first}" if factor == 1
                  else f"({num_first} + {factor}√{root}) / {dem_first}")
        else:
            result_1 = f"{first_part} - ({second_part})"
            result_2 = f"{first_part} + ({second_part})"

            # if root != 1:
            #     result_1 += f"√{root}"
            #     result_2 += f"√{root}"

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
