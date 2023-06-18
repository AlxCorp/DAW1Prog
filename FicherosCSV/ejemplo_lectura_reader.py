import csv
import os.path, sys

FILE = "datos.csv"

""" Comprobamos que exista el archivo """
if not os.path.exists(FILE):
    print(f"El fichero {FILE} no existe. Terminamos...", file=sys.stderr)
    exit(1)

with open("datos.csv", "rt", encoding="UTF-8") as csv_file:   # Abrimos como LECTURA y en modo TEXTO
    csv_reader = csv.reader(csv_file)
    next(csv_reader)    # Nos saltamos la primera línea/fila (encabezado).
    for row in csv_reader:
        print(f"{row[0]} trabaja como {row[1]} y nació en el mes de {row[2]}")
