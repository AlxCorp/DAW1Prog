# 2. Calcular el perímetro y área de un rectángulo dada su base y su altura.

base = float(input("Indica la base: "))            # Preguntamos Base y Altura
altura = float(input("Indica la altura: "))

perimetro = 2 * base + 2 * altura                   # Guardamos las fórmulas en variables para usarlas más tarde
area = base * altura

print("El Perímetro del rectángulo es: ", perimetro, "Metros")      # Imprimimos el resultado de ambas operaciones
print("El Área del rectángulo es: ", area, "Metros Cuadrados")
