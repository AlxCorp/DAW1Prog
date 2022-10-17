# Programa que pida dos números e indique si el primero es mayor que el segundo o no.
# Author: Alejandro Priego Izquierdo
# Date: 14/10/2022

# Encabezado del ejercicio
print("")
print("Este programa comparará dos números e indicará cual es el mayor de los dos.")
print("---------------------------------------------------------------------------")

# Preguntamos ambos números
a = float(input("Indica el valor del primer número: "))
b = float(input("Indica el valor del segundo número: "))

# Comprobamos todos los valores posibles e imprimimos los resultados
if a > b:
    print("El primer número,", a, "es MAYOR que el segundo,", b)
elif a < b:     # Con elif evitamos usar else + if, así como continuas identaciones
    print("El segundo número,", b, "es MAYOR que el primero,", a)
elif a == b:
    print("El primer y el segundo número son idénticos")
else:
    print("Por favor, introduce un valor de tipo numérico, asegúrate que colocas un '.' como separador decimal")
