# Algoritmo que pida caracteres e imprima ‘VOCAL’ si son vocales y ‘NO VOCAL’ en caso contrario,
# el programa termina cuando se introduce un espacio.
# Author: Alejandro Priego Izquierdo
# Date: 27/10/2022

# Encabezado del ejercicio
print("")
print("Este programa indique si el caracter introducido es o no una vocal")
print("Introduce un ESPACIO para terminar el programa")
print("------------------------------------------------------------------")

dictionary = "aeiouAEIOUáéíóúÁÉÍÓÚ"
counter = 0

while True:
    character = input("Por favor, introduce un caracter: ")

    if len(character) != 1:
        print("ERROR: Debes introducir UN solo caracter")
        print()
    elif character == " ":
        break
    elif character in dictionary:
        print("El caracter", '"', character, '"', "es una Vocal")
        print()
    else:
        print("El caracter", '"', character, '"', "NO es una Vocal")
        print()

    counter += 1

print("El programa ha finalizado correctamente, has realizado", counter, "operaciones")
