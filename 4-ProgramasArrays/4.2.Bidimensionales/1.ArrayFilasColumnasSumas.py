# Escribe un programa que pida 20 números enteros. Estos números se deben introducir en un array de 4 filas por 5
# columnas. El programa mostrará las sumas parciales de filas y columnas igual que si de una hoja de cálculo se
# tratara. La suma total debe aparecer en la esquina inferior derecha.
# Author: Alejandro Priego Izquierdo
# Date: 21/11/2022

# Encabezado del ejercicio
print("")
print("Este programa muestra la suma de filas y columnas")
print("-------------------------------------------------")

# Preguntamos las variables
numbers = [[0] * 5 for _ in range(4)]

for fila in range(4):
    for columna in range(5):
        numbers[fila][columna] = int(input("Ingrese un número: "))

for fila in range(4):
    print(f"{numbers[fila][0]:^8}{numbers[fila][1]:^8}{numbers[fila][2]:^8}{numbers[fila][3]:^8}{numbers[fila][4]:^8}"
          f"--> "
          f"{numbers[fila][0] + numbers[fila][1] + numbers[fila][2] + numbers[fila][3] + numbers[fila][4]:^8}")

print(f"{'-----':^8}{'-----':^8}{'-----':^8}{'-----':^8}{'-----':^8}    {'-----':^8}")

for columna in range(5):
    print(f"{numbers[0][columna] + numbers[1][columna] + numbers[2][columna] + numbers[3][columna]:^8}", end="")

total = 0
for fila in range(4):
    for columna in range(5):
        total += numbers[fila][columna]
total *= 2

print(f"    {total:^8}")
