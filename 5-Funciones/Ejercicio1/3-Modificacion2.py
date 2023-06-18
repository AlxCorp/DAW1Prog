# Haz un programa que pida dos valores (a y b) y a continuación muestre un menú con cinco opciones: sumar, restar,
# multiplicar, dividir y terminar. Cada opción llama a una función a la que se le pasan las dos variables y muestra
# el resultado de la operación. Si se introduce una opción incorrecta se muestra un mensaje de error. El menú se
# volverá a mostrar, a menos que no se de a la opción terminar.
# Author: Alejandro Priego Izquierdo
# Date: 26/11/2022

# Encabezado del ejercicio
print("")
print("Este programa realiza las operaciones deseadas")
print("----------------------------------------------")

a = 0
b = 0
activar = False


def introducir_numeros():
    global a, b, activar
    a = float(input("Ingrese el valor de a: "))
    b = float(input("Ingrese el valor de b: "))
    activar = True


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


while True:
    print()
    print("1. Introducir Números")
    print("2. Sumar a y b")
    print("3. Restar a y b")
    print("4. Multiplicar a y b")
    print("5. Dividir a y b")
    print("0. Salir")
    print("--------------------")
    menu = int(input("Ingrese la opción a ejecutar: "))

    match menu:
        case 1:
            introducir_numeros()
        case 2:
            print(sumar(a, b))
        case 3:
            print(restar(a, b))
        case 4:
            print(multiplicar(a, b))
        case 5:
            print(dividir(a, b))
        case 0:
            quit()
        case _:
            pass
