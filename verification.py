import sys
from colorama import Fore

from ft_math import ft_pow


def verify_solutions(solutions, terms):
    print(Fore.BLUE + "\n\nVERIFY SOLUTIONS FUNCTION", file=sys.stderr, flush=True)

    def f(z):
        return sum([term.result() * ft_pow(z, i) for i, term in enumerate(terms)])

    print("Verifying the solutions...")
    for solution in solutions:
        result = f(solution)
        print(f"Equation with solution {solution}: {round(result, 10)}")
    print("Verification complete.")
