# Suponiendo que hemos introducido una cadena por teclado que representa una frase (palabras separadas por espacios),
# realiza un programa que cuente cuantas palabras tiene.
# Author: Alejandro Priego Izquierdo
# Date: 02/11/2022

# Encabezado del ejercicio
print("")
print("Este programa indicará la cantidad de palabras de una cadena")
print("------------------------------------------------------------")

# Preguntamos las variables
string = input("Ingrese la cadena a contar: ")

string = string.replace("  ", " ")

splittedString = string.split(" ")

print("Esta cadena tiene un total de ", len(splittedString), "palabras")

