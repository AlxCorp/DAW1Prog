# Programa que calcule la potencia con la base y exponente indicados por el usuario.
# Author: Alejandro Priego Izquierdo
# Date: 19/10/2022

# Encabezado del ejercicio
print("")
print("Este programa calculará la potencia")
print("-----------------------------------")

# Preguntamos los números
base = input("Indica la base: ")
exp = input("Indica el exponente: ")

operation = pow(base, exp)  # Usamos la función pow para elevar

if exp > 0:
    print("La potencia de elevar", base, "a", exp, "es", operation)
elif exp == 0:
    print("La potencia de elevar", base, "a", exp, "es 1")
elif exp < 0:
    operation = 1 / abs(operation)  # Al ser negativo el exponente, se invierten el divisor y dividendo de la base
    print("La potencia de elevar", base, "a", exp, "es", operation)
else:
    print("Por favor, ingresa un valor válido")
