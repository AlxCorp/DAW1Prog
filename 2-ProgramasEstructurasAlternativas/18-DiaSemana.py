# Indicar cuál es el día de la semana que corresponde al número introducido
# Author: Alejandro Priego Izquierdo
# Date: 23/10/2022

# Encabezado del ejercicio
print("")
print("Este programa indica el día de la semana correspondiente al número introducido")
print("------------------------------------------------------------------------------")

# Preguntamos las variables
day = int(input("Ingrese el día de la semana (1-7): "))

match day:
    case 1:
        print("El día", day, "corresponde al Lunes")
    case 2:
        print("El día", day, "corresponde al Martes")
    case 3:
        print("El día", day, "corresponde al Miércoles")
    case 4:
        print("El día", day, "corresponde al Jueves")
    case 5:
        print("El día", day, "corresponde al Viernes")
    case 6:
        print("El día", day, "corresponde al Sábado")
    case 7:
        print("El día", day, "corresponde al Domingo")
    case _:
        print('Ese día NO existe')
