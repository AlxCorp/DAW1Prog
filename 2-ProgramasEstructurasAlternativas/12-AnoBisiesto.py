# Escribir un programa que lea un año e indicar si es bisiesto.
# Author: Alejandro Priego Izquierdo
# Date: 19/10/2022

# Encabezado del ejercicio
print("")
print("Este programa determina el tipo de triángulo")
print("--------------------------------------------")

# Preguntamos las variables
year = int(input("Ingrese el año: "))

# Un año es bisiesto si es divisible por 4, pero no si es divisible por 100, excepto que también sea divisible por 400.
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("El año", year, "es Bisiesto")
else:
    print("El año", year, "NO es Bisiesto")
