import matplotlib.pyplot as plt
import numpy as np

from fraction import Fraction
from ft_math import ft_pow


def plot_equation(terms: list[Fraction]) -> None:
    print("Plotting the equation...\n")

    def term_result(term):
        return term.result()

    v_term_result = np.vectorize(term_result)

    def f(z):
        return sum([v_term_result(term) * ft_pow(z, i) for i, term in enumerate(terms)])

    x = np.linspace(-5, 5, 1000)
    y = f(x)

    plt.plot(x, y)

    # plt.xlim(-5, 5)
    plt.ylim(-5, 5)

    ax = plt.gca()
    ax.spines['left'].set_position('center')  # Put y-axis at the center
    ax.spines['bottom'].set_position('center')  # Put x-axis at the center
    ax.spines['right'].set_color('none')  # Delete the y-axis on the right
    ax.spines['top'].set_color('none')  # Delete the x-axis on the top

    ax.xaxis.set_label_coords(0, 1.04)
    ax.yaxis.set_label_coords(1.03, 0)

    plt.xlabel("f(x)", fontweight="bold")
    plt.ylabel("x", fontweight="bold", rotation=0)
    plt.title("Plot of the equation", fontweight="bold", fontsize=20, loc="center", pad=20)
    plt.grid()
    plt.show()
