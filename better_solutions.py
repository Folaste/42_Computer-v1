import sys
from colorama import Fore

from ft_math import ft_gcd, simplify_sqrt


def better_solution_deg1(a: float | int, b: float | int) -> None:
    # Turn a and b into integers to write a correct fraction
    a, b = to_int(a, b)
    print(Fore.MAGENTA + a, b, file=sys.stderr, flush=True)

    # Find the greatest common divisor of a and b
    gcd = ft_gcd(a, b)
    print(Fore.MAGENTA + f"{gcd}", file=sys.stderr, flush=True)

    # Simplify the fraction
    b //= gcd
    a //= gcd
    print(Fore.MAGENTA + a, b, file=sys.stderr, flush=True)

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


def better_solution_deg2(a: float | int, b: float | int, discriminant: int) -> None:
    # Case where the discriminant is positive
    if discriminant > 0:

        # Simplify the discriminant
        factor, root = simplify_sqrt(discriminant)

        # Turn a, b and factor into integers to write a correct fraction
        a, b, factor = to_int(a, b, factor)
        print(Fore.MAGENTA + a, b, factor, file=sys.stderr, flush=True)

        # Remove minus sign at denominator
        if a < 0:
            a *= -1
            b *= -1
            factor *= -1

        # General case
        print(Fore.MAGENTA + f"{b} ± {factor}√{root} / {a}", file=sys.stderr, flush=True)

        # No root case
        if root == 1:
            dem_pos = dem_neg = a

            # Simplify the positive fraction
            num_pos = b + factor
            gcd_pos = ft_gcd(num_pos, dem_pos)
            num_pos //= gcd_pos
            dem_pos //= gcd_pos

            # Simplify the negative fraction
            num_neg = b - factor
            gcd_neg = ft_gcd(num_neg, dem_neg)
            num_neg //= gcd_neg
            dem_neg //= gcd_neg

            # Print the solution
            if dem_pos == 1:
                print(num_pos)
            else:
                print(f"{num_pos} / {dem_pos}")

            if dem_neg == 1:
                print(num_neg)
            else:
                print(f"{num_neg} / {dem_neg}")

        # Root case
        else:
            # Find the greatest common divisor of a, b and factor
            gcd = ft_gcd(a, b)
            gcd = ft_gcd(gcd, factor)
            print(Fore.MAGENTA + f"{gcd}", file=sys.stderr, flush=True)

            # Simplify the fraction
            b //= gcd
            a //= gcd
            factor //= gcd

            # Print the solution
            if factor == 1:
                if a == 1:
                    print(f"{b} - √{root}")
                    print(f"{b} + √{root}")
                else:
                    print(f"{b} - √{root} / {a}")
                    print(f"{b} + √{root} / {a}")
            else:
                if a == 1:
                    print(f"{b} - {factor}√{root}")
                    print(f"{b} + {factor}√{root}")
                else:
                    print(f"{b} - {factor}√{root} / {a}")
                    print(f"{b} + {factor}√{root} / {a}")

    # Case where the discriminant is negative (Cannot be null)
    else:
        # Simplify the discriminant
        factor, root = simplify_sqrt(-discriminant)

        # Turn a, b and factor into integers to write a correct fraction
        a, b, factor = to_int(a, b, factor)
        print(Fore.MAGENTA + a, b, factor, file=sys.stderr, flush=True)

        # Remove minus sign at denominator
        if a < 0:
            a *= -1
            b *= -1
            factor *= -1

        # General case
        print(Fore.MAGENTA + f"{b} / {a} ± {factor}√{root}i / {a}", file=sys.stderr, flush=True)

        dem_re = dem_im = a

        # Simplify the real part
        gcd_re = ft_gcd(b, dem_re)
        b //= gcd_re
        dem_re //= gcd_re

        if dem_re == 1:
            re_part = str(b)
        else:
            re_part = f"{b} / {dem_re}"

        # Simplify the imaginary part
        gcd_im = ft_gcd(factor, dem_im)
        factor //= gcd_im
        dem_im //= gcd_im

        if root == 1:
            if dem_im == 1:
                if factor == 1:
                    im_part = 'i'
                else:
                    im_part = str(factor) + "i"
            else:
                im_part = f"{factor}i / {dem_im}"
        else:
            if dem_im == 1:
                if factor == 1:
                    im_part = f"√{root}i"
                else:
                    im_part = f"{factor}√{root}i"
            else:
                im_part = f"{factor}√{root}i / {dem_im}"

        print(re_part + " - " + im_part)
        print(re_part + " + " + im_part)
    print()


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
            print(Fore.MAGENTA + args[i], file=sys.stderr, flush=True)

    else:
        # Convert the arguments to integers
        args = [int(arg) for arg in args]

    return tuple(args)
