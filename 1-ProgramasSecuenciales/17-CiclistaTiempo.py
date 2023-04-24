# 17. Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. El tiempo de viaje hasta llegar
#  a otra ciudad B es de T segundos. Escribir un algoritmo que determine la hora de llegada a la ciudad B.

A = input("Indica el nombre de la ciudad de Salida: ")  # Preguntamos las diferentes horas de salida y llegada
HH = int(input("Indica la hora de salida: "))
MM = int(input("Indica el minuto de salida: "))
SS = int(input("Indica el segundo de salida: "))
B = input("Indica el nombre de la ciudad de Llegada: ")
tmp = int(input("Indica el tiempo en llegar a B en Segundos: "))

horaSalida = (HH * 60 * 60) + (MM * 60) + SS    # Convertimos la hora de salida a segundos
horaTotal = horaSalida + tmp    # Sumamos la hora de salida a la de llegada

tToHour = horaTotal // 60 // 60  # Convertimos el tiempo final a horas
horaTotal -= tToHour * 60 * 60   # Restamos las horas
tToMin = (horaTotal // 60)       # Convertimos el tiempo restante a minutos
horaTotal -= tToMin * 60         # Restamos los minutos
tToSeg = horaTotal               # Asignamos el resto a los segundos

horaSalida = str(HH) + ":" + str(MM) + ":" + str(SS)        # Guardamos la hora de salida formateada
horaLlegada = str(tToHour) + ":" + str(tToMin) + ":" + str(tToSeg)  # Guardamos la hora de llegada formateada

# Imprimimos horas de llegada y salida
print("El ciclista sale de", A, "a las", horaSalida, "y llega a", B, "a las", horaLlegada)
