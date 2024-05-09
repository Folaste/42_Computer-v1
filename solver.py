import sys
from colorama import Fore
from complex import Complex
from ft_math import ft_pow, ft_sqrt
from better_solutions import better_solutions


def solve_equation(terms):
    print(Fore.BLUE + "\n\nSOLVE EQUATION FUNCTION", file=sys.stderr, flush=True)
    degree = len(terms) - 1
    print("Polynomial degree:", degree, "\n")

    solutions = None
    if degree == 0:
        solve_degree_0(terms)
    elif degree == 1:
        solutions = solve_degree_1(terms)
    elif degree == 2:
        solutions = solve_degree_2(terms)
    else:
        print("The polynomial degree is strictly greater than 2, I can't solve.")
        solutions = None
    return solutions


def solve_degree_0(terms) -> None:
    print(Fore.GREEN + "SOLVE DEGREE 0 FUNCTION", file=sys.stderr, flush=True)
    if terms[0] == 0:
        print("All real numbers are solutions.")
    else:
        print("There is no solution for the equation.")


# IN : list[Fraction]
def solve_degree_1(terms):
    print(Fore.GREEN + "SOLVE DEGREE 1 FUNCTION", file=sys.stderr, flush=True)
    b = terms[0]
    a = terms[1]
    x = -b / a
    print("The solution is:")
    print(x, "\n")
    return [x.result()]


# IN : list[Fraction]
def solve_degree_2(terms):
    print(Fore.GREEN + "SOLVE DEGREE 2 FUNCTION", file=sys.stderr, flush=True)
    a = terms[2]
    b = terms[1]
    c = terms[0]
    discriminant = ft_pow(b, 2) - 4 * a * c
    discriminant = discriminant.result()
    print("Discriminant:", discriminant)

    a_float = a.result()
    b_float = b.result()

    if discriminant > 0:
        print(Fore.YELLOW + "POSITIVE DISCRIMINANT", file=sys.stderr, flush=True)
        print("Discriminant is strictly positive, the two solutions are:")
        x1 = (-b_float / (2 * a_float)) - (ft_sqrt(discriminant) / (2 * a_float))
        x2 = (-b_float / (2 * a_float)) + (ft_sqrt(discriminant) / (2 * a_float))
        if discriminant.is_integer() is False:
            print(x1)
            print(x2, "\n")
        else:
            better_solutions(2 * a, -b, int(discriminant), False)
        return [x1, x2]

    elif discriminant == 0:
        print(Fore.YELLOW + "NULL DISCRIMINANT", file=sys.stderr, flush=True)
        print("Discriminant is equal to 0, the solution is:")
        x = -b / (2 * a)
        print(x, "\n")
        return [x.result()]

    else:
        print(Fore.YELLOW + "NEGATIVE DISCRIMINANT", file=sys.stderr, flush=True)
        print("Discriminant is strictly negative, the two complex solutions are:")
        z1 = Complex(-b_float / (2 * a_float), -ft_sqrt(-discriminant) / (2 * a_float))
        z2 = Complex(-b_float / (2 * a_float), ft_sqrt(-discriminant) / (2 * a_float))
        if discriminant.is_integer() is False:
            print(z1)
            print(z2, "\n")
        else:
            better_solutions(2 * a, -b, int(discriminant), True)
        return [z1, z2]
