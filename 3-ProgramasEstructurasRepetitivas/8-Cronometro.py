# Escribe un cronómetro
# Author: Alejandro Priego Izquierdo
# Date: 31/10/2022

# Encabezado del ejercicio
from time import sleep
from keyboard import is_pressed

print("")
print("Este programa es un cronómetro")
print("------------------------------")

# Preguntamos las variables
segundos = -1
minutos = 0
horas = 0

status = input("Introduzca I para Iniciar, P para Pausar y Q para Quitar: ").upper()
print(f"{horas:02d}:{minutos:02d}:{segundos:02d}", end="")

while True:
    while status == "I":
        print(8 * "\b", end="")
        segundos += 1

        if is_pressed("p"):
            status = "P"
            break

        if segundos == 60:
            minutos += 1
            segundos -= 60

        if minutos == 60:
            horas += 1
            minutos -= 60

        print(f"{horas:02d}:{minutos:02d}:{segundos:02d}", end="", flush=True)
        sleep(1)
#        print(8 * "\b", end="")

        if is_pressed("q"):
            status = "Q"
            break

    while status == "P":
        print("Cronómetro en Pausa, para reanudar escriba C y pulse Enter")
        print(horas, ":", minutos, ":", segundos)
        status = input().upper()

        if status == "C":
            status = "I"
            break

        if is_pressed("q"):
            status = "Q"
            break

    while status == "Q":
        print("Cronómetro finalizado correctamente")
        quit()
