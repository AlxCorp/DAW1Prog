# Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario.
# Author: Alejandro Priego Izquierdo
# Date: 27/10/2022

# Encabezado del ejercicio
print("")
print("Este programa imprime los pares entre dos números")
print("-------------------------------------------------")

# Preguntamos las variables
min = int(input("Ingrese el número mínimo: "))
max = int(input("Ingrese el número máximo: "))

i = min     # i es el PAR y al mismo tiempo el CONTARDOR
if i % 2 != 0:
    i += 1

if min == max:
    print("Los números introducidos deben ser diferentes.")
    quit()

# Bucle que imprime los pares
while i < max:
    print(i)
    i += 2
