# 3. Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
from math import sqrt       # Importamos la función sqrt de la libreria math

cateto1 = float(input("Indica el primer cateto: "))        # Preguntamos la longitud de ambos catetos
cateto2 = float(input("Indica el segundo cateto: "))

hipo = sqrt(cateto1 ** 2 + cateto2 ** 2)        # Guardamos la operación en una variable

print("La hipotenusa es: ", round(hipo, 2), "Metros")   # Imprimimos la solución redondeando los decimales a 2 dígitos
