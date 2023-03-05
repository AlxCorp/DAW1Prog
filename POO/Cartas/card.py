from typeguard import typechecked


@typechecked
class Card:
    def __init__(self, suit_letter, value):
        self.__suit_letter = suit_letter
        self.__value = value
