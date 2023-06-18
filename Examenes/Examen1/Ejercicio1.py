"""Realiza el control de acceso a una caja fuerte. La combinación será un número de 4 cifras. El
programa nos pedirá la combinación para abrirla. Si no acertamos, se nos mostrará el mensaje “Lo
siento, esa no es la combinación” y si acertamos se nos dirá “La caja fuerte se ha abierto
satisfactoriamente”. Tendremos cuatro oportunidades para abrir la caja fuerte.
Si no se introduce un número o este no tiene cuatro cifras, el programa debe terminar de manera
anormal con un mensaje de error."""
# Author: Alejandro Priego Izquierdo
# Date: 10/11/2022
import sys

# Encabezado del ejercicio
print("")
print("Este programa es una Caja Fuerte")
print("--------------------------------")

KEY = 1234  # Declaramos KEY como Constante para facilitar el cambio en el futuro
key_enter_hints = 0     # Contador de intentos

print("La clave está compuesta por 4 cifras, tienes 4 intentos. Buena suerte.")

# Preguntamos las variables mientras le queden intentos
while key_enter_hints < 4:
    key_input = input("Ingrese la clave de la Caja Fuerte: ")
    key_enter_hints += 1    # Aumentamos el contador de intentos

    if len(key_input) != 4 or not key_input.isdecimal():    # Comprobamos que la entrada tenga 4 números
        print("ERROR: Debes ingresar una contraseña válida", file=sys.stderr)   # Imprimimos en salida de errores
        quit(1)     # Salimos con código de error
    else:
        key_input = int(key_input)      # Lo transformo posteriormente para poder manejar la excepción.

    if key_input != KEY:
        print("Lo siento, esa no es la combinación. Te quedan", 4-key_enter_hints, "intentos")
    elif key_input == KEY:
        print()
        print("La caja fuerte se ha abierto satisfactoriamente.")
        quit()

print()
print("Has agotado todos tus intentos, la Caja Fuerte sigue cerrada.")
