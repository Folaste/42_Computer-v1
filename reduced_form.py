import sys


def reduced_form(equation: str) -> list[int]:
    left, right = split_equation(equation)
    print("Left part:", left, "\nRight part:", right, file=sys.stderr, flush=True)

    # Split parts into terms
    left_terms = split_into_terms(left)
    right_terms = split_into_terms(right)
    print("\nLeft terms:", left_terms, "\nRight terms:", right_terms, file=sys.stderr, flush=True)

    # Create list of values
    left_values = get_values(left_terms)
    right_values = get_values(right_terms)
    print("\nLeft values:", left_values, "\nRight values:", right_values, file=sys.stderr, flush=True)

    # Find the max degree theoretical of the equation
    max_degree_th = max(max(left_values, key=lambda x: x[1])[1], max(right_values, key=lambda x: x[1])[1])
    print("\nMax degree theoretical:", max_degree_th, file=sys.stderr, flush=True)

    # Create lists of coefficients
    left_coefficients = get_coefficients(left_values, max_degree_th)
    right_coefficients = get_coefficients(right_values, max_degree_th)
    print("\nLeft coefficients:", left_coefficients, file=sys.stderr, flush=True)
    print("Right coefficients:", right_coefficients, file=sys.stderr, flush=True)

    # Get the reduced coefficients
    reduced_coefficients = get_reduced_coefficients(left_coefficients, right_coefficients)
    print("\nReduced coefficients:", reduced_coefficients, file=sys.stderr, flush=True)

    # Create the reduced form
    str_reduced_form = create_reduced_form(reduced_coefficients)

    # Print the reduced form
    print("Reduced form: " + str_reduced_form)
    return reduced_coefficients


def split_equation(equation: str) -> tuple[str, str]:
    # Trim spaces from the equation
    equation = equation.replace(" ", "")
    # Split the equation into left and right parts
    left, right = equation.split("=")
    return left, right


def split_into_terms(part: str) -> list[str]:
    part = part.replace("+", " ").replace("-", " -")
    terms = part.split(" ")
    return terms


def get_values(terms: list[str]) -> list[tuple[int, int]]:
    values = []
    for term in terms:
        value = term.split("*X^")
        value = int(value[0]), int(value[1])
        values.append(value)
    return values


def get_coefficients(values: list[tuple[int, int]], max_degree: int) -> list[int]:
    coefficients = [0] * (max_degree + 1)
    for value in values:
        coefficients[value[1]] = value[0]
    return coefficients


def get_reduced_coefficients(left_coefficients: list[int], right_coefficients: list[int]) -> list[int]:
    reduced_coefficients = [left - right for left, right in zip(left_coefficients, right_coefficients)]
    # Remove trailing zeros
    while reduced_coefficients and reduced_coefficients[-1] == 0 and len(reduced_coefficients) > 1:
        reduced_coefficients.pop()
    return reduced_coefficients


def create_reduced_form(reduced_coefficients: list[int]) -> str:
    string = ""
    for i, coefficient in enumerate(reduced_coefficients):
        if i == 0:
            string += f"{coefficient} * X^{i}"
        elif coefficient < 0:
            string += f" - {-coefficient} * X^{i}"
        else:
            string += f" + {coefficient} * X^{i}"
    string += " = 0"
    return string
