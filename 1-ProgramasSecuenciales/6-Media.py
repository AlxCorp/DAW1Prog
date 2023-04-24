# 6. Calcular la media de tres números pedidos por teclado.

num1 = float(input("Indica el primer número: "))    # Pedimos los 3 números
num2 = float(input("Indica el segundo número: "))
num3 = float(input("Indica el tercer número: "))

media = round((num1 + num2 + num3)/3, 4)    # Hacemos el cálculo de la media

print("La media de estos números es: ", media)  # Imprimimos el resultado
