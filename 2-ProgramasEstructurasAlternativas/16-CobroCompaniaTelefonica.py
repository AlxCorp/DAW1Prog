# Política de cobro de una compañía telefónica
# Author: Alejandro Priego Izquierdo
# Date: 21/10/2022

# Encabezado del ejercicio
print("")
print("Este programa determina cuanto cobrar a los clientes de una compañía telefónica")
print("-------------------------------------------------------------------------------")

# Preguntamos las variables
callTime = int(input("Ingrese el tiempo de la llamada (Minutos): "))
day = input("Indica el día de la semana (L, M, X, J, V, S, D): ").upper()
dayTime = input("Indica si la llamada se ha efectuado en turno de mañana (M) o tarde (T): ").upper()

weeksDays = "LMXJVSD"
brutePrice = None
total = None
TAX = None

COST5 = 100
COST5_3 = 80
COST5_3_2 = 70
COST10 = 50

# Comprobar día para aplicar "impuesto"
if day in weeksDays:
    match day:
        case "D":
            TAX = 3
        case other:
            match dayTime:
                case "M":
                    TAX = 15
                case "T":
                    TAX = 10
else:
    print("Por favor, ingresa un valor válido")
    quit()

if callTime <= 5:
    brutePrice = callTime * COST5
elif 5 < callTime <= 8:
    brutePrice = 5 * COST5 + ((callTime - 5) * COST5_3)
elif 8 < callTime <= 10:
    brutePrice = 5 * COST5 + 3 * COST5_3 + ((callTime - 8) * COST5_3_2)
elif 10 < callTime:
    brutePrice = 5 * COST5 + 3 * COST5_3 + 2 * COST5_3_2 + ((callTime - 10) * COST10)
else:
    print("Por favor, ingresa un valor válido")
    quit()

price = brutePrice * (TAX / 100)

print("El importe total de la llamada será de", price, "Euros para un total de", callTime, "Minutos, realizada el",
      day, "en horario de", dayTime)
