# Indicar cuál de los cinco números es mayor.
# Author: Alejandro Priego Izquierdo
# Date: 24/10/2022

# Encabezado del ejercicio
print("")
print("Este programa indica cual de los cinco números es mayor")
print("------------------------------------------------------")

# Preguntamos las variables
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))
num4 = int(input("Ingrese el cuarto número: "))
num5 = int(input("Ingrese el quinto número: "))

if num1 > num2 and num1 > num3 and num1 > num4 and num1 > num5:
    print("El número", num1, "es Mayor que", num2, ",", num3, ",", num4, "y", num5)
elif num2 > num1 and num2 > num3 and num2 > num4 and num2 > num5:
    print("El número", num2, "es Mayor que", num1, ",", num3, ",", num4, "y", num5)
elif num3 > num1 and num3 > num2 and num3 > num4 and num3 > num5:
    print("El número", num3, "es Mayor que", num1, ",", num2, ",", num4, "y", num5)
elif num4 > num1 and num4 > num2 and num4 > num3 and num4 > num5:
    print("El número", num4, "es Mayor que", num1, ",", num2, ",", num3, "y", num5)
elif num5 > num1 and num5 > num2 and num5 > num3 and num5 > num4:
    print("El número", num5, "es Mayor que", num1, ",", num2, ",", num3, "y", num4)
else:
    print("Por favor, introduce un valor válido")
