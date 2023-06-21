"""Implementa la clase Rectangulo (determinado por dos objetos Point) que además de su constructor, tendrá dos
métodos para calcular su área y su perímetro que tienes que transformar en propiedades. Implementa también un test
que cree dos puntos y un rectángulo a partir de estos dos puntos y que muestre el área y perímetro de dicho rectángulo.

Author: Alejandro Priego
Date: 24/01/2023
"""


class Rectangle:
    def __init__(self, base=0, altura=0):
        self.base = base
        self.altura = altura

    @property
    def area(self):
        return self.base * self.altura

    @property
    def perimetro(self):
        return 2 * self.base + 2 * self.altura
