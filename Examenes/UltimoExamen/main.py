"""
Programa de TEST para la Clase AddressBook

Author: Alejandro Priego Izquierdo
Date: 22-05-2023
"""
from menu import Menu
import AddressBook
from os import path
from sys import stderr

BOOK = AddressBook.AddressBook()


def main():
    global BOOK
    options = ("Crear desde Fichero XML", "Alta Contacto", "Baja Contacto", "Búsqueda Contacto", "Listado Agenda",
               "Exportar a Fichero XML")
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
                try:
                    BOOK = AddressBook.AddressBook(input("Introduce el nombre del fichero XML: "))
                except ValueError as e:
                    print(f"ERROR: {e}", file=stderr)
            case 2:
                tmp_name = input("Introduce el nombre del contacto: ")
                tmp_phone = input("Introduce el teléfono del contacto: ")
                tmp_email = input("Introduce el email del contacto: ")
                tmp_address = input("Introduce la dirección del contacto (opcional): ")
                try:
                    BOOK.register_contact(tmp_name, tmp_phone, tmp_email, tmp_address)
                except AddressBook.ct.PhoneIsNotValid:
                    print("ERROR: El teléfono introducido no es válido", file=stderr)
                except AddressBook.ct.EmailIsNotValid:
                    print("ERROR: El email introducido no es válido", file=stderr)
            case 3:
                try:
                    BOOK.delete_contact(input("Introduce el nombre del contacto a borrar: "))
                except AddressBook.ContactDoesNotExists:
                    print("ERROR: El contacto no existe", file=stderr)
            case 4:
                try:
                    cont = BOOK.search_contact(input("Introduce el nombre del contacto a buscar: "))
                    print(f"Nombre: {cont.name}\nTeléfono: {cont.phone}\nEmail: {cont.email}\nDirección: {cont.address}")
                except AddressBook.ContactDoesNotExists:
                    print("ERROR: El contacto no existe", file=stderr)
            case 5:
                address_book_list()
            case 6:
                filename = input("Introduce el nombre del fichero XML: ")
                if path.exists(filename):
                    overwritten = input("¿El fichero ya existe, quieres sobreescribirlo? (S/N): ")
                    if overwritten.upper() != "S":
                        break
                BOOK.xml_export(filename)
        print("\n\n")


def address_book_list():
    print(f"{'Lista de Contactos de Agenda':^60}")
    print(f"{'----------------------------':^60}")
    print()
    for n in BOOK.contacts:
        print(f"{f'{n.name} | {n.phone} | {n.email} | {n.address}':^60}")
        print(f"{'-------------------------------------------------------------------':^60}")


if __name__ == '__main__':
    main()
