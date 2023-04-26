"""
Realiza un programa que sea capaz de ordenar alfabéticamente las palabras contenidas en un fichero de texto. El nombre
del fichero que contiene las palabras se debe pasar como argumento en la línea de comandos. El nombre del fichero
resultado debe ser el mismo que el original añadiendo la coletilla sort, por ejemplo palabras_sort.txt. Suponemos que
cada palabra ocupa una línea.

Author: Alejandro Priego Izquierdo
Date: 25/04/2023
"""
from sys import argv

if len(argv) == 1:
    raise ValueError("Debes ingresar un argumento.")

with open(argv[1], mode="r", encoding="utf-8") as f:
    raw_words = f.readlines()

words = []
for n in raw_words:
    words.append(n.rstrip())
words.sort()

new_file = argv[1][:-4] + "_sort.txt"
with open(new_file, mode="w", encoding="utf-8") as f:
    for n in words:
        f.write(n + "\n")
