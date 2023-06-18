# 13. Realiza un programa que lea un número y que muestre su raíz cuadrada y su raíz cúbica. Python no
#  tiene ninguna función predefinida que permita calcular la raíz cúbica, ¿cómo se puede calcular?

from math import sqrt       # Importamos librerias para calcular de forma sencilla raíces cuadradas y cúbicas
from numpy import cbrt

numero = float(input("Indica el número a operar: "))    # Pedimos número para operar

cubo = cbrt(numero)     # Calculamos raíz cúbica

# Comprobamos que el número NO sea negativo. En caso de serlo NO se calcula raíz cuadrada
if numero < 0:
    cuadrada = "NO SE PUEDE CALCULAR LA RAÍZ CUADRADA DE UN NÚMERO NEGATIVO."
    print(cuadrada)
    print("El resultado de calcular la raíz cúbica de", numero, "es", cubo)
    quit()

cuadrada = sqrt(numero)     # Calculamos raíz cuadrada

print("El resultado de calcular la raíz cuadrada de", numero, "es", cuadrada, "y el de calcular la raíz cúbica es de", cubo)    # Imprimimos resultado
