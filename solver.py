import sys
from colorama import Fore


def solve_equation(terms: list[float]):
    print(Fore.BLUE + "\n\nSOLVE EQUATION FUNCTION", file=sys.stderr, flush=True)
    degree = len(terms) - 1
    print("Polynomial degree:", degree)

    if degree == 0:
        solve_degree_0(terms)
    elif degree == 1:
        solve_degree_1(terms)
    elif degree == 2:
        solve_degree_2(terms)
    else:
        print("The polynomial degree is strictly greater than 2, I can't solve.")


def solve_degree_0(terms: list[float]):
    print(Fore.GREEN + "SOLVE DEGREE 0 FUNCTION", file=sys.stderr, flush=True)
    if terms[0] == 0:
        print("All real numbers are solutions.")
    else:
        print("There is no solution for the equation.")


def solve_degree_1(terms: list[float]):
    print(Fore.GREEN + "SOLVE DEGREE 1 FUNCTION", file=sys.stderr, flush=True)
    b = terms[0]
    a = terms[1]
    result = -b / a
    print("The solution is:")
    print(result)


def solve_degree_2(terms: list[float]):
    print(Fore.GREEN + "SOLVE DEGREE 2 FUNCTION", file=sys.stderr, flush=True)
    a = terms[2]
    b = terms[1]
    c = terms[0]
    discriminant = b ** 2 - 4 * a * c
    print("Discriminant:", discriminant, file=sys.stderr, flush=True)
    if discriminant > 0:
        print("Discriminant is strictly positive, the two solutions are:")
        x1 = (-b - discriminant ** 0.5) / (2 * a)
        x2 = (-b + discriminant ** 0.5) / (2 * a)
        print(x1)
        print(x2)
    elif discriminant == 0:
        print("Discriminant is equal to 0, the solution is:")
        x = -b / (2 * a)
        print(x)
    else:
        print("Discriminant is strictly negative, the two complex solutions are:")
        z1_re = -b / (2 * a)
        z1_im = (-discriminant) ** 0.5 / (2 * a)
        z2_re = -b / (2 * a)
        z2_im = -(-discriminant) ** 0.5 / (2 * a)
        print(f"{z1_re} + {z1_im}i")
        print(f"{z2_re} - {z2_im}i")
