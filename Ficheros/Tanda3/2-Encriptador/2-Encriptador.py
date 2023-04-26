"""
Crea un programa que encripte un fichero que le pasamos como parámetro y almacene el resultado en otro, que también
pasamos como parámetro, de manera que:

    - Si el programa no recibe el número de parámetros adecuado termina con un error 1.
    - Si el programa recibe un solo parámetro guardará la información encriptada en el mismo archivo del que lee, pero
        antes advertirá al usuario de que machacará el archivo origen, dando opción a que la operación no se haga.
    - Si el fichero origen no existe (da error al abrirlo como lectura) el programa termina con un mensaje de error y
        código 2.
    - Si en el fichero destino no se puede escribir (da error al abrirlo como escritura) el programa termina con un
        mensaje de error y código 3.
    - Para encriptar usa el método César, necesitarás una clave que debes pedir al usuario.

Author: Alejandro Priego Izquierdo
Date: 25/04/2023
"""
from sys import argv, stderr
from random import randint as rng

one_file = False

if len(argv) == 2:
    if input(f"Se va a sobreescribir el fichero {argv[1]}, está seguro? (S/N): ").upper() == "S":
        try:
            f2 = open(argv[1], "wt")
            one_file = True
        except:
            print("ERROR: No puede abrirse el fichero", file=stderr)
            quit(2)
    else:
        quit(0)

if len(argv) < 2 or len(argv) > 4:
    print("ERROR: Debes ingresar TRES argumentos", file=stderr)
    quit(1)

try:
    f1 = open(argv[1], "rt")
except:
    print("ERROR: No puede abrirse el fichero", file=stderr)
    quit(2)

if not one_file:
    try:
        f2 = open(argv[2], "wt")
    except:
        print("ERROR: No puede abrirse el fichero", file=stderr)
        quit(2)

"""
lower_letters = [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90]
upper_letters = [97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117,
                 118, 119, 120, 121, 122]
"""


def cifrado_cesar(message, key):
    result = ""
    for letter in message:
        if letter.isalpha():
            if letter.isupper():
                for n in range(key):
                    if 96 < ord(letter) < 122:
                        new_letter = ord(letter) + 1
                    else:
                        new_letter = 97
            else:
                for n in range(key):
                    if 64 < ord(letter) < 90:
                        new_letter = ord(letter) + 1
                    else:
                        new_letter = 65
            result += chr(new_letter)
        else:
            result += letter

    return result


f2.write(cifrado_cesar(f1.read(), int(argv[3])))

f1.close()
f2.close()
