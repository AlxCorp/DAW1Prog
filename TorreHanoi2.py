num = int(input("Introduce el número de discos: "))


def hanoi(origen, destino, auxiliar, discos=num):
    if discos == 1:
        print(f"Movemos del palo {origen} al {destino}")
    else:
        hanoi(origen, auxiliar, destino, discos-1)
        print(f"Movemos del palo {origen} al {destino}")
        hanoi(auxiliar, destino, origen, discos-1)


hanoi("A", "B", "C")
