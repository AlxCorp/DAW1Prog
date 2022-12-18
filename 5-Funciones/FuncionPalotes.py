# Crea una función que reciba un número, lo convierta al sistema de palotes y lo devuelva en una cadena de caracteres.
#
# Por ejemplo, el 470213 en decimal es el | | | | - | | | | | | | - - | | - | - | | | en el sistema de palotes.
#
# Utiliza esta función en un programa para comprobar que funciona bien. Desde la función no se debe mostrar nada por
# pantalla, solo se debe usar print desde el programa principal.
# Author: Alejandro Priego Izquierdo
# Date: 18/12/2022

def conversor_palotes(x):
    x = str(x)
    numpalote = ""
    posicion = 0

    for n in x:
        numpalote += int(n) * '|'
        posicion += 1

        if posicion == len(x):
            pass
        else:
            numpalote += " - "

    return numpalote

