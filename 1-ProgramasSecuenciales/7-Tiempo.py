# 7. Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos
# corresponde.

minutos = int(input("Indica el tiempo en minutos: "))   # Pedimos minutos

horas = minutos//60             # Convertimos los minutos a horas y minutos
minutosSolo = minutos % 60

print("Equivale a", horas, "horas y", minutosSolo, "minutos.")     # Imprimimos el resultado
