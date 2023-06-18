from typeguard import typechecked
from ..Point.point import Point


class Rectangulo:
    @typechecked
    def __init__(self, base: float = 0, altura: float = 0, p1: Point = Point(0, 0), p2: Point = Point(0, 0)):
        self.__base = base
        self.__altura = altura
        self.__p1 = p1
        self.__p2 = p2
        self.calcular_base_altura()

    @property
    def area(self):
        area = self.__base * self.__altura
        return area

    @property
    def perimetro(self):
        perimetro = self.__base * 2 + self.__altura * 2
        return perimetro

    def calcular_base_altura(self):
        if self.__base != 0 or self.__altura != 0:
            return

        self.__base = abs(self.__p1.x - self.__p2.x)
        self.__altura = abs(self.__p1.y - self.__p2.y)
