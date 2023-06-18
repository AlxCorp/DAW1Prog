# Programa que pida dos números ‘nota’ y ‘edad’ y un carácter ‘sexo’ y muestre el mensaje ‘ACEPTADA’ si la nota es
# mayor o igual a cinco, la edad es mayor o igual a dieciocho y el sexo es ‘F’. En caso de que se cumpla lo mismo,
# pero el sexo sea ‘M’, debe imprimir ‘POSIBLE’. Si no se cumplen dichas condiciones se debe mostrar ‘NO ACEPTADA’.
# Author: Alejandro Priego Izquierdo
# Date: 19/10/2022

# Encabezado del ejercicio
print("")
print("Este programa indicará si es apto o no")
print("--------------------------------------")

# Preguntamos los números
note = float(input("Indica tu nota: "))
age = int(input("Indica tu edad: "))
sex = input("Indica si tu sexo es Masculino(M) o Femenino(F): ")

sex = sex.upper()[0]    # Primera letra solo por si se introduce palabra entera

if note >= 5 and age >= 18 and sex == "F":  # Comprobamos nota, edad y sexo
    print("ACEPTADA")
elif note >= 5 and age >= 18 and sex == "M":
    print("POSIBLE")
else:
    print("NO ACEPTADA")
