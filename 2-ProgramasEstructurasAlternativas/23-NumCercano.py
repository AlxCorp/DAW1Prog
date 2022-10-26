# Indicar cuál de los cuatro números es más cercano al primero.
# Author: Alejandro Priego Izquierdo
# Date: 24/10/2022

# Encabezado del ejercicio
print("")
print("Este programa indica cual de los cuatro números es más cercano al primero")
print("-------------------------------------------------------------------------")

# Preguntamos las variables
num1 = int(input("Ingrese el primer número (referencia): "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))
num4 = int(input("Ingrese el cuarto número: "))
num5 = int(input("Ingrese el quinto número: "))

op1 = abs(num1-num2)
op2 = abs(num1-num3)
op3 = abs(num1-num4)
op4 = abs(num1-num5)

if op1 < op2 and op1 < op3 and op1 < op4:
    print("El número", num2, "es el más cercano a", num1)
elif op2 < op1 and op2 < op3 and op2 < op4:
    print("El número", num3, "es el más cercano a", num1)
elif op3 < op1 and op3 < op2 and op3 < op4:
    print("El número", num4, "es el más cercano a", num1)
elif op4 < op1 and op4 < op2 and op4 < op3:
    print("El número", num5, "es el más cercano a", num1)
else:
    print("Por favor, introduce un valor válido")