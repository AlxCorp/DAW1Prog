"""
EXAMEN PRÁCTICO 3 - PROGRAMACIÓN

Author: Alejandro Priego Izquierdo
Date: 08-03-2023
"""

import cashregister
from menu import Menu


def main():
    opts = ("Entrada de caja (con la fecha y hora actual)", "Salida de caja (con la fecha y hora actual)",
            "Borrado del último movimiento de la caja", "Impresión de la caja")
    m = Menu("Caja Registradora", opts)

    while True:
        selected = m.print_menu()

        match selected:
            case 1:
                input_cash_actual_datetime()
            case 2:
                output_cash_actual_datetime()
            case 3:
                c.delete_last()
            case 4:
                print(c)
            case 0:
                break

        print()


def input_cash_actual_datetime():
    amount = float(input("Introduce la cantidad de ingresar en la Caja: "))
    if amount < 0:
        assert ValueError("No puedes introducir valores negativos!")

    concept = input("Introduce el concepto del ingreso: ")

    c.add(amount, concept)


def output_cash_actual_datetime():
    amount = float(input("Introduce la cantidad de retirar en la Caja: "))
    if amount < 0:
        assert ValueError("No puedes introducir valores negativos!")

    amount *= -1    # Debajo para asegurarme de que no introduzcan valores negativos que pueden cambiar de signo (-*-=+)

    concept = input("Introduce el concepto del retiro: ")
    print("\n\n")

    c.add(amount, concept)


if __name__ == '__main__':
    c = cashregister.CashRegister()

    main()
