# El director de una escuela está organizando un viaje de estudios, y requiere determinar cuánto debe cobrar a cada
# alumno y cuánto debe pagar a la compañía de viajes por el servicio.
# Author: Alejandro Priego Izquierdo
# Date: 21/10/2022

# Encabezado del ejercicio
print("")
print("Este programa determina cuanto cobrar a los alumnos y pagar a la compañía de viaje")
print("----------------------------------------------------------------------------------")

# Preguntamos las variables
studentsQuantity = int(input("Ingrese el número de estudiantes: "))
BUSCOST = 4000
studentCost = None

if studentsQuantity >= 100:
    studentCost = 65
    print("El precio a pagar por cada estudiante es de", studentCost, "Euros; los cuales suman un total de",
          studentCost * studentsQuantity, "Euros para la compañía de Viajes")
elif 50 <= studentsQuantity <= 99:
    studentCost = 70
    print("El precio a pagar por cada estudiante es de", studentCost, "Euros; los cuales suman un total de",
          studentCost * studentsQuantity, "Euros para la compañía de Viajes")
elif 30 <= studentsQuantity <= 49:
    studentCost = 95
    print("El precio a pagar por cada estudiante es de", studentCost, "Euros; los cuales suman un total de",
          studentCost * studentsQuantity, "Euros para la compañía de Viajes")
else:
    print("El precio a pagar por cada estudiante es de", BUSCOST/studentsQuantity,
          "Euros para pagar los 4000 Euros que pide la compañía de Viajes")
