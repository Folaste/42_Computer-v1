"""
Write a program that solves a polynomial equation of degree less than or equal to 2.
We have to show at least:
- The reduced form of the equation.
- The degree of the equation.
- It’s solution(s) and the polarity of the discriminant if it makes sense.
"""

import sys

from colorama import init

from plot_equation import plot_equation
from reduced_form import reduced_form
from solver import solve_equation
from verification import verify_solutions


def main():
    print("Welcome to Computor_v1 !\n")

    if len(sys.argv) == 1:  # No arguments
        try:
            equation = input("Please enter the equation: ")
        except EOFError:
            print()
            sys.exit(1)

    elif len(sys.argv) == 2:  # One argument
        equation = sys.argv[1]

    else:
        print("Error: Invalid number of arguments")
        print("Usage: python computor.py <equation>")
        sys.exit(1)

    print("Equation:", equation, "\n")
    terms = reduced_form(equation)

    if len(terms) - 1 <= 2:
        plot_equation(terms)

    solutions = solve_equation(terms)

    if solutions is not None:
        verify_solutions(solutions, terms)


if __name__ == "__main__":
    init(autoreset=True)
    main()
