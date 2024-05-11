import sys

from colorama import Fore

from fraction import Fraction
from ft_math import ft_pow


def verify_solutions(solutions: list[float], terms: list[Fraction]) -> None:
    print(Fore.BLUE + "\n\nVERIFY SOLUTIONS FUNCTION", file=sys.stderr, flush=True)

    def f(z):
        return sum([term.result() * ft_pow(z, i) for i, term in enumerate(terms)])

    print("Verifying the solutions...")
    for solution in solutions:
        result = f(solution)
        print(f"Equation with solution {round(solution, 5)}: {round(result, 10)}")
    print("Verification complete.")
