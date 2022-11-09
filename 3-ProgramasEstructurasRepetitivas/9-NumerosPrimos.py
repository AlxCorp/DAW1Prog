# Escribe un programa que escriba los N primeros números primos.
# Author: Alejandro Priego Izquierdo
# Date: 31/10/2022

# Encabezado del ejercicio
print("")
print("Este programa imprimirá números primos")
print("--------------------------------------")

# Preguntamos las variables
quantity = 0
while quantity <= 0:
    quantity = int(input("Ingrese la cantidad de números primos a mostrar: "))
print()
print("Los primeros", quantity, "números primos son:")
print("El primo número 1 es: 2")  # Primer primo y único primo par

candidato_a_primo = 3  # Número posible que puede ser primo
total_primos_mostrados = 1  # Cuantos números hemos mostrado para parar el programa

while total_primos_mostrados < quantity:   # Mientras que no hayamos impreso la cantidad de primos pedida hacemos:
    # Vemos si el candidato es primo
    es_primo = True
    for divisor in range(3, int(candidato_a_primo ** 0.5) + 1, 2):  # Comprobamos solo hasta la raíz cuadrada
        if candidato_a_primo % divisor == 0:                        # del candidato, de dos en dos
            es_primo = False
            break

    # Si el candidato es primo lo muestro
    if es_primo:
        print(candidato_a_primo)
        total_primos_mostrados += 1

    candidato_a_primo += 2  # Siguiente candidato
