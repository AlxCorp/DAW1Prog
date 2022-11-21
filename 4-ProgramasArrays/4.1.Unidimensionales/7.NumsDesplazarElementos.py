# Escribe un programa que lea 15 números por teclado y que los almacene en un array. Rota los elementos de ese array,
# es decir, el elemento de la posición 0 debe pasar a la posición 1, el de la 1 a la 2, etc. El número que se
# encuentra en la última posición debe pasar a la posición 0. Finalmente, muestra el contenido del array.
# Author: Alejandro Priego Izquierdo
# Date: 21/11/2022

# Encabezado del ejercicio
print("")
print("Este programa invierte el orden de los números impresos")
print("-------------------------------------------------------")

# Preguntamos las variables
numbers = []

for i in range(15):
    numbers.append(float(input("Ingrese un número: ")))

last_number = numbers[14]

print(numbers)

for i in range(len(numbers)-1, 0, -1):
    numbers[i] = numbers[i-1]

numbers[0] = last_number

print(numbers)
