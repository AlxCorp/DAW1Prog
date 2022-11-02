# Realizar un programa que lea una cadena por teclado y convierta las mayúsculas a minúsculas y viceversa.
# Author: Alejandro Priego Izquierdo
# Date: 02/11/2022

# Encabezado del ejercicio
print("")
print("Este programa convierte mayúsculas a minúsculas y viceversa")
print("-----------------------------------------------------------")

# Preguntamos las variables
string = input("Ingrese la cadena a cambiar: ")

for i in string:
    if i.isupper():
        print(i.lower(), end="")
    elif i.islower():
        print(i.upper(), end="")
    else:
        print(i, end="")
