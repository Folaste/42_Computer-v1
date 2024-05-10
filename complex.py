"""
This module contains the Complex class which represents a complex number.
"""


class Complex:

    def __init__(self, re: float, im: float):
        self._re = re
        self._im = im

    def __str__(self) -> str:
        sign = "+" if self._im >= 0 else "-"
        return f"{self._re} {sign} {abs(self._im)}i"

    def __add__(self, other) -> 'Complex':
        if isinstance(other, Complex):
            return Complex(self._re + other.re, self._im + other.im)
        else:
            return Complex(self._re + other, self._im)

    def __radd__(self, other) -> 'Complex':
        return self + other

    def __sub__(self, other) -> 'Complex':
        if isinstance(other, Complex):
            return Complex(self._re - other.re, self._im - other.im)
        else:
            return Complex(self._re - other, self._im)

    def __mul__(self, other) -> 'Complex':
        if isinstance(other, Complex):
            return Complex(self._re * other.re - self._im * other.im, self._re * other.im + self._im * other.re)
        else:
            return Complex(self._re * other, self._im * other)

    def __rmul__(self, other) -> 'Complex':
        return self * other

    def ft_pow(self, exponent: int) -> 'Complex':
        if exponent == 0:
            return Complex(1, 0)
        return self * self.ft_pow(exponent - 1)

    def __round__(self, n=None) -> 'Complex':
        return Complex(round(self._re, n), round(self._im, n))

    @property
    def re(self) -> float:
        return self._re

    @property
    def im(self) -> float:
        return self._im

    @re.setter
    def re(self, re: float) -> None:
        self._re = re

    @im.setter
    def im(self, im: float) -> None:
        self._im = im
