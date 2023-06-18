"""Nos podemos aproximar al número PI usando la serie de Leibniz que dice que PI se puede
obtener a partir de la siguiente sucesión: 4/1 – 4/3 + 4/5 – 4/7 + 4/9…
Si te fijas, el 4 (numerador) es fijo, y el denominador se aumenta de 2 en 2. Además, en cada paso
se intercambia el signo.
Haz un programa que pidiendo el número de iteraciones nos de el valor de PI."""
# Author: Alejandro Priego Izquierdo
# Date: 10/11/2022
import sys

# Encabezado del ejercicio
print("")
print("Este programa es da el valor de PI mediante la serie de Leibniz")
print("---------------------------------------------------------------")

# Preguntamos las variables
iterations = input("Ingrese el número de iteraciones de la serie: ")

if not iterations.isdecimal() or int(iterations) < 0:   # Comprobamos que sea un número mayor que 0
    print("ERROR: Debes ingresar un número decimal positivo", file=sys.stderr)  # Imprimimos en salida de errores
    quit(1)  # Salimos con código de error
else:
    iterations = int(iterations)  # Lo transformo posteriormente para poder manejar la excepción.

NUMERADOR = 4
denominador = 1
signo = True
pi = 0

for i in range(iterations):
    if signo:
        pi += NUMERADOR / denominador
        signo = False
    else:
        pi -= NUMERADOR / denominador
        signo = True

    denominador += 2

print("PI es igual a: ", pi)
