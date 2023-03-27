"""
Ejemplo de distintas formas de leer un fichero.

Author: Alejandro Priego Izquierdo
"""
print("Distintas formas de leer un fichero")
print("-----------------------------------")

# 1º. Línea a línea:
f = open("palabras.csv", "rt", encoding='utf-8')  # Se coloca cabeza de lectura en el primer byte
line = f.readline()  # Leo bytes desde principio hasta primer \n (Salto de línea)
linePointer1 = 0
while line != "":
    linePointer1 += 1
    print(f"Leida la línea {linePointer1}: {line.rstrip()}")  # Se escribe línea sin salto de línea final
    line = f.readline()
f.close()


# 2º. Fichero entero, en una instrucción, se almacena en lista.
# Se usa "with" para no tener que cerrar el fichero
with open("palabras.csv", "rt", encoding='utf-8') as f:  # Se coloca cabeza de lectura en el primer byte
    lines = f.readlines()   # Leer to-do el fichero y crear lista
    for n, line in enumerate(lines):
        print(f"Leida la línea {n+1}: {line.rstrip()}")


# 3º. Fichero entero, en una instrucción, se almacena en str.
# Capturamos excepción por si hay problema en la apertura.
try:
    f = open("palabras.csv", "rt", encoding="utf-8")
    lines = f.read()    # Leo to-do el fichero como cadena de caracteres.
    print(lines)
    f.close()
except FileNotFoundError:
    print("No se ha podido abrir el fichero.")


# 4º. Ciclo for.
try:
    f = open("palabras.csv", "rt", encoding="utf-8")
    for n, line in enumerate(f):
        print(f"Leida la línea {n+1}: {line.rstrip()}")     # Evitamos dos saltos de línea.
    f.close()
except FileNotFoundError:
    print("No se ha podido abrir el fichero.")


# 5º. Ciclo for y guardar en diccionario.
try:
    d = dict()
    f = open("palabras.csv", "rt", encoding="utf-8")
    f.readline()    # Así eliminamos la cabecera del archivo
    for line in f:
        entry = line.split(",")     # Evitamos dos saltos de línea.
        word, translation = entry[0], entry[1]
        d[word] = translation.rstrip()
    f.close()
    print(d)
except FileNotFoundError:
    print("No se ha podido abrir el fichero.")
