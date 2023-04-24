# Escribe un programa que lea un número e indique si es par o impar.
# Author: Alejandro Priego Izquierdo
# Date: 17/10/2022

# Encabezado del ejercicio
print("")
print("Este programa comprobará si el número indicado es Par o Impar.")
print("--------------------------------------------------------------")

# Preguntamos el número
num = float(input("Indica el número: "))

# Usamos el resto para saber si es par o impar
if num % 2 == 0:
    print("Este número es PAR")
else:
    print("Este número es IMPAR")
