class Fraction:

    def __init__(self, numerator: int | float, denominator: int | float = 1.0):
        from better_solutions import to_int
        numerator, denominator = to_int(numerator, denominator)
        if denominator < 0:
            numerator, denominator = -numerator, -denominator
        self._numerator = numerator
        self._denominator = denominator
        self.simplify()

    def __str__(self) -> str:
        return f"{self._numerator} / {self._denominator}" if self._denominator != 1 else str(self._numerator)

    def __repr__(self) -> str:
        return f"Fraction({self._numerator}, {self._denominator})"

    def simplify(self) -> None:
        from ft_math import ft_gcd
        gcd = ft_gcd(self._numerator, self._denominator)
        self._numerator //= gcd
        self._denominator //= gcd

    def result(self) -> float:
        return self._numerator / self._denominator

    def __add__(self, other) -> 'Fraction':
        if isinstance(other, (int, float)):
            other = Fraction(other, 1.0)
        numerator = self._numerator * other._denominator + other._numerator * self._denominator
        denominator = self._denominator * other._denominator
        result = Fraction(numerator, denominator)
        result.simplify()
        return result

    def __radd__(self, other) -> 'Fraction':
        return self + other

    def __sub__(self, other) -> 'Fraction':
        if isinstance(other, (int, float)):
            other = Fraction(other, 1)
        numerator = self._numerator * other._denominator - other._numerator * self._denominator
        denominator = self._denominator * other._denominator
        result = Fraction(numerator, denominator)
        result.simplify()
        return result

    def __rsub__(self, other) -> 'Fraction':
        return -self + other

    def __mul__(self, other) -> 'Fraction':
        if isinstance(other, (int, float)):
            other = Fraction(other, 1)
        numerator = self._numerator * other._numerator
        denominator = self._denominator * other._denominator
        result = Fraction(numerator, denominator)
        result.simplify()
        return result

    def __rmul__(self, other) -> 'Fraction':
        return self * other

    def __truediv__(self, other) -> 'Fraction':
        if isinstance(other, (int, float)):
            other = Fraction(other, 1)
        numerator = self._numerator * other._denominator
        denominator = self._denominator * other._numerator
        result = Fraction(numerator, denominator)
        result.simplify()
        return result

    def __rtruediv__(self, other) -> 'Fraction':
        return Fraction(self._denominator, self._numerator) * other

    def ft_pow(self, exponent) -> 'Fraction':
        if exponent == 0:
            return Fraction(1, 1)
        if exponent < 0:
            return Fraction(self._denominator, self._numerator).ft_pow(-exponent)
        return self * self.ft_pow(exponent - 1)

    def __neg__(self) -> 'Fraction':
        return Fraction(-self._numerator, self._denominator)

    def __eq__(self, other) -> bool:
        """ Check if two fractions are equal """
        if isinstance(other, (int, float)):
            other = Fraction(other, 1)
        return self._numerator == other._numerator and self._denominator == other._denominator

    def __ne__(self, other) -> bool:
        """ Check if two fractions are not equal """
        return not self == other

    def __lt__(self, other) -> bool:
        """ Check if a fraction is less than another """
        if isinstance(other, (int, float)):
            other = Fraction(other, 1)
        return self._numerator // self._denominator < other._numerator // other._denominator

    def __le__(self, other) -> bool:
        """ Check if a fraction is less than or equal to another """
        return self < other or self == other

    def __gt__(self, other) -> bool:
        """ Check if a fraction is greater than another """
        return not self <= other

    def __ge__(self, other) -> bool:
        """ Check if a fraction is greater than or equal to another """
        return not self < other

    def __round__(self, n=None) -> float:
        return round(self.result(), n)

    def __abs__(self) -> 'Fraction':
        from ft_math import ft_abs
        return Fraction(ft_abs(self._numerator), self._denominator)

    @property
    def numerator(self) -> int:
        return self._numerator

    @property
    def denominator(self) -> int:
        return self._denominator
