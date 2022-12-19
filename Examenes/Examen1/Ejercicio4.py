""" Según cierta cultura oriental, los números de la suerte son el 3, el 7, el 8 y el 9. Los números de la
mala suerte son el resto: el 0, el 1, el 2, el 4, el 5 y el 6. Un número es afortunado si contiene más
números de la suerte que de la mala suerte. Realiza un programa que diga si un número introducido
por el usuario es afortunado o no."""
# Author: Alejandro Priego Izquierdo
# Date: 10/11/2022
import sys

# Encabezado del ejercicio
print("")
print("Este programa dirá si el número es afortunado o no")
print("--------------------------------------------------")

# Preguntamos las variables
number = input("Ingrese el número: ")

# Contadores para números de suerte o no suerte
contador_num_suerte = 0
contador_num_mala_suerte = 0

if not number.isdecimal() or int(number) < 0:   # Comprobamos que sea un número mayor que 0
    print("ERROR: Debes ingresar un número decimal positivo", file=sys.stderr)  # Imprimimos en salida de errores
    quit(1)      # Salimos con código de error
# else:
    # number = int(number)  # Lo transformo posteriormente para poder manejar la excepción.

for digit in range(len(number)):    # No lo convierto a INT para poder comprobar longitud
    temporal = number[digit]    # Sacamos cada uno de los dígitos a una variable temporal

    # Comprobamos qué "número" se ha introducido y lo transformamos. También aumentamos el contador respectivo
    match temporal:
        case "3" | "7" | "8" | "9":
            contador_num_suerte += 1
        case "0" | "1" | "2" | "4" | "5" | "6":
            contador_num_mala_suerte += 1

if contador_num_suerte > contador_num_mala_suerte:
    print("Este es un número afortunado")
if contador_num_suerte <= contador_num_mala_suerte:
    print("Este NO es un número afortunado")
