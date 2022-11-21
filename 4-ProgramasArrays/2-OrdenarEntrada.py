# Crea un programa que invierta el orden de los elementos introducidos.
# Author: Alejandro Priego Izquierdo
# Date: 14/11/2022

# Encabezado del ejercicio
print("")
print("Este programa invierte el orden de los números impresos")
print("-------------------------------------------------------")

# Preguntamos las variables
numbers = []

for i in range(10):
    numbers.append(float(input("Ingrese un número: ")))

numbers.reverse()

print()
for i in range(10):
    if i < 9:
        print(numbers[i], ", ", end="")
    else:
        print(numbers[i], end="")
