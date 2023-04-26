"""
Realiza un programa que diga cuántas ocurrencias de una palabra hay en un fichero. Tanto el nombre del fichero como la
palabra se deben pasar como argumentos en la línea de comandos.

Author: Alejandro Priego Izquierdo
Date: 25/04/2023
"""
from sys import argv, stderr

if len(argv) == 1 or len(argv) == 2:
    raise ValueError("Debes ingresar DOS argumentos.")

words = {}
with open(argv[1], mode="r", encoding="utf-8") as f:
    f_lines = f.readlines()

for n in f_lines:
    if not n.rstrip() in words:
        words[n.rstrip()] = 1
    else:
        words[n.rstrip()] += 1
try:
    print(f'La palabra {argv[2]} tiene un total de {words[argv[2]]} ocurrencias.')
except KeyError:
    print("ERROR: Palabra no encontrada", file=stderr)
