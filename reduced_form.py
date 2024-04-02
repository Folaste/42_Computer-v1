import sys


# TODO: Mettre au propre
def reduced_form(equation) -> list[int]:
    # Trim spaces from the equation
    equation = equation.replace(" ", "")
    print(equation, file=sys.stderr, flush=True)

    # Split the equation into left and right parts
    left, right = equation.split("=")
    print("\n\nAFTER SPLITTING", file=sys.stderr, flush=True)
    print("left: " + left, file=sys.stderr, flush=True)
    print("right: " + right, file=sys.stderr, flush=True)

    # Split parts into terms
    left = left.replace("+", " ").replace("-", " -")
    right = right.replace("+", " ").replace("-", " -")
    left_terms = left.split(" ")
    right_terms = right.split(" ")
    print("\n\nAFTER SPLITTING INTO TERMS", file=sys.stderr, flush=True)
    print("left: ", left_terms, file=sys.stderr, flush=True)
    print("right: ", right_terms, file=sys.stderr, flush=True)

    # Create list of values
    # terms = left_terms + right_terms
    left_values = []
    print("\n\nLEFT TERMS LOOP", file=sys.stderr, flush=True)
    for term in left_terms:
        print(term, file=sys.stderr, flush=True)
        value = term.split("*X^")
        value = int(value[0]), int(value[1])
        left_values.append(value)
    print(left_values, file=sys.stderr, flush=True)

    right_values = []
    print("\n\nRIGHT TERMS LOOP", file=sys.stderr, flush=True)
    for term in right_terms:
        print(term, file=sys.stderr, flush=True)
        value = term.split("*X^")
        value = int(value[0]), int(value[1])
        right_values.append(value)
    print(right_values, file=sys.stderr, flush=True)

    # Find the max degree of the equation
    max_degree_l = max(left_values, key=lambda x: x[1])[1]
    max_degree_r = max(right_values, key=lambda x: x[1])[1]
    max_degree = max(max_degree_l, max_degree_r)
    print("\n\nDEGREE THEORETICAL", max_degree, file=sys.stderr, flush=True)

    # Create lists of coefficients
    left_coefficients = [0] * (max_degree + 1)
    for value in left_values:
        left_coefficients[value[1]] = value[0]
    print("\n\nLEFT COEFFICIENTS", left_coefficients, file=sys.stderr, flush=True)

    right_coefficients = [0] * (max_degree + 1)
    for value in right_values:
        right_coefficients[value[1]] = value[0]
    print("RIGHT COEFFICIENTS", right_coefficients, file=sys.stderr, flush=True)

    # Subtract right coefficients from left coefficients\
    reduced_coefficients = [left - right for left, right in zip(left_coefficients, right_coefficients)]
    # Remove trailing zeros
    # TODO: Prevent if all zeros in list
    while reduced_coefficients and reduced_coefficients[-1] == 0:
        reduced_coefficients.pop()
    print("\n\nREDUCED COEFFICIENTS", reduced_coefficients, file=sys.stderr, flush=True)

    # Create the reduced form
    last_reduced_form = ""
    for i, coefficient in enumerate(reduced_coefficients):
        if i == 0:
            last_reduced_form += f"{coefficient} * X^{i}"
        elif coefficient < 0:
            last_reduced_form += f" - {-coefficient} * X^{i}"
        else:
            last_reduced_form += f" + {coefficient} * X^{i}"
    last_reduced_form += " = 0"

    print("Reduced form: " + last_reduced_form)
    print("Degree:", len(reduced_coefficients) - 1)

    return reduced_coefficients
