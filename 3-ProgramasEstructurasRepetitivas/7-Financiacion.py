# Escribe un programa que calcule las cuotas de la financiación
# Author: Alejandro Priego Izquierdo
# Date: 31/10/2022

# Encabezado del ejercicio
print("")
print("Este programa calcula los pagos de una financiación")
print("---------------------------------------------------")

# Preguntamos las variables
NO_MESES = 20
PRIMER_MES = 10

for i in range(1, NO_MESES + 1):
    print("El mes", i, "pagarás", PRIMER_MES, "€")
    i += 1
    PRIMER_MES *= 2
