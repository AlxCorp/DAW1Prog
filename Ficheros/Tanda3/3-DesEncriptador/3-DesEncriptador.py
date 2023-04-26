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

one_file = False

if len(argv) == 3:
    if input(f"Se va a sobreescribir el fichero {argv[1]}, está seguro? (S/N): ").upper() == "S":
        try:
            f2 = open(argv[1], "wt")
            one_file = True
        except:
            print("ERROR: No puede abrirse el fichero", file=stderr)
            quit(2)
    else:
        quit(0)

if len(argv) < 3 or len(argv) > 4:
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


def cifrado_cesar(message, key):
    result = ""
    for letter in message:
        if letter.isalpha():
            position = ord(letter) - ord('a')
            new_position = (position - key) % 26
            new_letter = chr(new_position + ord('a'))
            result += new_letter
        else:
            result += letter

    return result


f2.write(cifrado_cesar(f1.read(), int(argv[3])))

f1.close()
f2.close()