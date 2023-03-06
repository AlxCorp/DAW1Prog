
from typeguard import typechecked
from random import randrange as rng
from random import shuffle
from typing import List
from card import Card


@typechecked
class Deck:
    def __init__(self, cards: List['Card']):
        self.__cards = []
        for i in cards:
            self.__cards.append(i)

    def deal(self, quantity: int = 1):
        if self.__cards:
            if quantity == 1:
                return self.__cards.pop(rng(0, len(self.__cards)))
            if quantity > 1:
                cards = []
                for i in range(quantity):
                    cards.append(self.__cards.pop(rng(0, len(self.__cards))))
                return cards
            raise ValueError("Debes ingresar un número positivo")
        raise ValueError("No hay cartas en la baraja")

    def stole(self):
        if self.__cards:
            return self.__cards.pop(0)
        raise ValueError("No hay cartas en la baraja")

    def shuffle(self):
        shuffle(self.__cards)
