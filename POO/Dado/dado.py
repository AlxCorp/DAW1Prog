"""
Crea una clase "Dado" que simule el funcionamiento de un dado con caras del 1 al 6 que tienen la misma probabilidad
de salir y un programa de prueba.

Author: Alejandro Priego
Date: 24/01/2023
"""
from random import randint as rng


class Dado:
    def __init__(self):
        self.tirada: int = 0

    def tirar_dado(self):
        self.tirada: int = rng(1, 6)
        return self.tirada
