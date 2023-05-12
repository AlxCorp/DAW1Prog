"""
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
"""
from sys import stderr
from random import choices

while True:
    LENGTH = int(input("Indica la longitud de la contraseña? (8 - 16): "))
    if LENGTH < 8 or LENGTH > 16:
        print("Debes introducir un valor entre 8 y 16!", file=stderr)
    else:
        break

UPPER_CASE = (input("Quieres incluir letras mayúsculas? (S/N): ").upper() == "S")
NUMBERS = (input("Quieres incluir números? (S/N): ").upper() == "S")
SYMBOLS = (input("Quieres incluir símbolos? (S/N): ").upper() == "S")

LOWER_LETTER_LIST = list("abcdefghijklmnopqrstuvwxyz")
UPPER_LETTER_LIST = list("abcdefghijklmnopqrstuvwxyz".upper())
NUMBERS_LIST = list("1234567890")
SYMBOLS_LIST = list("!@#$%^&*()_+=-}{][';:.><,/?\\|")

generator_list = []

generator_list.extend(LOWER_LETTER_LIST)
if UPPER_CASE:
    generator_list.extend(UPPER_LETTER_LIST)
if NUMBERS:
    generator_list.extend(NUMBERS_LIST)
if SYMBOLS:
    generator_list.extend(SYMBOLS_LIST)


print("".join(choices(generator_list, k=LENGTH)))
