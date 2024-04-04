"""
Write a program that solves a polynomial equation of degree less than or equal to 2.
We have to show at least:
- The reduced form of the equation.
- The degree of the equation.
- It’s solution(s) and the polarity of the discriminant if it makes sense.
"""
import sys
from reduced_form import reduced_form
from solver import solve_equation
from colorama import init




def main():
    print("Welcome to Computer_v1 !")
    if len(sys.argv) == 1:
        try:
            equation = input("Please enter the equation: ")
        except EOFError:
            print()
            sys.exit(1)

    elif len(sys.argv) == 2:
        equation = sys.argv[1]

    else:
        print("Error: Invalid number of arguments")
        print("Usage: python main.py <equation>")
        sys.exit(1)

    # print("Equation:", equation)
    terms = reduced_form(equation)
    solve_equation(terms)


if __name__ == "__main__":
    init(autoreset=True)
    main()
