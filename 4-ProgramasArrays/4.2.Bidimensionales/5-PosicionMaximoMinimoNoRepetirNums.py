# Realiza un programa que rellene un array de 6 filas por 10 columnas con números enteros positivos comprendidos
# entre 0 y 1000 (ambos incluidos). A continuación, el programa deberá dar la posición tanto del máximo como del
# mínimo.
# Author: Alejandro Priego Izquierdo
# Date: 26/11/2022
import random as rng
from copy import deepcopy

# Encabezado del ejercicio
print("")
print("Este programa muestra la suma de filas y columnas")
print("-------------------------------------------------")

numbers = [[0] * 10 for _ in range(6)]
for fila in range(6):
    for columna in range(10):
        while True:
            temp = rng.randrange(0, 1001)
            if temp in numbers[fila]:
                pass
            else:
                numbers[fila][columna] = temp
                break

# numbers_ordered = numbers.copy()
numbers_ordered = deepcopy(numbers)
for i in range(6):
    numbers_ordered[i].sort()

menores = []
mayores = []
for i in range(6):
    menores.append(numbers_ordered[i][0])
    mayores.append(numbers_ordered[i][9])

menores.sort()
menor = menores[0]
mayores.sort()
mayor = mayores[5]

'''
# Debug
print(numbers)
print(numbers_ordered)
print(mayores)
print(menores)
print(mayor)
print(menor)
'''

for fila in range(6):
    for columna in range(10):
        print(f"{numbers[fila][columna]:^6}", end="")
    print()
print()

# En caso de que solo se muestre 1 mayor o 1 menor:
# menor_display = False
# mayor_display = False
for fila in range(6):
    for columna in range(10):
        if menor == numbers[fila][columna]:
            print(f"El número menor ({menor}) se encuentra en la posición ({fila+1},{columna+1})")
        if mayor == numbers[fila][columna]:
            print(f"El número mayor ({mayor}) se encuentra en la posición ({fila+1},{columna+1})")
