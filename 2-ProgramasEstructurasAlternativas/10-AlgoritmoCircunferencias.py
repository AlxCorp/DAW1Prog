# Algoritmo que pida los puntos centrales x1,y1,x2,y2 y los radios r1,r2 de dos circunferencias y las clasifique en
# uno de estos estados:
# exteriores / tangentes exteriores / secantes / tangentes interiores / interiores / concéntricas
#
# Author: Alejandro Priego Izquierdo
# Date: 19/10/2022

# Encabezado del ejercicio
print("")
print("Este programa clasifica las circunferencias en varios estados")
print("-------------------------------------------------------------")

# Preguntamos las variables
x1 = float(input("Ingrese el punto central x1: "))
y1 = float(input("Ingrese el punto central y1: "))
x2 = float(input("Ingrese el punto central x2: "))
y2 = float(input("Ingrese el punto central y2: "))
r1 = float(input("Ingrese el radio r1: "))
r2 = float(input("Ingrese el radio r2: "))

# Operaciones Recurrentes
distanciaX = x2 - x1
distanciaY = y2 - y1
DISTANCIA = pow((distanciaX ** 2) + (distanciaY ** 2), 1 / 2)   # raíz2((x2-x1)e2+(y2,y1)e2)
sumaRadios = r1 + r2
difRadios = r1 - r2

if DISTANCIA > sumaRadios:
    print("Estas son Circunferencias Exteriores")
elif DISTANCIA == sumaRadios:
    print("Estas son Circunferencias Tangentes Exteriores")
elif sumaRadios > DISTANCIA > difRadios:
    print("Estas son Circunferencias Secantes")
elif DISTANCIA == abs(difRadios):
    print("Estas son Circunferencias Tangentes Interiores")
elif DISTANCIA < difRadios:
    print("Estas son Circunferencias Interiores")
else:
    print("Estas son Circunferencias Interiores Concéntricas")
