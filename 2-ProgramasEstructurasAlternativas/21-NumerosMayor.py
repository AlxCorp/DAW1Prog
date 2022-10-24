# Indicar cuál de los tres números es mayor.
# Author: Alejandro Priego Izquierdo
# Date: 24/10/2022

# Encabezado del ejercicio
print("")
print("Este programa indica cual de los tres números es mayor")
print("------------------------------------------------------")

# Preguntamos las variables
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

if num1 > num2 and num1 > num3:
    print("El número", num1, "es Mayor que", num2, "y que", num3)
elif num2 > num1 and num2 > num3:
    print("El número", num2, "es Mayor que", num1, "y que", num3)
elif num3 > num1 and num3 > num2:
    print("El número", num3, "es Mayor que", num1, "y que", num2)
elif num1 == num2 and num1 != num3:
    print(num1, "y", num2, "son Iguales")
elif num2 == num3 and num1 != num2:
    print(num2, "y", num3, "son Iguales")
elif num1 == num3 and num1 != num2:
    print(num1, "y", num3, "son Iguales")
elif num1 == num2 == num3:
    print(num1, ",", num2, "y", num3, "son Iguales")
else:
    print("Por favor, introduce un valor válido")
