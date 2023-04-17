import csv

FILE = "palabras.csv"

with open(FILE, mode='wt') as csv_file:
    fieldnames = ['castellano', 'inglés']
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    csv_writer.writeheader()
    csv_writer.writerow({'castellano': 'leche', 'inglés': 'milk'})
    csv_writer.writerow({'castellano': 'manzana', 'inglés': 'apple'})