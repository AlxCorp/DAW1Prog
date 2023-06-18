# Escribe un programa que pida 10 números por teclado y que luego muestre los números introducidos junto con las
# palabras “máximo” y “mínimo” al lado del máximo y del mínimo respectivamente.
# Author: Alejandro Priego Izquierdo
# Date: 16/11/2022

# Encabezado del ejercicio
print("")
print("Este programa calcula el máximo y mínimo de 10 números")
print("------------------------------------------------------")

# Preguntamos las variables
numbers = []
numbers_ordered = []

for i in range(10):
    numbers.append(int(input("Por favor, ingrese un número: ")))

numbers_ordered = numbers.copy()
numbers_ordered.sort()
print()

for i in numbers:
    if i == numbers_ordered[0]:
        print(f"{i:^8} Mínimo")
    elif i == numbers_ordered[9]:
        print(f"{i:^8} Máximo")
    else:
        print(f"{i:^8}")
