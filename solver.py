import sys
from colorama import Fore
from complex import Complex
from ft_math import ft_pow, ft_sqrt


def solve_equation(terms: list[float]) -> list[float | Complex] | None:
    # print(Fore.BLUE + "\n\nSOLVE EQUATION FUNCTION", file=sys.stderr, flush=True)
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


def solve_degree_0(terms: list[float]) -> None:
    # print(Fore.GREEN + "SOLVE DEGREE 0 FUNCTION", file=sys.stderr, flush=True)
    if terms[0] == 0:
        print("All real numbers are solutions.")
    else:
        print("There is no solution for the equation.")


def solve_degree_1(terms: list[float]) -> list[float]:
    # print(Fore.GREEN + "SOLVE DEGREE 1 FUNCTION", file=sys.stderr, flush=True)
    b = terms[0]
    a = terms[1]
    result = -b / a
    print("The solution is:")
    print(result, "\n")
    return [result]


def solve_degree_2(terms: list[float]) -> list[float | Complex]:
    # print(Fore.GREEN + "SOLVE DEGREE 2 FUNCTION", file=sys.stderr, flush=True)
    a = terms[2]
    b = terms[1]
    c = terms[0]
    discriminant = ft_pow(b, 2) - 4 * a * c
    print("Discriminant:", discriminant)

    if discriminant > 0:
        print("Discriminant is strictly positive, the two solutions are:")
        x1 = (-b - ft_sqrt(discriminant)) / (2 * a)
        x2 = (-b + ft_sqrt(discriminant)) / (2 * a)
        print(x1)
        print(x2, "\n")
        return [x1, x2]

    elif discriminant == 0:
        print("Discriminant is equal to 0, the solution is:")
        x = -b / (2 * a)
        print(x, "\n")
        return [x]

    else:
        print("Discriminant is strictly negative, the two complex solutions are:")
        z1 = Complex(0, 0)
        z2 = Complex(0, 0)
        z1.re = z2.re = -b / (2 * a)
        z1.im = ft_sqrt(-discriminant) / (2 * a)
        z2.im = -z1.im
        print(z1)
        print(z2, "\n")
        return [z1, z2]
