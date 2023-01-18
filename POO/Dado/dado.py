from random import randint as rng


class Dado:
    def __init__(self):
        self.tirada: int = 0

    def tirar_dado(self):
        self.tirada: int = rng(1, 6)
        return self.tirada
