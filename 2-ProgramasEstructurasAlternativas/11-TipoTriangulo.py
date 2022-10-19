# Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los lados de un triángulo. El
# programa debe determinar que tipo de triángulo es, teniendo en cuenta los siguientes:
#   Si se cumple Pitágoras entonces es triángulo rectángulo
#   Si solo dos lados del triángulo son iguales entonces es isósceles.
#   Si los 3 lados son iguales entonces es equilátero.
#   Si no se cumple ninguna de las condiciones anteriores, es escaleno.
#
# Author: Alejandro Priego Izquierdo
# Date: 19/10/2022

# Encabezado del ejercicio
print("")
print("Este programa determina el tipo de triángulo")
print("--------------------------------------------")

# Preguntamos las variables
a = float(input("Ingrese el lado 1: "))
b = float(input("Ingrese el lado 2: "))
c = float(input("Ingrese el lado 3: "))

if a**2 + b**2 == c**2:     # Comprobar si se cumple fórmula triángulo equilátero (a^2 + b^2 = c^2)
    print("Este es un Triángulo Rectángulo")
elif a == b or a == c or a == c and a != b or a != c or b != c:     # Comprueba SOLO 2 lados iguales
    print("Este es un Triángulo Isósceles")
elif a == b == c:
    print("Este es un Triángulo Equilátero")
else:
    print("Este es un Triángulo Escaleno")
