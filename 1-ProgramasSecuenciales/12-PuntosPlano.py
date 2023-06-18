# 12. Pide al usuario dos pares de números x1,y1 y x2,y2, que representen dos puntos en el plano.
#    Calcula y muestra la distancia entre ellos.

# Este programa calcula la distancia entre dos puntos en el plano
# Author: Alejandro Priego Izquierdo
# Date: 1/10/2022

# Encabezado del ejercicio
print("")
print("Este programa calcula la distancia entre dos puntos en el plano.")
print("--------------------------------------------------------------")

# Pedimos 2 valores para cada uno de los pares
par1x = float(input("Indica la coordenada X del Primer Par: "))
par1y = float(input("Indica la coordenada Y del Segundo Par: "))
par2x = float(input("Indica la coordenada X del Primer Par: "))
par2y = float(input("Indica la coordenada Y del Segundo Par: "))

parx = abs(par1x - par2x)   # Calculamos distancia entre las X
pary = abs(par1y - par2y)   # Calculamos distancia entre las Y

print("La distancia entre estos puntos es de", parx, "en la coordenada X y de", pary, "en la coordenada Y")  # Imprimir
