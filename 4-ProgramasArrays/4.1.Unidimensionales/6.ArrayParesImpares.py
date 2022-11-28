# Escribe un programa que genere 20 números enteros aleatorios entre 0 y 100 y que los almacene en un array. El
# programa debe ser capaz de pasar todos los números pares a las primeras posiciones del array (del 0 en adelante) y
# todos los números impares a las celdas restantes. Utiliza arrays auxiliares si es necesario.
# Author: Alejandro Priego Izquierdo
# Date: 20/11/2022
import random as rng

# Encabezado del ejercicio
print("")
print("Este programa ordena un array según pares e impares")
print("---------------------------------------------------")

nums = []
nums_par = []
nums_impar = []
for i in range(20):
    nums.append(rng.randrange(0, 100))

# Comprobar si es par o impar
for i in nums:
    if i % 2 == 0:
        nums_par.append(i)
    elif i % 2 != 0:
        nums_impar.append(i)

nums = []
nums.extend(nums_par)
nums.extend(nums_impar)

print()
print(nums)
