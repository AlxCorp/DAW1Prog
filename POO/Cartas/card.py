from typeguard import typechecked


@typechecked
class Card:
    def __init__(self, suit_letter: str, value: str):
        self.__suit_letter = suit_letter
        self.__value = value

    @property
    def suit_letter(self):
        return self.__suit_letter

    @property
    def value(self):
        return self.__value

    def __eq__(self, other):
        return self.suit_letter == other.suit_letter and self.value == other.value


""" OTRA FORMA DE HACERLO

from dataclasses import dataclass
from typeguard import typechecked

@typechecked
@dataclass(frozen=True)
class Card:
    number: str
    suit: str
    
"""