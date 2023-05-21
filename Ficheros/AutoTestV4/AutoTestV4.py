"""
Necesitamos crear los ficheros (JSON o XML) donde guardar las preguntas del test. Editarlos directamente puede ser una
labor un poco engorrosa, así que vamos a hacer un programa que nos facilite la tarea.

Nuestro programa mostrará un menú con las siguientes opciones:

Author: Alejandro Priego Izquierdo
Date: 14-05-2023
"""
from question import Question
from POO.Menu.menu import Menu
from sys import stderr
from os import path
import json
import xml.etree.ElementTree as ET
from xml.dom import minidom

file = ""


def main():
    options = ("Crear Nuevo Test", "Seleccionar Test Existente", "Agregar Pregunta")
    m = Menu("AutoTest V4", options)
    while True:
        selected = m.print_menu()

        match selected:
            case 0:
                break
            case 1:
                create_test_file()
            case 2:
                select_test_file()
            case 3:
                add_question()


def create_test_file():
    """
    1. Crear fichero de test.

    Pedirá al usuario una cadena con el nombre del fichero donde se almacenarán las preguntas.
    La extensión del fichero debe ser json o xml, si no es así hay que advertir de que no es posible hacerlo porque este
    programa únicamente maneja estos dos formatos.
    Si el fichero existe, se debe advertir al usuario/a de esta circunstancia y darle la opción de volver atrás.
    Finalmente se creará el fichero correspondiente.
    """
    global file

    f_name = f_name_input()
    if f_name == "fail":
        print("ERROR: Nombre no válido", file=stderr)
        return

    if path.exists(f_name):
        overwritten = input("¿El fichero ya existe, quieres sobreescribirlo? (S/N): ")
        if overwritten.upper() != "S":
            return

    open(f_name, "wt").close()
    file = f_name
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

#    file = open(f_name, "rt")
    file = f_name


def add_question():
    """
    3. Añadir pregunta al test.

    Si no se ha seleccionado o creado fichero de test se debe indicar al usuario y terminar con esta opción.
    Pedimos los datos correspondientes a la pregunta, teniendo en cuenta que el enunciado puede tener varias líneas.
    Comprobamos que los datos son correctos, para ello podríamos crear un objeto Question y si no lanza excepción es que
    están bien.
    Añadimos la pregunta al fichero en el formato que tenga (JSON o XML).
    Para hacer esto cargamos el JSON o XML desde el fichero a una variable, la modificamos y escribimos de nuevo en el
    fichero.
    """
    global file

    if file == "":
        print("ERROR: No has seleccionado o creado ningún archivo.", file=stderr)
        return

    tmp_name = input(f"Ingrese el nombre para la pregunta: ")
    tmp_statement = []
    while "." not in tmp_statement:
        tmp_statement.append(input(f"Ingrese el enunciado para la pregunta (. para finalizar): "))
    tmp_statement = "\n".join(tmp_statement)
    tmp_answer = []
    for n in range(4):
        tmp_answer_text = input(f"Ingrese el texto para la respuesta número {n + 1}: ")
        tmp_answer_qualification = float(
            input(f"Ingrese el porcentaje (entre '-1' y '+1') para la respuesta número {n + 1}: "))
        tmp_answer.append((tmp_answer_text, tmp_answer_qualification))

    try:
        question = Question(tmp_name, tmp_statement, tmp_answer)
    except:
        print("Algo ha ido mal... Inténtalo de nuevo", file=stderr)
        return

    if f_name_parser(file) == "json":
        save_json(question)
    else:
        save_xml(question)


def save_json(question):
    f_name = file

    questions = []
    raw_questions = []

    with open(f_name, "rt", encoding="UTF-8") as f:
        f_json = json.load(f)

        if isinstance(f_json, dict):
            f_json = [f_json]

        for i in f_json:
            questions.append(Question(i["name"], i["statement"], i["options"], i["points"]))

    questions.append(question)

    for n in questions:
        raw_questions.append({"name": n.name, "statement": n.statement, "options": n.answers, "points": n.score})

    with open(f_name, "wt", encoding="UTF-8") as f:
        f.write(json.dumps(raw_questions, indent=3, ensure_ascii=True))
    print("\n")


def save_xml(question):
    f_name = file
    try:
        tree = ET.parse(f_name)
    except:
        with open(f_name, "wt") as f:
            f.write('<?xml version="1.0" encoding="utf-8"?>\n<test>\n</test>')
        tree = ET.parse(f_name)
    root = tree.getroot()

    qst = ET.Element('question', {'name': question.name, 'base_score': str(question.score)})
    ET.SubElement(qst, 'statement').text = question.statement
    opts = ET.SubElement(qst, 'options')
    for answer in question.answers:
        ET.SubElement(opts, 'option', {'weight': str(answer[1])}).text = answer[0]
    root.append(qst)

    xml_minidom = minidom.parseString(ET.tostring(root))
    xml_str = xml_minidom.toprettyxml()
    with open(f_name, 'w', encoding="UTF-8") as archivo:
        archivo.write(xml_str)


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
