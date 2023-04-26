"""
Programa que guarda en un fichero con nombre primos.txt los números primos que hay entre 1 y 500.

Author: Alejandro Priego Izquierdo
Date: 25/04/2023
"""


def es_primo(num, n=2):
    if n >= num:
        return True
    elif num % n != 0:
        return es_primo(num, n + 1)
    else:
        return False


with open("primos.txt", mode="w") as f:
    for candidate in range(1, 501):
        if es_primo(candidate):
            f.write(str(candidate)+"\n")
