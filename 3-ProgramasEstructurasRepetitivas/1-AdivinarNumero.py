# Crea una aplicación que permita adivinar un número.
# Author: Alejandro Priego Izquierdo
# Date: 26/10/2022

# Encabezado del ejercicio
from random import randrange

print("")
print("Este programa permite adivinar un número, tienes diez intentos")
print("--------------------------------------------------------------")

# Preguntamos las variables
userNumber = int(input("Ingrese el número que cree que es: "))
number = randrange(100)
counter = 1

while userNumber != number and counter <= 10:
    print("El número introducido NO es correcto")
    if userNumber > number:
        print("El número a adivinar es menor")
    else:
        print("El número a adivinar es mayor")

    counter += 1

    if counter == 11:
        print("Has perdido, el número correcto era el", number)
        quit()

    userNumber = int(input("Prueba otra vez: "))

print("Enhorabuena! El número", userNumber, "es correcto, has usado", counter, "intentos")
