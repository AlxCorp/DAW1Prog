# 14. Dado un número de dos cifras, diseñe un programa que permita obtener el número invertido.

numero = input("Indica un número de dos cifras: ")  # Pedimos numero de dos cifras

if len(numero) == 2:        # Comprobamos que la longitud del número sea de 2 dígitos
    print(numero[1] + numero[0])    # Imprimimos primero el segundo caracter y luego el primero
    quit()      # Finalizamos el programa

print("El número indicado debe tener 2 cifras!!")   # Imprimimos el resultado
