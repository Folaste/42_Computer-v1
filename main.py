"""
Write a program that solves a polynomial equation of degree less than or equal to 2.
We have to show at least:
- The reduced form of the equation.
- The degree of the equation.
- It’s solution(s) and the polarity of the discriminant if it makes sense.
"""
import sys
from reduced_form import reduced_form


def main():
    print("Welcome to Computer_v1 !")
    if len(sys.argv) == 1:
        equation = input("Please enter the equation: ")
    elif len(sys.argv) == 2:
        equation = sys.argv[1]
    else:
        print("Error: Invalid number of arguments")
        print("Usage: python main.py <equation>")
        sys.exit(1)

    reduced_form(equation)


if __name__ == "__main__":
    main()
