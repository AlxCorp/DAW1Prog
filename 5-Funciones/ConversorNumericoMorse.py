# Author: Alejandro Priego Izquierdo
# Date: 18/12/2022

def numerico_a_morse(x):
    diccionario_numeros_morse = ["_____", ".____", "..___", "...__", "...._", ".....", "_....", "__...",
                                 "___..", "____."]

    x = str(x)
    morse = ""
    posicion = 0

    for n in x:
        morse += diccionario_numeros_morse[int(n)]

        posicion += 1
        if posicion == len(x):
            pass
        else:
            morse += " "

    return morse
