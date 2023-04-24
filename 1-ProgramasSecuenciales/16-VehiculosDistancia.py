# 16. Dos vehículos viajan a diferentes velocidades (v1 y v2) y están distanciados por una distancia d.
#  El que está detrás viaja a una velocidad mayor. Se pide hacer un algoritmo para ingresar la distancia entre
#  los dos vehículos (km) y sus respectivas velocidades (km/h) y con esto determinar y mostrar en que tiempo (minutos)
#  alcanzará el vehículo más rápido al otro.

v1 = int(input("Indica la velocidad del vehículo A: "))  # Preguntamos la velocidad a la que circulan ambos vehículos
v2 = int(input("Indica la velocidad del vehículo B: "))

# Comprobamos que el vehículo A circule a una mayor velocidad, ya que, de lo contrario,
# nunca sucedería el adelantamiento
if v1 < v2:
    print("ERROR: El vehículo A debe tener una velocidad mayor a la del vehículo B")
    quit()

dist = int(input("Indica la distancia en KM entre ambos vehículos: "))  # Preguntamos la distancia entre ambos vehículos

vt = v1-v2  # Calculamos la velocidad total
tiempoMin = int(round((dist/vt) * 60))  # Calculamos los minutos
tiempoSeg = int(round(((dist/vt) * 60 * 60) % 60, 2))     # Calculamos los segundos


print("El vehículo A tardará", tiempoMin, "Minutos y", tiempoSeg, "Segundos en adelantar al vehículo B")   # Imprimimos
