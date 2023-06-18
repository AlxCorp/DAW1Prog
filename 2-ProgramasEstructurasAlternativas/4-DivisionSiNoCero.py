# Crea un programa que pida al usuario dos números y muestre su división si el segundo no es cero, o un mensaje de
# aviso en caso contrario.
# Author: Alejandro Priego Izquierdo
# Date: 18/10/2022

# Encabezado del ejercicio
print("")
print("Este programa realizará una división si el segundo número es distinto a 0")
print("-------------------------------------------------------------------------")

# Preguntamos los números
num1 = float(input("Indica el primer número: "))
num2 = float(input("Indica el segundo número: "))

# Comprobamos que sea distinto a 0 e imprimimos el resultado
if num2 != 0:
    print("El resultado de la operación es", num1/num2)
elif num2 == 0:
    print("El segundo valor no puede ser igual a 0")
else:
    print("Por favor, ingresa un valor válido")
