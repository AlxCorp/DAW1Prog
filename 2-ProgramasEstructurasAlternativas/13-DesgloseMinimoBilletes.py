# Escribir un programa que calcule el desglose mínimo en billetes y monedas de una cantidad exacta de euros. Hay
# billetes de 500, 200, 100, 50, 20, 10 y 5 € y monedas de 2 y 1 €.
# Author: Alejandro Priego Izquierdo
# Date: 21/10/2022

# Encabezado del ejercicio
print("")
print("Este programa determina el desglose mínimo de la cantidad introducida (No Céntimos)")
print("-----------------------------------------------------------------------------------")

# Preguntamos las variables
amount = int(input("Ingrese la cantidad: "))

b500 = amount // 500
amount -= b500*500
b200 = amount // 200
amount -= b200*200
b100 = amount // 100
amount -= b100*100
b50 = amount // 50
amount -= b50*50
b20 = amount // 20
amount -= b20*20
b10 = amount // 10
amount -= b10*10
b5 = amount // 5
amount -= b5*5
m2 = amount // 2
amount -= m2*2
m1 = amount // 1

print("El desglose es el siguiente:")
print(b500, "Billetes de 500€")
print(b200, "Billetes de 200€")
print(b100, "Billetes de 100€")
print(b50, "Billetes de 50€")
print(b20, "Billetes de 20€")
print(b10, "Billetes de 10€")
print(b5, "Billetes de 5€")
print(m2, "Monedas de 2€")
print(m1, "Monedas de 1€")

