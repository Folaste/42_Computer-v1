import sys
from ft_math import ft_gcd, simplify_sqrt


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
    print()


def better_solution_deg2(a: float | int, b: float | int, discriminant: int, is_complex: bool) -> None:
    if is_complex is False:
        factor, root = simplify_sqrt(discriminant)
        a, b, factor = to_int(a, b, factor)
        print(a, b, factor, file=sys.stderr, flush=True)
        if a < 0:
            a *= -1
            b *= -1
            factor *= -1
        print(a, b, factor, root, file=sys.stderr, flush=True)
        print(f"{b} - {factor}√{root} / {a}")
        print(f"{b} + {factor}√{root} / {a}")
        # if a == 1:
        #     if root == 1:
        #         print("Cas 1", file=sys.stderr, flush=True)
        #         print(f"{b - factor}")
        #         print(f"{b + factor}")
        #     else:
        #         if factor == 1:
        #             print("Cas 2", file=sys.stderr, flush=True)
        #             print(f"{b} - √{root}")
        #             print(f"{b} + √{root}")
        #         else:
        #             print("Cas 3", file=sys.stderr, flush=True)
        #             print(f"{b} - {factor}√{root}")
        #             print(f"{b} + {factor}√{root}")
        # else:
        #     if root == 1:
        #         print("Cas 4", file=sys.stderr, flush=True)
        #         print(f"{b - factor} / {a}")
        #         print(f"{b + factor} / {a}")
        #     else:
        #         if factor == 1:
        #             print("Cas 5", file=sys.stderr, flush=True)
        #             print(f"{b} - √{root} / {a}")
        #             print(f"{b} + √{root} / {a}")
        #         else:
        #             print("Cas 6", file=sys.stderr, flush=True)
        #             print(f"{b} - {factor}√{root} / {a}")
        #             print(f"{b} + {factor}√{root} / {a}")
        print()
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
        print(args, file=sys.stderr, flush=True)
    else:
        # Convert the arguments to integers
        args = [int(arg) for arg in args]

    return tuple(args)
