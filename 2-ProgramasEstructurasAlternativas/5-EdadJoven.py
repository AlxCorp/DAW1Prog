# Crea un programa que lea la edad de dos personas y diga quién es más joven, la primera o la segunda.
# Ten en cuenta que ambas pueden tener la misma edad. En tal caso, hazlo saber con un mensaje adecuado.
# Author: Alejandro Priego Izquierdo
# Date: 18/10/2022

# Encabezado del ejercicio
print("")
print("Este programa indicará quién es más joven de los dos")
print("----------------------------------------------------")

# Preguntamos los números
edad1 = float(input("Indica la edad de la primera persona: "))
edad2 = float(input("Indica la edad de la segunda persona: "))

if edad1 == edad2:
    print("Las dos edades son iguales, las dos personas tienen la misma edad")
elif edad1 < edad2:
    print("La primera persona es más joven que la segunda")
elif edad1 > edad2:
    print("La segunda persona es más joven que la primera")
else:
    print("Por favor, ingresa un valor válido")
