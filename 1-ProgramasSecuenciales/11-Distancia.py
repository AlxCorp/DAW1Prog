# 11. Pide al usuario dos números y muestra la "distancia" entre ellos (el valor absoluto de su diferencia,
#  de modo que el resultado sea siempre positivo).

dis1 = float(input("Indica el primer número: "))       # Pedimos los dos números
dis2 = float(input("Indica el segundo número: "))

dist = abs(dis1 - dis2)     # Usamos la funcion abs para sacar el valor absoluto

print("La distancia entre estos dos números es de", dist, "metros")
