# Haz un programa que pida dos valores (a y b) y a continuación muestre un menú con cinco opciones: sumar, restar,
# multiplicar, dividir y terminar. Cada opción llama a una función a la que se le pasan las dos variables y muestra
# el resultado de la operación. Si se introduce una opción incorrecta se muestra un mensaje de error. El menú se
# volverá a mostrar, a menos que no se dé a la opción terminar.
# Author: Alejandro Priego Izquierdo
# Date: 26/11/2022

# Encabezado del ejercicio



def main():
    print("")
    print("Este programa realiza las operaciones deseadas")
    print("----------------------------------------------")

    a, b = 0, 0
    activar = False
    opciones = ["Introducir Números", "Sumar a y b", "Restar a y b", "Multiplicar a y b", "Dividir a y b", "Salir"]

    while True:
        match menu(opciones):
            case 0:
                introducir_numeros()
            case 1:
                if not activar:
                    error_valores()
                    continue
                print(sumar(a, b))
            case 2:
                if not activar:
                    error_valores()
                    continue
                print(restar(a, b))
            case 3:
                if not activar:
                    error_valores()
                    continue
                print(multiplicar(a, b))
            case 4:
                if not activar:
                    error_valores()
                    continue
                print(dividir(a, b))
            case 5:
                quit()
            case _:
                pass
        print()


def introducir_numeros():
    global a, b, activar
    a = float(input("Ingrese el valor de a: "))
    b = float(input("Ingrese el valor de b: "))
    activar = True


def error_valores():
    if not activar:
        print("\n ERROR: Primero debes introducir dos valores \n")
        return 0
    else:
        return 1


def sumar(x, y):
    if activar:
        return x + y
    else:
        print("Primero debes introducir dos valores")
        return ""


def restar(x, y):
    if activar:
        return x - y
    else:
        print("Primero debes introducir dos valores")
        return ""


def multiplicar(x, y):
    if activar:
        return x * y
    else:
        print("Primero debes introducir dos valores")
        return ""


def dividir(x, y):
    if activar:
        if x == 0:
            return 0
        elif y == 0:
            return "No se puede dividir algo entre 0"
        else:
            return x / y
    else:
        print("Primero debes introducir dos valores")
        return ""


def menu(opciones):
    for i in range(len(opciones)):
        print(f"{i}. {opciones[i]}")

    print("------------------------")
    opcion_menu = int(input("Ingrese la opción a ejecutar: "))

    return opcion_menu


if __name__ == "__main__":
    main()
