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


def introducir_numeros():
    global a, b
    a = float(input("Ingrese el valor de a: "))
    b = float(input("Ingrese el valor de b: "))


def sumar(x, y):
    return x + y


def restar(x, y):
    return x - y


def multiplicar(x, y):
    return x * y


def dividir(x, y):
    if x == 0:
        return 0
    elif y == 0:
        return "No se puede dividir algo entre 0"
    else:
        return x / y


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
