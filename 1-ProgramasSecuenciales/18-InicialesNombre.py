#  18. Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.

Nom = input("Indica tu Nombre: ")   # Preguntamos las diferentes variables
Ap1 = input("Indica tu Primer Apellido: ")
Ap2 = input("Indica tu Segundo Apellido: ")

Nom = Nom[0]    # Seleccionamos la posición 0 (1.er caracter) de cada una de las cadenas
Ap1 = Ap1[0]
Ap2 = Ap2[0]

Iniciales = Nom + Ap1 + Ap2     # Concatenamos todas las cadenas

# Imprimimos las iniciales con el método Upper para ponerlas en Mayúscula
print("Tus iniciales son", Iniciales.upper())
