"""
1. Programa que recibe dos parámetros: un fichero de texto y una cadena que le indica qué información va extraer del
    mismo, después muestra por la pantalla los datos extraídos.

Los posibles valores del segundo parámetro y la información que extrae es:

DNI: extrae los DNIs.
IP: extrae las direcciones IP.
MAT: extrae matrículas de coche con formato 0000XXX.
HEX: extrae números hexadecimales. Entendemos que las letras entre A y F son en mayúsculas y el número empieza con #.
FEC: extrae fechas con formato dd/mm/aaaa.
TWT: extrae usuarios de twitter: empieza por @ y puede contener letras mayusculas y minusculas, numeros, guiones y
    guiones bajos.
El programa tiene que ser en relación a su complejidad y número de líneas lo más eficiente posible.

Author: Alejandro Priego Izquierdo
Date: 12-05-2023
"""
from sys import argv, stderr
import re

OPTIONS = {"DNI": "[0-9]{8}[ABCDEFGHJKLMNPQRSTUVWXYZ]",
           "IP": "((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}",
           "MAT": "[0-9]{4}(?!.*(LL|CH))[BCDFGHJKLMNPRSTVWXYZ]{1,3}",
           "HEX": "#[0-9A-F]+",
           "FEC": "([0-2][0-9]|3[0-1])\/(0[1-9]|1[0-2])\/(\d{4})",
           "TWT": "@[a-zA-Z0-9-_]+"
           }

if len(argv) != 3:
    print("ERROR: Debes introducir 2 argumentos.", file=stderr)
    quit(1)

FILE = argv[1]

if argv[2].upper() not in OPTIONS.keys():
    print("ERROR: Valor no válido. Los valores permitidos para el segundo argumento son: DNI|IP|MAT|HEX|FEC|TWT",
          file=stderr)
    quit(1)
opt = OPTIONS[argv[2].upper()]

with open(FILE, "rt") as f:
    file = f.read()
    for n in re.findall(opt, file):
        print(n)
