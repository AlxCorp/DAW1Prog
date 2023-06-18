import csv

FILE = "datos.csv"

with open(FILE, mode='at') as csv_file:     # Abrimos en ESCRITURA y modo TEXTO.
    csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    # delimiter indica el carácter para separar cada campo. (Por defecto ',')
    # quotechar indica el carácter para "encofrar" cada campo. (Por defecto '"')
    # quoting indica que tipo texto entre comillas, te guarda las comillas, y puedes meter unos con y otros sin comillas

    csv_writer.writerow(['Pepe Guacamole', 'Contable', 'noviembre'])
    csv_writer.writerow(['Hola Caracola', 'IT', 'enero'])
