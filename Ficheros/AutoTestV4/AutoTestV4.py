"""
Necesitamos crear los ficheros (JSON o XML) donde guardar las preguntas del test. Editarlos directamente puede ser una
labor un poco engorrosa, así que vamos a hacer un programa que nos facilite la tarea.

Nuestro programa mostrará un menú con las siguientes opciones:



3. Añadir pregunta al test.

Si no se ha seleccionado o creado fichero de test se debe indicar al usuario y terminar con esta opción.
Pedimos los datos correspondientes a la pregunta, teniendo en cuenta que el enunciado puede tener varias líneas.
Comprobamos que los datos son correctos, para ello podríamos crear un objeto Question y si no lanza excepción es que están bien.
Añadimos la pregunta al fichero en el formato que tenga (JSON o XML).
Para hacer esto cargamos el JSON o XML desde el fichero a una variable, la modificamos y escribimos de nuevo en el fichero.

Author: Alejandro Priego Izquierdo
Date: 14-05-2023
"""
from question import Question
from POO.Menu.menu import Menu
from sys import stderr
from os import path

file = ""


def main():
    options = ("Crear Nuevo Test", "Cargar Test desde Archivo", "Guardar Test actual en Archivo", "Realizar Test")
    m = Menu("AutoTest V2", options)
    switch = False
    while True:
        selected = m.print_menu()

        match selected:
            case 0:
                break
            case 1:
                make_test()
                switch = True
            case 2:
                if switch:
                    confirmation = input("Se eliminarán las preguntas guardadas, ¿desea continuar? (S/N): ")
                    if confirmation.upper() == "S":
                        load_test()
                else:
                    load_test()
                    switch = True
            case 3:
                if switch:
                    save_test()
                else:
                    print("No hay ninguna pregunta guardada.")
            case 4:
                if switch:
                    do_test()
                else:
                    print("No hay ninguna pregunta guardada.")


def create_test_file():
    """
    1. Crear fichero de test.

    Pedirá al usuario una cadena con el nombre del fichero donde se almacenarán las preguntas.
    La extensión del fichero debe ser json o xml, si no es así hay que advertir de que no es posible hacerlo porque este
    programa únicamente maneja estos dos formatos.
    Si el fichero existe, se debe advertir al usuario/a de esta circunstancia y darle la opción de volver atrás.
    Finalmente se creará el fichero correspondiente.
    """

    f_name = f_name_input()
    if f_name == "fail":
        return

    if path.exists(f_name):
        overwritten = input("¿El fichero ya existe, quieres sobreescribirlo? (S/N): ")
        if overwritten.upper() != "S":
            return

    open(f_name, "wt").close()
    return


def select_test_file():
    """
    2. Seleccionar fichero de test.

    Pedirá al usuario una cadena con el nombre del fichero donde se almacenarán las preguntas.
    La extensión del fichero debe ser json o xml, si no es así hay que advertir de que no es posible hacerlo porque este
    programa únicamente maneja estos dos formatos.
    Pensad que estos dos apartados son iguales que la opción anterior, igual podemos modularizar para ahorrar código.
    Comprobamos que el fichero existe, si no es así acabamos advirtiendo del error.
    """
    global file

    f_name = f_name_input()
    if f_name == "fail":
        return

    if not path.exists(f_name):
        print("ERROR: El fichero no existe", file=stderr)
        return

    file = open(f_name, "rt")


def f_name_input():
    f_name = input("Introduzca el nombre del fichero donde se almacenarán las preguntas (XML/JSON): ")
    if not f_name_parser(f_name.lower()):
        print("ERROR: Debes introducir un fichero XML o JSON")
        return "fail"
    return f_name


def f_name_parser(filename):
    if filename[-4:] == ".xml":
        return "xml"
    elif filename[-5:] == ".json":
        return "json"
    return False


if __name__ == '__main__':
    main()
