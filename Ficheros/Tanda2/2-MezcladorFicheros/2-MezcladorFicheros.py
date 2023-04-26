"""
Escribe un programa que guarde en un fichero el contenido de otros dos ficheros, de tal forma que en el fichero
resultante aparezcan las líneas de los primeros dos ficheros mezcladas, es decir, la primera línea será del primer
fichero, la segunda será del segundo fichero, la tercera será la siguiente del primer fichero, etc.

Los nombres de los dos ficheros origen y el nombre del fichero destino se deben pasar como argumentos en la línea de
comandos.

Hay que tener en cuenta que los ficheros de donde se van cogiendo las líneas pueden tener tamaños diferentes.

Author: Alejandro Priego Izquierdo
Date: 25/04/2023
"""
from sys import argv

if len(argv) == 1 or len(argv) == 2:
    raise ValueError("Debes ingresar DOS argumentos.")

with open(argv[1], mode="r", encoding="utf-8") as f1:
    f1_lines = f1.readlines()

with open(argv[2], mode="r", encoding="utf-8") as f2:
    f2_lines = f2.readlines()

if len(f2_lines) < len(f1_lines):
    f1_lines, f2_lines = f2_lines, f1_lines

with open(argv[1][:-4] + "_" + argv[2], mode="w", encoding="utf-8") as f:
    for _ in range(len(f1_lines)):
        f.write(f1_lines.pop(0))
        f.write(f2_lines.pop(0))
    for n in f2_lines:
        f.write(n)


