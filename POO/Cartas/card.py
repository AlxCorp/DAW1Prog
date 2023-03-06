from typeguard import typechecked


@typechecked
class Card:
    def __init__(self, suit_letter: str, value: str):
        self.__suit_letter = suit_letter
        self.__value = value


""" OTRA FORMA DE HACERLO

from dataclasses import dataclass
from typeguard import typechecked

@typechecked
@dataclass(frozen=True)
class Card:
    number: str
    suit: str
    
"""