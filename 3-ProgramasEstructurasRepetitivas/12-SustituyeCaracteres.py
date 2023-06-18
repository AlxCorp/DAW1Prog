# Pide una cadena y dos caracteres por teclado (valida que sea un carácter), sustituye la aparición del primer
# carácter en la cadena por el segundo carácter.
# Author: Alejandro Priego Izquierdo
# Date: 02/11/2022

# Encabezado del ejercicio
print("")
print("Este programa sustituye un carácter por otro")
print("--------------------------------------------")

# Preguntamos las variables
string = input("Ingrese la cadena: ")
broken = input("Ingrese el valor a sustituir: ")
replacement = input("Ingrese el valor sustituto: ")

# while not broken.isalpha() or not replacement.isalpha() or len(broken) != 1 or len(replacement) != 1:
while len(broken) != 1 or len(replacement) != 1:
    print("Ingresa UN solo carácter")
    broken = input("Ingrese el valor a sustituir: ")
    replacement = input("Ingrese el valor sustituto: ")

string = string.replace(broken, replacement)

print(string)
