# Indicar cuál es la calificación cualitativa de un examen a partir de la numérica.
# Author: Alejandro Priego Izquierdo
# Date: 24/10/2022

# Encabezado del ejercicio
print("")
print("Este programa indica cual es la nota cualitativa del examen")
print("-----------------------------------------------------------")

# Preguntamos las variables
note = float(input("Ingrese la nota del examen: "))

if note < 5:
    print("Suspenso")
elif 5 <= note < 7:
    print("Aprobado")
elif 7 <= note < 9:
    print("Notable")
elif 9 <= note < 10:
    print("Sobresaliente")
elif note == 10:
    print("Matrícula de Honor")
else:
    print("Por favor, introduce un valor válido")