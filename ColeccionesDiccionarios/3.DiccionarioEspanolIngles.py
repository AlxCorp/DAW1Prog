"""
Crea un mini-diccionario español-inglés que contenga, al menos, 20 palabras (con su correspondiente traducción). Utiliza
un diccionario para almacenar las parejas de palabras. El programa pedirá una palabra en español y dará la
correspondiente traducción en inglés.

Author: Alejandro Priego Izquierdo
Date: 21-03-2023
"""

DICT = {'Porque': 'Because', 'Tiempo': 'Time', 'Año': 'Year', 'Día': 'Day', 'Vida': 'Life',
        'Thing': 'Cosa', 'Man': 'Hombre', 'Mundo': 'World', 'Mano': 'HHand', 'Ojo': 'Eye',
        'Cerveza': 'Beer', 'Mujer': 'Woman', 'Trabajo': 'Work', 'Vino': 'Wine', 'Semana': 'Week',
        'Punto': 'Point', 'Niño': 'Child', 'Escuela': 'School', 'Cafe': 'Coffee', 'Cacao': 'Cocoa'}

while True:
    palabra = input("Introduzca la palabra a traducir ('Ctrl + C' para salir): ").title()

    if palabra in DICT:
        print(f'La traducción de {palabra} es {DICT[palabra]} \n')
    else:
        print(f'Lo siento, palabra no encontrada. :/ \n')
