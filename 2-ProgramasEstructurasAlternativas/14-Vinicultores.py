# Se requiere determinar cuánto recibirá un productor por la uva que entrega en un embarque
# Author: Alejandro Priego Izquierdo
# Date: 21/10/2022

# Encabezado del ejercicio
print("")
print("Este programa determina las ganancias del productor por la UVA")
print("--------------------------------------------------------------")

# Preguntamos las variables y comprobar entrada de datos
grapeType = input("Ingrese el tipo de la uva(A o B): ").upper()


if grapeType != "A" and grapeType != "B" or len(grapeType) != 1:
    print("Debes ingresar solamente A o B")
    quit()

grapeSize = int(input("Ingrese el tamaño de la uva(1 o 2): "))
if grapeSize != 1 and grapeSize != 2:
    print("Debes ingresar solamente 1 o 2")
    quit()

grapePrice = float(input("Ingrese del precio de la uva (Euros): "))
grapeAmount = float(input("Ingrese la cantidad de uva (Kg): "))


if grapeType == "A":
    if grapeSize == 1:
        grapePrice += 20
    else:
        grapePrice += 30
else:
    if grapeSize == 1:
        grapePrice -= 30
    else:
        grapePrice += 50


total = grapeAmount * grapePrice

euros = int(total // 100)
total -= euros * 100
cents = int(total)

print("El vinicultor ganará", euros, "Euros y", cents, "céntimos por", grapeAmount,
      "Kilos de uva tipo", grapeType, "y tamaño número", grapeSize)
