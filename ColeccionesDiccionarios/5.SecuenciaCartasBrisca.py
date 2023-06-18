"""
Escribe un programa que genere una secuencia de 5 cartas de la baraja española y que sume los puntos según el juego de
la brisca.
    El valor de las cartas se debe guardar en un diccionario que debe contener parejas (figura, valor), por
ejemplo (“caballo”, 3).
    La secuencia de cartas debe ser una lista que contiene objetos de la clase Carta.
    El valor de las cartas es el siguiente: as → 11, tres → 10, sota → 2, caballo → 3, rey → 4; el resto de cartas no
vale nada.

Author: Alejandro Priego Izquierdo
Date: 03-04-2023
"""

from random import choice
from POO.Cartas.card import Card

PALOS = ('BASTOS', 'COPAS', 'ESPADAS', 'OROS')
NUMEROS = ('AS', '2', '3', '4', '5', '6', '7', 'SOTA', 'CABALLO', 'REY')

cards = []

ITERATOR = 5
for i in range(ITERATOR):
    palo, numero = choice(PALOS), choice(NUMEROS)

    if Card(palo, numero) in cards:
        ITERATOR += 1
        continue
    cards.append(Card(palo, numero))

