# Realizar un programa que compruebe si una cadena contiene una subcadena. Las dos cadenas se introducen por teclado.
# Author: Alejandro Priego Izquierdo
# Date: 02/11/2022

# Encabezado del ejercicio
print("")
print("Este programa indica si encuentra una subcadena dentro de otra")
print("--------------------------------------------------------------")

# Preguntamos las variables
string1 = input("Ingrese la cadena: ")
string2 = input("Ingrese la subcadena: ")

if string2 in string1:
    print("La subcadena está incluida dentro de la cadena")
else:
    print("La subcadena NO está incluida dentro de la cadena")
