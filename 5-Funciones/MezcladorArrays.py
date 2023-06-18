"""
Define la función mezcla de forma que tome dos listas como parámetros y devuelve otra que es el resultado de mezclar
los números de ambos de forma alterna, se coge un número de a, luego de b, luego de a, etc. Los arrays a y b pueden
tener longitudes diferentes; por tanto, si se terminan los números de un array se terminan de coger todos los que
quedan del otro.
"""
# Author: Alejandro Priego Izquierdo
# Date: 18/12/2022


def mezcla(x, y):
    menor = []
    mayor = []
    mezcla_final = []

    if len(x) < len(y) or len(x) == len(y):
        menor = x
        mayor = y
    elif len(y) < len(x):
        menor = y
        mayor = x

    for n in range(len(mayor)):
        if n < len(menor):
            mezcla_final.append(x[n])
            mezcla_final.append(y[n])
        else:
            mezcla_final.append(mayor[n])

    return mezcla_final
