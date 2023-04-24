# 15. Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar un algoritmo que intercambie
#  los valores de ambas variables y muestre cuanto valen al final las dos variables.

A = input("Indica el valor de A: ")     # Preguntamos el valor de las dos variables
B = input("Indica el valor de B: ")
C = None       # Declaramos una variable vacía para realizar el intercambio de valores

C = A   # Realizamos los diferentes intercambios de valores entre las variables
A = B
B = C

print("El valor de A es", A, "y el de B es", B)  # Imprimimos el resultado
