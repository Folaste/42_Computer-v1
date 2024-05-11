import sys

from colorama import Fore

from fraction import Fraction
from ft_math import simplify_sqrt, ft_abs


def better_solutions(a: Fraction, b: Fraction, discriminant: int, is_complex: bool) -> None:
    print(Fore.BLUE + "BETTER SOLUTION DEGREE 2 FUNCTION", file=sys.stderr, flush=True)

    if is_complex:
        discriminant = -discriminant
    factor, root = simplify_sqrt(discriminant)

    print(Fore.MAGENTA + f"Factor: {factor}, Root: {root}", file=sys.stderr, flush=True)

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
        num_second = ft_abs(second_part.numerator)
        dem_second = second_part.denominator

        if num_second == 1:
            second_part = f"√{root}" if dem_second == 1 else f"√{root} / {dem_second}"
        else:
            second_part = f"{num_second}√{root}" if dem_second == 1 else f"({num_second}√{root} / {dem_second})"

        if dem_first == dem_second != 1 and not is_complex:
            print(f"({num_first} - √{root}) / {dem_first}" if num_second == 1
                  else f"({num_first} - {num_second}√{root}) / {dem_first}")
            print(f"({num_first} + √{root}) / {dem_first}" if num_second == 1
                  else f"({num_first} + {num_second}√{root}) / {dem_first}")
        else:
            result_1 = f"{first_part} - ({second_part})"
            result_2 = f"{first_part} + ({second_part})"

            if is_complex:
                result_1 += 'i'
                result_2 += 'i'

            print(result_1)
            print(result_2)
    print()


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
