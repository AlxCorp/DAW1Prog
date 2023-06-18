"""
Realiza un programa que escoja al azar 5 palabras en español del mini-diccionario del ejercicio anterior. El programa
irá pidiendo que el usuario teclee la traducción al inglés de cada una de las palabras y comprobará si son correctas.
Al final, el programa deberá mostrar cuántas respuestas son válidas y cuántas erróneas.

Author: Alejandro Priego Izquierdo
Date: 21-03-2023
"""

DICT = {'Porque': 'Because', 'Tiempo': 'Time', 'Año': 'Year', 'Día': 'Day', 'Vida': 'Life',
        'Thing': 'Cosa', 'Man': 'Hombre', 'Mundo': 'World', 'Mano': 'HHand', 'Ojo': 'Eye',
        'Cerveza': 'Beer', 'Mujer': 'Woman', 'Trabajo': 'Work', 'Vino': 'Wine', 'Semana': 'Week',
        'Punto': 'Point', 'Niño': 'Child', 'Escuela': 'School', 'Cafe': 'Coffee', 'Cacao': 'Cocoa'}

PALABRAS = 5
marcador = 0

palabras = list()
for _ in range(PALABRAS):
    palabras.append(DICT.popitem())

for i in palabras:
    palabra = input(f"Introduzca la traducción para {i[0]}: ").title()

    if palabra == i[1]:
        marcador += 1

print(f"Aciertos: {marcador}  |  Fallos: {PALABRAS-marcador}  |  TOTAL PREGUNTAS: {PALABRAS}")
