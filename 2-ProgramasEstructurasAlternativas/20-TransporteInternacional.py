# Indicar cuantos abonará el cliente por envíos a diferentes lugares y con diferentes pesos.
# Author: Alejandro Priego Izquierdo
# Date: 23/10/2022

# Encabezado del ejercicio
print("")
print("Este programa indica el importe del envío")
print("-----------------------------------------")

print("las ubicaciones geográficas son las siguientes:")
print("1. América del Norte")
print("2. América Central")
print("3. América del Sur")
print("4. Europa")
print("5. Asia")

# Preguntamos las variables
region = int(input("Ingrese el número de su región (1-5): "))
weight = float(input("Ingrese el peso del envío (Kg)")) * 1000

GRAMO1 = 24
GRAMO2 = 20
GRAMO3 = 21
GRAMO4 = 10
GRAMO5 = 18
cost = None

if weight > 5000:
    print("Envío rechazado al pesar más de 5Kg")
    quit()
elif weight < 1:
    print("El peso del envío debe ser superior a 1g")
    quit()

match region:
    case 1:
        cost = GRAMO1
    case 2:
        cost = GRAMO2
    case 3:
        cost = GRAMO3
    case 4:
        cost = GRAMO4
    case 5:
        cost = GRAMO5
    case _:
        print("ERROR: Ubicación no válida")
        quit()

cost *= weight

print("El precio del envío será de", cost, "€")