from typeguard import typechecked
from random import randrange as rng
from card import Card
from deck import Deck
from typing import List


@typechecked
class CardPlayer:
    def __init__(self, name: str):
        self.__name = name
        self.__cards = []

    @property
    def name(self):
        return self.__name

    @property
    def cards(self):
        return self.__cards.copy()

    def stole_card(self, other: 'Deck'):
        self.__cards.append(other.stole)

    def throw_off(self, card: ('Card', int, None) = None):
        if self.__cards and isinstance(card, Card):
            self.__cards.remove(card)
            return card
        elif self.__cards and card is None:
            return self.__cards.pop(rng(0, len(self.__cards)))
        elif self.__cards and card <= len(self.__cards):
            return self.__cards.pop(card-1)
        elif self.__cards:
            raise ValueError("Este jugador no tiene tantas cartas")
        raise ValueError("Este jugador no tiene cartas")

    def get_cards(self, cards: List['Card']):
        for i in cards:
            self.get_card(i)

    def get_card(self, card: 'Card'):
        if card not in self.__cards:
            self.__cards.append(card)
        else:
            raise ValueError("El jugador ya tiene esta carta")
