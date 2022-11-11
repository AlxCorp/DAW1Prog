""" Realiza un conversor del sistema decimal al sistema de “palotes”.
Ejemplo:
Por favor, introduzca un número entero positivo: 47021
El 47021 en decimal es el | | | | - | | | | | | | - - | | - | en el sistema de palotes.
Si no se introduce un número entero positivo el programa debe terminar de manera anormal con un
mensaje de error."""
# Author: Alejandro Priego Izquierdo
# Date: 10/11/2022
import sys

# Encabezado del ejercicio
print("")
print("Este programa convierte al sistema \"palotes\"")
print("----------------------------------------------")

# Preguntamos las variables
number = input("Ingrese el número en decimal: ")
palotes = ""

if not number.isdecimal() or int(number) < 0:   # Comprobamos que sea un número mayor que 0
    print("ERROR: Debes ingresar un número decimal positivo", file=sys.stderr)  # Imprimimos en salida de errores
    quit(1)     # Salimos con código de error
#   else:
#       number = int(number)  # Lo transformo posteriormente para poder manejar la excepción.

for digit in range(len(number)):    # No lo convierto a INT para poder comprobar longitud
    temporal = number[digit]    # Sacamos cada uno de los dígitos a una variable temporal

    # Comprobamos qué "número" se ha introducido y lo transformamos
    match temporal:
        case "0":
            temporal = ""
        case "1":
            temporal = "|"
        case "2":
            temporal = "||"
        case "3":
            temporal = "|||"
        case "4":
            temporal = "||||"
        case "5":
            temporal = "|||||"
        case "6":
            temporal = "||||||"
        case "7":
            temporal = "|||||||"
        case "8":
            temporal = "||||||||"
        case "9":
            temporal = "|||||||||"

    # Concatenamos las salidas
    if digit == len(number)-1:
        palotes += temporal
    else:
        palotes += temporal + " - "

print(palotes)
