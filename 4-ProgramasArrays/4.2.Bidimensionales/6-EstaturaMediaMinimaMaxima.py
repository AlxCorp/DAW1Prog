# Realiza un programa que calcule la estatura media, mínima y máxima en centímetros de personas de diferentes países.
# Author: Alejandro Priego Izquierdo
# Date: 26/11/2022
import random as rng

# Encabezado del ejercicio
print("")
print("Este programa muestra la suma de filas y columnas")
print("-------------------------------------------------")

paises = ["España", "Rusia", "Japón", "Australia"]

estaturas = [[0] * 10 for _ in range(4)]
for fila in range(4):
    for columna in range(10):
        estaturas[fila][columna] = rng.randrange(140, 210)


def media_array(array):
    total = 0
    contador = 1
    for i in array:
        total += i
        contador += 1
    total //= contador
    return total


def min_array(array):
    minarray = array.copy()
    minarray.sort()
    return minarray[0]


def max_array(array):
    maxarray = array.copy()
    maxarray.sort()
    return maxarray[9]


print(f"{'':57} MED  MIN  MAX")
for fila in range(4):
    print(f"{paises[fila]:11}: ", end="")
    for i in range(10):
        print(f"{estaturas[fila][i]:^4}", end="")
    print(f"  |  {media_array(estaturas[fila])}  {min_array(estaturas[fila])}  {max_array(estaturas[fila])}")
    print()
