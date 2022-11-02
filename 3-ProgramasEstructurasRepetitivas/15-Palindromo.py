# Introducir una cadena de caracteres e indicar si es un palíndromo. Una palabra palíndroma es aquella que
# se lee igual adelante que atrás.
# Author: Alejandro Priego Izquierdo
# Date: 02/11/2022

# Encabezado del ejercicio
print("")
print("Este programa indica si la cadena es un palíndromo")
print("--------------------------------------------------")

# Preguntamos las variables
string = input("Ingrese la cadena: ")
reversedString = ""

for i in string[::-1]:
    reversedString += str(i)

if reversedString == string:
    print("La cadena ES un palíndromo")
else:
    print("La cadena NO es un palíndromo")
