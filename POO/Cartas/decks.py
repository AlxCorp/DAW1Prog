from typeguard import typechecked
from deck import Deck, Card


@typechecked
class SpanishDeck(Deck):
    cards = (
        ("Bastos", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),
        ("Espadas", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),
        ("Oros", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),
        ("Copas", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
    )

    def __init__(self, *cards: 'Card'):
        super().__init__(*cards)


@typechecked
class EnglishDeck(Deck):
    cards = (
        ("Picas", 'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'),
        ("Corazones", 'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'),
        ("Tréboles", 'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'),
        ("Rombos", 'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K')
    )

    def __init__(self, *cards: 'Card'):
        super().__init__(*cards)
