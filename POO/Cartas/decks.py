from typeguard import typechecked
from deck import Deck, Card


@typechecked
class SpanishDeck(Deck):
    cards_suits = ("Bastos", "Espadas", "Oros", "Copas")
    cards_numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)

    def __init__(self):
        cards = [Card(n, s) for n in SpanishDeck.cards_suits for s in str(SpanishDeck.cards_numbers)]
        super().__init__(cards)


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
