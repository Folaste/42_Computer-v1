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

    def __add__(self, other):
        if isinstance(other, Complex):
            return Complex(self._re + other.re, self._im + other.im)
        else:
            return Complex(self._re + other, self._im)

    def __sub__(self, other):
        if isinstance(other, Complex):
            return Complex(self._re - other.re, self._im - other.im)
        else:
            return Complex(self._re - other, self._im)

    def __mul__(self, other):
        if isinstance(other, Complex):
            return Complex(self._re * other.re - self._im * other.im, self._re * other.im + self._im * other.re)
        else:
            return Complex(self._re * other, self._im * other)

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
