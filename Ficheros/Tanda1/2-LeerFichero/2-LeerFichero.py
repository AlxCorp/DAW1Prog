"""
Programa que lee fichero y lo muestra en pantalla.

Author: Alejandro Priego Izquierdo
Date: 25/04/2023
"""

with open("../1-FicheroPrimos500/primos.txt", mode="r") as f:
    for n in f.readlines():
        print(n.rstrip())
