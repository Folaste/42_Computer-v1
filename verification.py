from ft_math import ft_pow


def verify_solutions(solutions, terms):
    def f(z):
        return sum([term * ft_pow(z, i) for i, term in enumerate(terms)])

    print("Verifying the solutions...")
    for solution in solutions:
        result = f(solution)
        print(f"Equation with solution {solution}: {result}")
    print("Verification complete.")
