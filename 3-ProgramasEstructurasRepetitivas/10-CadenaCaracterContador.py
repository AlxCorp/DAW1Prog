# Pide una cadena y un carácter por teclado y muestra cuantas veces aparece el carácter en la cadena.
# Author: Alejandro Priego Izquierdo
# Date: 02/11/2022

# Encabezado del ejercicio
print("")
print("Este programa indicará la cantidad de veces que se repite el carácter")
print("---------------------------------------------------------------------")

# Preguntamos las variables
string = input("Ingrese la cantidad de números primos a mostrar: ")
character = input("Ingrese el carácter a contar en la cadena: ")

counter = string.count(character)

print("El carácter", character, "se muestra en la cadena un total de", counter, "veces")
