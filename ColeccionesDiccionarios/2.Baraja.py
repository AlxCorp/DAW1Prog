"""
 Realiza un programa que escoja al azar 10 cartas de la baraja española (10 objetos de la clase Carta). Emplea una lista
 para almacenarlas y asegúrate de que no se repite ninguna. Las cartas se deben mostrar ordenadas. Primero se ordenarán
 por palo (bastos, copas, espadas, oros) y cuando coincida el palo, se ordenará por número: as, 2, 3, 4, 5, 6, 7, sota,
 caballo, rey.

Author: Alejandro Priego Izquierdo
Date: 20-03-2023
"""

from random import choice
from POO.Cartas.card import Card

PALOS = ('BASTOS', 'COPAS', 'ESPADAS', 'OROS')
NUMEROS = ('AS', '2', '3', '4', '5', '6', '7', 'SOTA', 'CABALLO', 'REY')

cards = []

iterator = 10
for i in range(iterator):
    palo, numero = choice(PALOS), choice(NUMEROS)

    if Card(palo, numero) in cards:
        iterator += 1
        continue
    cards.append(Card(palo, numero))

cards = sorted(cards, key=lambda x: NUMEROS.index(x.value))
cards = sorted(cards, key=lambda x: x.suit_letter)

# cards = sorted(cards, key=lambda card: (PALOS.index(card.suit_letter), card.value))

for i in cards:
    print(f'{i.value} de {i.suit_letter}')
