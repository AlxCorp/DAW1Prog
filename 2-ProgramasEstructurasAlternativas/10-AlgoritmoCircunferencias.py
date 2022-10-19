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

DISTANCIAX = abs(x1 - x2)
DISTANCIAY = abs(y1 - y2)

if DISTANCIAX != 0 or DISTANCIAY != 0 and

# https://www.edu.xunta.gal/espazoAbalar/sites/espazoAbalar/files/datos/1445431865/contido/ud6/23_posiciones_relativas_entre_dos_circunferencias.html#:~:text=La%20posici%C3%B3n%20relativa%20de%20dos,la%20suma%20de%20sus%20radios.