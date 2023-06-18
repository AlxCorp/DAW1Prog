"""
Implementar otra clase Dado. Por defecto el dado tendrá 6 caras. Tendremos tres formar de construir un dado (uno
al que no se le pasa nada e inicializa el dado al azar, otro al que solo se le pasa que número tiene el dado en la
cara superior y otro con el número del dado en la cara superior y el número de caras del dado). Implementa los
getters, el método roll() que tirará el dado al azar y el __str__(). Implementa un tester que tenga un vector de 4
dados y los lance una serie de veces.

Author: Alejandro Priego
Date: 24/01/2023
"""
from typeguard import typechecked
from random import randint as rng


@typechecked
class Dice:
    def __init__(self, result: int = None, faces: int = 6):
        self.__result = result
        self.__faces = faces

        if self.__result is None:
            self.roll()

    def roll(self):
        self.__result: int = rng(1, self.__faces)
        return self.__result

    @property
    def faces_number(self):
        return self.__faces

    @faces_number.setter
    def faces_number(self, faces: int):
        self.__faces = faces
        if self.__faces < self.__result:
            self.roll()

    @property
    def result(self):
        return self.__result

    def __str__(self):
        return f'Ha salido {self.__result}'
