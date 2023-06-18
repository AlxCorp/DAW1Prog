from sys import argv
from ping3 import ping

if len(argv) < 2:
    print("Debes introducir la IP como argumento")
elif len(argv) > 2:
    print("Solo puedes introducir UN argumento")

ping = ping(argv[1])

print(ping)
