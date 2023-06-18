from Tablero import *


def game():
    global posiciones_x, posiciones_y
    ganada = False

    while not ganada:
        jugada_persona1()
        comprobar_ganador()
        print_table()
        jugada_persona2()
        comprobar_ganador()
        print_table()


def jugada_persona1():
    global posiciones_x
    movimiento_x = input("Elija dónde desea realizar el siguiente movimiento: ")

    while True:
        if movimiento_x in posiciones_x or movimiento_x in posiciones_y:
            movimiento_x = input("Elija dónde desea realizar el siguiente movimiento: ")
        else:
            posiciones_x.append(movimiento_xmovimiento_x)


def jugada_persona2():
    global posiciones_y
    movimiento_y = input("Elija dónde desea realizar el siguiente movimiento: ")

    while True:
        if movimiento_y in posiciones_y or movimiento_y in posiciones_x:
            movimiento_y = input("Elija dónde desea realizar el siguiente movimiento: ")
        else:
            posiciones_y.append(movimiento_xmovimiento_x)


def comprobar_ganador_x:
    if ()


if __name__ == '__main__':
    while True:
        posiciones_x = []
        posiciones_y = []
        game()
