"""Implementa la clase Rectangulo (determinado por dos objetos Point) que además de su constructor, tendrá dos
métodos para calcular su área y su perímetro que tienes que transformar en propiedades. Implementa también un test
que cree dos puntos y un rectángulo a partir de estos dos puntos y que muestre el área y perímetro de dicho rectángulo.

Author: Alejandro Priego
Date: 24/01/2023
"""
from typeguard import typechecked
from POO.Point.point import Point


class Rectangle:
    @typechecked
    def __init__(self, p1: Point = Point(0, 0), p2: Point = Point(0, 0)):
        self.__p1 = p1
        self.__p2 = p2

    @property
    def area(self):
        return abs(self.__p1.x - self.__p2.x) * abs(self.__p1.y - self.__p2.y)

    @property
    def perimetro(self):
        return abs(self.__p1.x - self.__p2.x) + abs(self.__p1.y - self.__p2.y)
