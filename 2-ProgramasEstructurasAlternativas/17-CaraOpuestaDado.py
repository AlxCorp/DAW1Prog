# Indicar cuál es la cara del dado opuesta a la introducida
# Author: Alejandro Priego Izquierdo
# Date: 23/10/2022

# Encabezado del ejercicio
print("")
print("Este programa determina cual es la cara del dado contraria")
print("----------------------------------------------------------")

# Preguntamos las variables
number = int(input("Ingrese el valor obtenido en el dado: "))

if number < 1 or number > 6:
    print("ERROR: número incorrecto")
    quit()

match number:
    case 1:
        print('En la cara opuesta se encuentra el número "seis"')
    case 2:
        print('En la cara opuesta se encuentra el número "cinco"')
    case 3:
        print('En la cara opuesta se encuentra el número "cuatro"')
    case 4:
        print('En la cara opuesta se encuentra el número "tres"')
    case 5:
        print('En la cara opuesta se encuentra el número "dos"')
    case 6:
        print('En la cara opuesta se encuentra el número "uno"')
