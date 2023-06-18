# Crea una aplicación que pida números y los compare con 0.
# Author: Alejandro Priego Izquierdo
# Date: 26/10/2022

# Encabezado del ejercicio
print("")
print("Este programa permite comparar números con 0")
print("--------------------------------------------------------------")

# Preguntamos las variables
quantity = int(input("Ingrese la cantidad de números a introducir: "))
i = 0
more = 0
equal = 0
less = 0

while i < quantity:
    i += 1

    x = float(input("Ingrese un número: "))

    if x < 0:
        less += 1
    elif x == 0:
        equal += 1
    elif x > 0:
        more += 1
    else:
        print("Por favor, ingresa un valor válido")

print("Has introducido", less, "números menores a cero,", equal, "números iguales a cero y,", more, "números mayores "
                                                                                                    "a cero")
