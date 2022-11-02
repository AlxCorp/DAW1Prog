# Escribe un programa que eleve un número sin usar pow ni **
# Author: Alejandro Priego Izquierdo
# Date: 30/10/2022

# Encabezado del ejercicio
print("")
print("Este programa imprime el resultado de una potencia")
print("--------------------------------------------------")

# Preguntamos las variables
base = float(input("Ingrese la base: "))
exp = int(input("Ingrese el exponente: "))
num = base
i = 1

if exp == 0:
    print("El resultado de elevar un número a 0 es 1")
    quit()

while i < exp:
    base *= num
    i += 1

print("El resultado es", base)
