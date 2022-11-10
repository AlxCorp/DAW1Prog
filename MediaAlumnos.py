# Este programa calcula la edad Desviación Típica de varios alumnos
# Author: Alejandro Priego Izquierdo
# Date: 03/11/2022

# Encabezado del ejercicio
print("")
print("Este programa calcula la edad Desviación Típica")
print("----------------------------------------------")

# Preguntamos las variables
num_alumnos = int(input("Ingrese la cantidad de alumnos: "))
suma_edades = []
media = 0
desviacion_tipica = 0

# Preguntar edades y guardarlas en Array
for i in range(1, num_alumnos + 1):
    temp = int(input(f"Ingrese la edad del alumno número {i}: "))
    suma_edades.append(int(temp))

# Calcular Media "normal"
for k in suma_edades:
    media += k

media /= num_alumnos

# Calcular Media Cuadrática
for n in suma_edades:
    desviacion_tipica += pow(n - media, 2)

desviacion_tipica /= num_alumnos
desviacion_tipica = desviacion_tipica * 1 / 2

print("La Desviación Típica es de", desviacion_tipica)
