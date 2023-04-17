import csv
import os.path, sys

FILE = "datos.csv"

""" Comprobamos que exista el archivo """
if not os.path.exists(FILE):
    print(f"El fichero {FILE} no existe. Terminamos...", file=sys.stderr)
    exit(1)

with open("datos.csv", encoding="UTF-8") as csv_file:   # Abrimos como LECTURA y en modo TEXTO (aunque no se indique)
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        print(f"{row['nombre']} trabaja como {row['puesto']} y nació en el mes de {row['mes de nacimiento']}")
