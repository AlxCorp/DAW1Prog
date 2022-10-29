# Escribe un programa que pida el límite inferior y superior de un intervalo. Si el límite inferior es mayor que el
# superior lo tiene que volver a pedir.
# Author: Alejandro Priego Izquierdo
# Date: 27/10/2022

# Encabezado del ejercicio
print("")
print("Este programa imprime ciertos valores entre intervalos")
print("------------------------------------------------------")

inferior = 1
superior = 0

# Preguntamos las variables
while superior < inferior:
    inferior = int(input("Ingrese el límite inferior: "))
    superior = int(input("Ingrese el límite superior: "))
    if superior < inferior:
        print("Recuerda que el límite inferior debe ser INFERIOR al límite superior")

sumaIntervalo = 0
fueraIntervalo = 0
igualLimite = 0
contador = 0

while True:
    number = int(input("Ingrese un número: "))
    contador += 1

    if number == 0:
        break
    elif number > inferior or number < superior:
        sumaIntervalo += number
    elif number == inferior or number == superior:
        igualLimite += 1
    elif number < inferior or number > superior:
        fueraIntervalo += 1
    else:
        print("ERROR: Por favor, ingresa un valor válido")

print(f"Has ingresado un total de {contador} números para comprobar en el intervalo entre {inferior} y {superior}, de "
      f"los cuales hemos obtenido:")
print()
print(f"{sumaIntervalo} de la suma de los números dentro del intervalo")
print(f"{fueraIntervalo} números fuera del intervalo")
print(f"{igualLimite} números iguales a los límites")
