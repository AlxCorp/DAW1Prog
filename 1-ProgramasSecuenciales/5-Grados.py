# 5. Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius.

grad1 = float(input("Indica la temperatura en grados Fahrenheit: "))    # Preguntamos la temperatura a convertir

cel = (grad1 * 9/5) + 32    # Formula conversión

print(grad1, "Grados Fahrenheit equivalen a", cel, "Grados Celcius")    # Imprimimos la solución
