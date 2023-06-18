"""
Programa de TEST para la Clase AddressBook

Author: Alejandro Priego Izquierdo
Date: 22-05-2023
"""

from menu import Menu
import AddressBook
import Sql_DAO
from os import path
from sys import stderr
import mysql.connector

BOOK = None
DAO = Sql_DAO.SqlDAO()


def main():
    global BOOK, DAO
    flag = False

    options = ("Crear Base de Datos", "Abrir Base de Datos", "Alta Contacto", "Baja Contacto", "Listado Agenda",
               "Exportar a Fichero XML", "Incorporar Desde XML")
    m = Menu("Agenda", options)
    while True:
        try:
            selected = m.print_menu()
        except:
            print("ERROR: Debes seleccionar una opción valida", file=stderr)
            continue
        match selected:
            case 0:
                break
            case 1:
                if flag and input("Ya hay cargada una BADA, ¿SOBREESCRIBIR? (S/N): ").upper() != "S":
                    continue
                dbname = input("Introduzca el nombre de la Base de Datos a crear: ")
                dbuser = input("Introduzca el usuario de la Base de Datos a crear: ")
                dbpassword = input("Introduzca la contraseña del usuario de la Base de Datos: ")
                DAO.create_database(dbname, dbuser, dbpassword)
                BOOK = AddressBook.AddressBook(DAO)
                flag = True
            case 2:
                if flag and input("Ya hay cargada una BADA, ¿SOBREESCRIBIR? (S/N): ").upper() != "S":
                    continue
                dbname = input("Introduzca el nombre de la Base de Datos a abrir: ")
                dbuser = input("Introduzca el usuario de la Base de Datos a abrir: ")
                dbpassword = input("Introduzca la contraseña del usuario de la Base de Datos: ")
                try:
                    DAO.use_database(dbname, dbuser, dbpassword)
                except RuntimeError:
                    print("ERROR: No se ha podido conectar con la BD.", file=stderr)
                    continue
                except:
                    print("ERROR: Usuario o Contraseña incorrectos.", file=stderr)
                    continue
                BOOK = AddressBook.AddressBook(DAO)
                flag = True
            case 3:
                if not flag:
                    print("ERROR: Debes seleccionar antes la opción 1 o 2", file=stderr)
                    continue
                tmp_name = input("Introduce el nombre del contacto: ")
                tmp_phone = input("Introduce el teléfono del contacto: ")
                tmp_email = input("Introduce el email del contacto: ")
                tmp_address = input("Introduce la dirección del contacto (opcional): ")
                try:
                    BOOK.register_contact(tmp_name, tmp_phone, tmp_email, tmp_address)
                except mysql.connector.errors.IntegrityError as e:
                    print(e)
                    print("ERROR: Contacto duplicado o valores no válidos", file=stderr)
                    continue
            case 4:
                if not flag:
                    print("ERROR: Debes seleccionar antes la opción 1 o 2", file=stderr)
                    continue
                BOOK.delete_contact(input("Introduce el nombre del contacto a borrar: "))
            case 5:
                if not flag:
                    print("ERROR: Debes seleccionar antes la opción 1 o 2", file=stderr)
                    continue
                address_book_list()
            case 6:
                if not flag:
                    print("ERROR: Debes seleccionar antes la opción 1 o 2", file=stderr)
                    continue
                filename = input("Introduce el nombre del fichero XML donde exportar la BD: ")
                if path.exists(filename):
                    overwritten = input("¿El fichero ya existe, quieres sobreescribirlo? (S/N): ")
                    if overwritten.upper() != "S":
                        break
                try:
                    BOOK.xml_export(filename)
                except FileNotFoundError:
                    print("ERROR: Nombre de Fichero o Ruta no válida.", file=stderr)
                    continue
            case 7:
                if not flag:
                    print("ERROR: Debes seleccionar antes la opción 1 o 2", file=stderr)
                    continue
                try:
                    BOOK.xml_import(input("Introduce el nombre del fichero XML: "))
                except ValueError as e:
                    print(f"ERROR: {e}", file=stderr)
        print("\n\n")


def address_book_list():
    global BOOK
    print(f"{'Lista de Contactos de Agenda':^60}")
    print(f"{'----------------------------':^60}")
    print()
    for n in BOOK.contacts:
        print(f"{f'{n[0]} | {n[1]} | {n[2]} | {n[3]}':^60}")
        print(f"{'-------------------------------------------------------------------':^60}")


if __name__ == '__main__':
    main()
