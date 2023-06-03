"""
Programa de TEST para la Clase AddressBook

Author: Alejandro Priego Izquierdo
Date: 22-05-2023
"""
from menu import Menu
import AddressBook
from os import path, getenv
from sys import stderr
from dotenv import load_dotenv
import mysql.connector

load_dotenv("secrets.env")
ROOT = getenv('ROOT')
book = None


def main():
    global ROOT, book
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
                book = AddressBook.AddressBook(ROOT, dbname, dbuser, dbpassword)
                flag = True
            case 2:
                if flag and input("Ya hay cargada una BADA, ¿SOBREESCRIBIR? (S/N): ").upper() != "S":
                    continue
                dbname = input("Introduzca el nombre de la Base de Datos a abrir: ")
                dbuser = input("Introduzca el usuario de la Base de Datos a abrir: ")
                dbpassword = input("Introduzca la contraseña del usuario de la Base de Datos: ")
                book = AddressBook.AddressBook(ROOT, dbname, dbuser, dbpassword)
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
                    book.register_contact(tmp_name, tmp_phone, tmp_email, tmp_address)
                except AddressBook.ct.PhoneIsNotValid:
                    print("ERROR: El teléfono introducido no es válido", file=stderr)
                except AddressBook.ct.EmailIsNotValid:
                    print("ERROR: El email introducido no es válido", file=stderr)
            case 4:
                if not flag:
                    print("ERROR: Debes seleccionar antes la opción 1 o 2", file=stderr)
                    continue
                try:
                    book.delete_contact(input("Introduce el nombre del contacto a borrar: "))
                except AddressBook.ContactDoesNotExists:
                    print("ERROR: El contacto no existe", file=stderr)
            case 5:
                if not flag:
                    print("ERROR: Debes seleccionar antes la opción 1 o 2", file=stderr)
                    continue
                address_book_list()


            case 1:
                try:
                    book = AddressBook.AddressBook(input("Introduce el nombre del fichero XML: "))
                except ValueError as e:
                    print(f"ERROR: {e}", file=stderr)
            case 6:
                filename = input("Introduce el nombre del fichero XML: ")
                if path.exists(filename):
                    overwritten = input("¿El fichero ya existe, quieres sobreescribirlo? (S/N): ")
                    if overwritten.upper() != "S":
                        break
                book.xml_export(filename)
        print("\n\n")


def address_book_list():
    global book
    print(f"{'Lista de Contactos de Agenda':^60}")
    print(f"{'----------------------------':^60}")
    print()
    for n in book.contacts:
        print(n)
        # print(f"{f'{n.name} | {n.phone} | {n.email} | {n.address}':^60}")
        print(f"{'-------------------------------------------------------------------':^60}")


if __name__ == '__main__':
    main()
