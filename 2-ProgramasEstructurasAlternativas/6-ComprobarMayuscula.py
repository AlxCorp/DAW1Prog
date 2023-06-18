# Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.
# Author: Alejandro Priego Izquierdo
# Date: 18/10/2022

# Encabezado del ejercicio
print("")
print("Este programa indicará si la letra introducida es mayúscula")
print("-----------------------------------------------------------")

# Preguntamos los números
letra = input("Indica la letra a comprobar: ")

if len(letra) != 1:
    print("Debes introducir UN solo caracter!")
elif len(letra) == 1 and letra.isupper():
    print("La letra", letra, "es Mayúscula")
elif len(letra) == 1 and letra.islower():
    print("La letra", letra, "es minúscula")
else:
    print("Por favor, ingresa un valor válido")
