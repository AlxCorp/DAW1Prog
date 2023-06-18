from typeguard import typechecked


@typechecked
class Fraction:
    @classmethod
    def __mcd(cls, x: int, y: int):
        if y == 0:
            return x
        else:
            return Fraction.__mcd(y, x % y)

    def __init__(self, num: int, den: int):
        if den == 0:
            raise ZeroDivisionError(f"El denominador debe ser diferente a 0")
        self.__num, self.__den = num, den
        self.__simplificador()

    def __simplificador(self):
        mcd = Fraction.__mcd(self.__num, self.__den)
        self.__num //= mcd; self.__den //= mcd
        return mcd

    @property
    def fraction(self):
        return self.__num/self.__den

    @property
    def num(self):
        return self.__num

    @property
    def den(self):
        return self.__den

    def multiply_self_fraction(self, x):
        if x == 0:
            raise ZeroDivisionError(f"El multiplicador debe ser diferente a 0")
        return Fraction(self.num*x, self.den*x)

    def __mul__(self, other):
        if isinstance(other, int):
            self.multiply_self_fraction(other)
        else:
            num = self.__num * other.__num
            den = self.__den * other.__den

            return Fraction(num, den)

    def __truediv__(self, other: 'Fraction'):
        num = self.__num * other.__den
        den = self.__den * other.__num

        return Fraction(num, den)

    def __add__(self, other: 'Fraction'):
        if self.__den == other.__den:
            num = self.__num + other.__num
            return Fraction(num, self.__den)

        den = self.__den * other.__den
        num = self.__num * other.__den + self.__den * other.__num
        return Fraction(num, den)

    def __sub__(self, other: 'Fraction'):
        if self.__den == other.__den:
            num = self.__num - other.__num
            return Fraction(num, self.__den)

        den = self.__den * other.__den
        num = self.__num * other.__den - self.__den * other.__num
        return Fraction(num, den)

    def __eq__(self, other):
        return self.num == other.num and self.den == other.den

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        return self.num * other.den < self.den * other.num

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other

    def __str__(self):
        return f'{self.__num}/{self.__den}'
