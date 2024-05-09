class Fraction:

    def __init__(self, numerator, denominator):
        from better_solutions import to_int
        numerator, denominator = to_int(numerator, denominator)
        if denominator < 0:
            numerator, denominator = -numerator, -denominator
        self._numerator = numerator
        self._denominator = denominator
        self.simplify()

    def __str__(self):
        return f"{self._numerator} / {self._denominator}" if self._denominator != 1 else str(self._numerator)

    def __repr__(self):
        return f"Fraction({self._numerator}, {self._denominator})"

    def simplify(self):
        from ft_math import ft_gcd
        gcd = ft_gcd(self._numerator, self._denominator)
        self._numerator //= gcd
        self._denominator //= gcd

    def result(self):
        return self._numerator / self._denominator

    def __add__(self, other):
        if isinstance(other, (int, float)):
            other = Fraction(other, 1)
        numerator = self._numerator * other._denominator + other._numerator * self._denominator
        denominator = self._denominator * other._denominator
        result = Fraction(numerator, denominator)
        result.simplify()
        return result

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            other = Fraction(other, 1)
        numerator = self._numerator * other._denominator - other._numerator * self._denominator
        denominator = self._denominator * other._denominator
        result = Fraction(numerator, denominator)
        result.simplify()
        return result

    def __rsub__(self, other):
        return -self + other

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            other = Fraction(other, 1)
        numerator = self._numerator * other._numerator
        denominator = self._denominator * other._denominator
        result = Fraction(numerator, denominator)
        result.simplify()
        return result

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            other = Fraction(other, 1)
        numerator = self._numerator * other._denominator
        denominator = self._denominator * other._numerator
        result = Fraction(numerator, denominator)
        result.simplify()
        return result

    def __rtruediv__(self, other):
        return Fraction(self._denominator, self._numerator) * other

    def ft_pow(self, exponent):
        if exponent == 0:
            return Fraction(1, 1)
        if exponent < 0:
            return Fraction(self._denominator, self._numerator).ft_pow(-exponent)
        return self * self.ft_pow(exponent - 1)

    def __neg__(self):
        return Fraction(-self._numerator, self._denominator)

    def __eq__(self, other):
        if isinstance(other, (int, float)):
            other = Fraction(other, 1)
        return self._numerator == other._numerator and self._denominator == other._denominator

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        if isinstance(other, (int, float)):
            other = Fraction(other, 1)
        return self._numerator // self._denominator < other._numerator // other._denominator

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other

    def __round__(self, n=None):
        return round(self.result(), n)

    @property
    def numerator(self):
        return self._numerator

    @property
    def denominator(self):
        return self._denominator