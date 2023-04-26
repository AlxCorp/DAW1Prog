"""
Clase Menú con las siguientes opciones:

input(): Introducir fecha en formato dd/mm/aaaa. Si no se introduce correctamente se devuelve un mensaje de error.
            Usa una función booleana para validar la fecha.
__add__(): Añadir días a la fecha. Pide un número de días para sumar a la fecha introducida previamente y actualiza su
            valor. Si el número es negativo restará los días. Esta opción únicamente podrá realizarse si hay una fecha
            introducida (se ha ejecutado la opción anterior), si no la hay mostrará un mensaje de error.
add_month(): Añadir meses a la fecha. El mismo procedimiento que la opción anterior.
add_year(): Añadir años a la fecha. El mismo procedimiento que la opción 2.
__eq__(): Comparar la fecha introducida con otra. Pide una fecha al usuario en formato dd/mm/aaaa (válida, si no lo
            es da error) y la comparará con la que tenemos guardada, posteriormente mostrará si esta fecha es anterior,
            igual o posterior a la que tenemos almacenada y el número de días comprendido entre las dos fechas.
date: Mostrar la fecha en formato largo (ejemplo: "lunes, 1 de febrero de 2021").
Terminar.
"""
import sys


class Menu:
    def __init__(self, title, *args):
        self.__title = title
        if len(args) == 1 and (isinstance(args[0], tuple) or isinstance(args[0], list)):
            self.__options = list(args[0])
        else:
            self.__options = list(args)

#    @property
    def print_menu(self):
        if not self.__options:
            raise ValueError('No hay elementos en el menu')

        print(f'{self.__title:^40}')
        print(f'{"-"*len(self.__title):^40}')
        for i in range(len(self.__options)):
            print(f'{i+1}. {self.__options[i]}.')
        print(f'0. Salir.')
        print()

        q = int(input("Seleccione la opción que desee: "))
        print()
        print()

        if q <= len(self.__options) or (q == 0):
            return q
        raise ValueError('Debes introducir una opción válida.')


if __name__ == '__main__':
    m = Menu("Menu de Prueba", ("OPC1", "OPC2", "OPC3"))

    while True:
        try:
            m.print_menu()
        except ValueError as error:
            print("\n")
            print("ERROR:", error, file=sys.stderr)
            print("\n")
