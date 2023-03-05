from typeguard import typechecked
from random import randrange as rng
from card import Card
from deck import Deck
from decks import SpanishDeck, EnglishDeck


@typechecked
class CardPlayer:
    def __init__(self):
        self.__cards = []

    def stole_card(self, other: ('Deck', 'SpanishDeck', 'EnglishDeck')):
        self.__cards.append(other.stole)

    def throw_off(self, card: (int, None) = None):
        if self.__cards and card is None:
            return self.__cards.pop(rng(0, len(self.__cards)))
        elif self.__cards and card <= len(self.__cards):
            return self.__cards.pop(card-1)
        elif self.__cards:
            raise ValueError("Este jugador no tiene tantas cartas")
        raise ValueError("Este jugador no tiene cartas")

    def get_card(self, card: 'Card'):
        if card not in self.__cards:
            self.__cards.append(card)
        else:
            raise ValueError("El jugador ya tiene esta carta")
