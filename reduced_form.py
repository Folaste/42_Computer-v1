import sys
from colorama import Fore

from fraction import Fraction


def reduced_form(equation):
    print(Fore.BLUE + "REDUCED FORM FUNCTION", file=sys.stderr, flush=True)
    left, right = split_equation(equation)
    print(Fore.MAGENTA + f"Left part: {left}\nRight part: {right}", file=sys.stderr, flush=True)

    # Split parts into terms
    left = split_into_terms(left)
    right = split_into_terms(right)
    print(Fore.MAGENTA + f"\nLeft terms: {left}\nRight terms: {right}", file=sys.stderr, flush=True)

    # Create list of values
    left = get_values(left)
    right = get_values(right)
    print(Fore.MAGENTA + f"\nLeft values: {left}\nRight values: {right}", file=sys.stderr, flush=True)

    # Find the degree theoretical of the equation
    degree_th = max(max(left, key=lambda x: x[1])[1], max(right, key=lambda x: x[1])[1])
    print(Fore.MAGENTA + f"\nDegree theoretical: {degree_th}", file=sys.stderr, flush=True, sep="\n\n")

    # Create lists of coefficients
    left = get_coefficients(left, degree_th)
    right = get_coefficients(right, degree_th)
    print(Fore.MAGENTA + f"\nLeft coefficients: {left}", file=sys.stderr, flush=True)
    print(Fore.MAGENTA + f"Right coefficients: {right}", file=sys.stderr, flush=True)

    # Get the reduced coefficients
    reduced_coefficients = get_reduced_coefficients(left, right)
    print(Fore.MAGENTA + f"\nReduced coefficients: {reduced_coefficients}", file=sys.stderr, flush=True)

    # Create the reduced form
    str_reduced_form = create_reduced_form(reduced_coefficients)

    # Print the reduced form
    print("Reduced form: " + str_reduced_form, "\n")
    return reduced_coefficients


def split_equation(equation):
    # Trim spaces from the equation
    equation = equation.replace(" ", "")
    # Split the equation into left and right parts
    left, right = equation.split("=")
    return left, right


def split_into_terms(part):
    part = part.replace("+", " ").replace("-", " -")
    while part[0] == " ":
        part = part[1:]
    terms = part.split(" ")
    return terms


def get_values(terms):
    values = []
    for term in terms:
        value = term.split("*X^")
        if value[0].find("/") != -1:
            division = value[0].split("/")
            value = Fraction(float(division[0]), float(division[1])), int(value[1])
        else:
            value = Fraction(float(value[0]), 1.0), int(value[1])
        values.append(value)
    return values


def get_coefficients(values, max_degree):
    coefficients = [Fraction(0.0, 1.0)] * (max_degree + 1)
    for value in values:
        coefficients[value[1]] += value[0]
    return coefficients


def get_reduced_coefficients(left_coefficients, right_coefficients):
    reduced_coefficients = [left - right for left, right in zip(left_coefficients, right_coefficients)]
    # Remove trailing zeros
    while reduced_coefficients and reduced_coefficients[-1] == 0 and len(reduced_coefficients) > 1:
        reduced_coefficients.pop()
    return reduced_coefficients


def create_reduced_form(reduced_coefficients):
    string = ""
    for i, coefficient in enumerate(reduced_coefficients):
        if i == 0 and coefficient != 0:
            string += f"{coefficient} * X^{i}"
        elif coefficient == 0:
            continue
        elif coefficient < 0:
            string += f" - {-coefficient} * X^{i}"
        else:
            string += f" + {coefficient} * X^{i}"
    string += " = 0"
    return string
