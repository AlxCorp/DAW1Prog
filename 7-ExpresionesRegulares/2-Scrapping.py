"""
2. Programa que reciba una url y el nombre de una etiqueta html. Si la url es válida debe mostrar por la pantalla el contenido de cada etiqueta.

Ejemplo:
si ejecuto python miprograma https://www.iesgrancapitan.org/ title

La salida sería:
Centro Educativo IES Gran Capitán
Número de etiquetas encontradas: 1

ó si ejecuto python miprograma https://example.com/ p

La salida sería:
This domain is for use in illustrative examples in documents. You may use this domain in literature without prior coordination or asking for permission.
<a href="https://www.iana.org/domains/example">More information...</a>
Número de etiquetas encontradas: 2

Author: Alejandro Priego Izquierdo
Date: 12-05-2023
"""
from sys import argv, stderr
from requests import request
import re

if len(argv) != 3:
    print("ERROR: Debes introducir 2 argumentos.", file=stderr)
    quit(1)

URL = argv[1]
WEBRQ = request('GET', URL).text.replace("\n", "").replace("    ", "\n")
TAG = argv[2]
REGEX = re.compile(r'<p>.*?</p>', re.DOTALL)

results = re.findall(REGEX, WEBRQ)

if not results:
    print("No se han encontrado resultados")
    quit(0)

for n in results:
    print(n, "\b")

print("\nSe han encontrado", len(results), "resultados.")
