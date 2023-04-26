"""
Escribe un programa capaz de quitar los comentarios de un programa de Java.
Se utilizaría de la siguiente manera:
    python quita-comentarios.py <PROGRAMA_ORIGINAL> <PROGRAMA_LIMPIO>
    Por ejemplo:
        python quita-comentarios.py Holav1.java Holav2.java
        crea un fichero con nombre Holav2.java que contiene el código de Holav1.java pero sin los comentarios.

Author: Alejandro Priego Izquierdo
Date: 25/04/2023
"""
import re
from sys import argv

if len(argv) == 1 or len(argv) == 2:
    raise ValueError("Debes ingresar DOS argumentos.")

f1 = open(argv[1], mode="r", encoding="utf-8")
f2 = open(argv[2], mode="w", encoding="utf-8")

for line in f1:
    linea_sin_comentarios = re.sub(r'//.*|/\*.*?\*/', '', line)
    f2.write(linea_sin_comentarios)

f1.close()
f2.close()
