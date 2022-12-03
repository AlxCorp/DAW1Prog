# Se desea almacenar las calificaciones del alumnado de 1DAW del IES Gran Capitán en los módulos de PROGRAMACIÓN,
# LENGUAJE DE MARCAS, BASES DE DATOS Y SISTEMAS INFORMÁTICOS.
# Author: Alejandro Priego Izquierdo
# Date: 26/11/2022
import sys

# Encabezado del ejercicio
print("")
print("Este programa almacena las calificaciones del alumnado")
print("------------------------------------------------------")

modulos = ["PROGRAMACIÓN", "LENGUAJE DE MARCAS", "BASE DE DATOS", "SISTEMAS INFORMÁTICOS"]
alumnos_nombre = []
alumnos_notas = []
contador_alumno = 1


def nuevo_alumno(nombre, apellidos, *notas):
    global contador_alumno

    dictionary = contador_alumno, nombre, apellidos
    alumnos_nombre.append(dictionary)
    contador_alumno += 1

    alumnos_notas.append(notas)


while True:
    nombre_temporal = input("Introduce el nombre del alumno: ").title()  # Title capitaliza todas las palabras
    if nombre_temporal == "":
        print()
        break

    apellidos_temporal = input("Introduce los apellidos del alumno: ").title()
    while len(apellidos_temporal) == 0:
        print("Debe introducir al menos un apellido!", sys.stderr)
        apellidos_temporal = input("Introduce los apellidos del alumno: ").title()

    notas_temporal = []
    for i in range(4):
        x = float(input(f"Introduce la nota del alumno en {modulos[i]}: "))
        while x < 0 or x > 10:
            print("Debe introducir una nota entre 0 y 10!", sys.stderr)
            x = float(input(f"Introduce la nota del alumno en {modulos[i]}: "))
        notas_temporal.append(x)

    nuevo_alumno(nombre_temporal, apellidos_temporal, notas_temporal[0], notas_temporal[1], notas_temporal[2],
                 notas_temporal[3])


# Función para imprimir calificaciones totales de todos los estudiantes
def imprimir_calificaciones():
    print(f"Calificaciones Curso")
    print(f"--------------------")
    print(f'{"Nombre":^10}  {"Apellidos":^25}  |  {modulos[0]:^21}  {modulos[1]:^21}  {modulos[2]:^21}  '
          f'{modulos[3]:^21}')
    for numero_alumno in range(contador_alumno - 1):
        print(f"{alumnos_nombre[numero_alumno][1]:^10}  {alumnos_nombre[numero_alumno][2]:^25}  "
              f"|  {alumnos_notas[numero_alumno][0]:^21}  {alumnos_notas[numero_alumno][1]:^21}  "
              f"{alumnos_notas[numero_alumno][2]:^21}  {alumnos_notas[numero_alumno][3]:^21}")


def imprimir_calificaciones_alumno():
    nombre = input("Ingrese el nombre del alumno: ").title()
    apellido = input("Ingrese los apellidos del alumno: ").title()
    print()
    print(f"Calificaciones Curso Alumno Concreto")
    print(f"------------------------------------")
    print(f'{"Nombre":^10}  {"Apellidos":^25}  |  {modulos[0]:^21}  {modulos[1]:^21}  {modulos[2]:^21}  '
          f'{modulos[3]:^21}')

    def buscar_alumno(nombre, apellido):
        for alumno in alumnos_nombre:
            if nombre in alumno:
                return alumno.index(nombre)
            elif apellido in alumno:
                return alumno.index(apellido)
        print("Alumno no encontrado!")

    numero_alumno = buscar_alumno(nombre, apellido)

    print(f"{nombre:^10}  {apellido:^25}  "
          f"|  {alumnos_notas[numero_alumno - 1][0]:^21}  {alumnos_notas[numero_alumno - 1][1]:^21}  "
          f"{alumnos_notas[numero_alumno - 1][2]:^21}  {alumnos_notas[numero_alumno - 1][3]:^21}")


def nota_media_modulo():
    print("Los módulos son: PROGRAMACIÓN, LENGUAJE DE MARCAS, BASE DE DATOS, SISTEMAS INFORMÁTICOS")
    modulo = input("Ingrese el nombre del módulo: ").upper()
    modulo_index = modulos.index(modulo)

    media = 0
    for nota in range(contador_alumno - 1):
        if modulo_index == 0:
            media += alumnos_notas[nota][0]
        elif modulo_index == 1:
            media += alumnos_notas[nota][1]
        elif modulo_index == 2:
            media += alumnos_notas[nota][2]
        elif modulo_index == 3:
            media += alumnos_notas[nota][3]
    media /= contador_alumno

    print("La media del módulo", modulo, "es de", media)


def nota_maxima_modulo():
    print("Los módulos son: PROGRAMACIÓN, LENGUAJE DE MARCAS, BASE DE DATOS, SISTEMAS INFORMÁTICOS")
    modulo = input("Ingrese el nombre del módulo: ").upper()
    modulo_index = modulos.index(modulo)

    notas = []
    for nota in range(contador_alumno - 1):
        if modulo_index == 0:
            notas.append(alumnos_notas[nota][0])
        elif modulo_index == 1:
            notas.append(alumnos_notas[nota][1])
        elif modulo_index == 2:
            notas.append(alumnos_notas[nota][2])
        elif modulo_index == 3:
            notas.append(alumnos_notas[nota][3])

    notas_ordered = notas.copy()
    notas_ordered.sort()

    alumno_id = notas.index(notas_ordered[-1])

    print("La nota máxima del módulo", modulo, "es de", notas_ordered[-1], "perteneciente a",
          alumnos_nombre[alumno_id][1], alumnos_nombre[alumno_id][2])


def nota_minima_modulo():
    print("Los módulos son: PROGRAMACIÓN, LENGUAJE DE MARCAS, BASE DE DATOS, SISTEMAS INFORMÁTICOS")
    modulo = input("Ingrese el nombre del módulo: ").upper()
    modulo_index = modulos.index(modulo)

    notas = []
    for nota in range(contador_alumno - 1):
        if modulo_index == 0:
            notas.append(alumnos_notas[nota][0])
        elif modulo_index == 1:
            notas.append(alumnos_notas[nota][1])
        elif modulo_index == 2:
            notas.append(alumnos_notas[nota][2])
        elif modulo_index == 3:
            notas.append(alumnos_notas[nota][3])

    notas_ordered = notas.copy()
    notas_ordered.sort()

    alumno_id = notas.index(notas_ordered[1])

    print("La nota máxima del módulo", modulo, "es de", notas_ordered[1], "perteneciente a",
          alumnos_nombre[alumno_id][1], alumnos_nombre[alumno_id][2])


while True:
    print()
    print("1. Imprimir Calificaciones Completas")
    print("2. Imprimir Calificaciones Alumno Concreto")
    print("3. Imprimir Nota Media Módulo")
    print("4. Imprimir Nota Máxima Módulo")
    print("5. Imprimir Nota Mínima Módulo")
    print("6. Imprimir Listado Ordenado con Respecto a Nota")
    print("0. Salir del Programa")
    print("------------------------------------------------")
    menu = int(input("Por favor, escoja la opción que desee realizar: "))

    match menu:
        case 1:
            imprimir_calificaciones()
        case 2:
            imprimir_calificaciones_alumno()
        case 3:
            nota_media_modulo()
        case 4:
            nota_maxima_modulo()
        case 5:
            nota_minima_modulo()
        case 6:
            pass
        case 0:
            quit()
