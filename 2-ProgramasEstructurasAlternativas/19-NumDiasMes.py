# Indicar cuantos días tiene el mes introducido.
# Author: Alejandro Priego Izquierdo
# Date: 23/10/2022

# Encabezado del ejercicio
print("")
print("Este programa indica los días correspondientes al número de mes introducido")
print("---------------------------------------------------------------------------")

# Preguntamos las variables
month = int(input("Ingrese el mes (1-12): "))

match month:
    case 1:
        print("Enero tiene 31 días")
    case 2:
        print("Febrero tiene 28 o 29 días")
    case 3:
        print("Marzo tiene 31 días")
    case 4:
        print("Abril tiene 30 días")
    case 5:
        print("Mayo tiene 31 días")
    case 6:
        print("Junio tiene 30 días")
    case 7:
        print("Julio tiene 31 días")
    case 8:
        print("Agosto tiene 31 días")
    case 9:
        print("Septiembre tiene 30 días")
    case 10:
        print("Octubre tiene 31 días")
    case 11:
        print("Noviembre tiene 30 días")
    case 12:
        print("Diciembre tiene 31 días")
    case _:
        print('Ese día NO existe')
