# Crea una aplicación que calcule el cuadrado y cubo de los números en una lista.
# Author: Alejandro Priego Izquierdo
# Date: 14/11/2022
import random as rng

# Encabezado del ejercicio
print("")
print("Este programa calcula el cuadrado y cubo de 20 número aleatorios")
print("----------------------------------------------------------------")

# Preguntamos las variables
numero = []
for i in range(20):
    numero.append(rng.randrange(0, 100))

cuadrado = []
for i in numero:
    cuadrado.append(i**2)

cubo = []
for i in numero:
    cubo.append(i**3)

multi_lista = []
for i in range(len(numero)):
    multi_lista.append([numero[i], cuadrado[i], cubo[i]])

print(f"{'Numero':^15} {'Cudrado':^15} {'Cubo':^15}")
print(f"{'---------------':^15} {'---------------':^15} {'---------------':^15}")
for i in range(len(multi_lista)):
    print(f"{multi_lista[i][0]:^15} {multi_lista[i][1]:^15} {multi_lista[i][2]:^15}")
