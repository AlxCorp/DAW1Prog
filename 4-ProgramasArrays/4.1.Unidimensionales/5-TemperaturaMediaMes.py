# Realiza un programa que pida la temperatura media que ha hecho en cada mes de un determinado año y que muestre a
# continuación un diagrama de barras horizontales con esos datos. Las barras del diagrama se pueden dibujar a base de
# asteriscos o cualquier otro carácter.
# Author: Alejandro Priego Izquierdo
# Date: 20/11/2022

# Encabezado del ejercicio
print("")
print("Este programa calcula las temperaturas en un año")
print("------------------------------------------------")

# Preguntamos las variables
temps = []
months = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre',
          'Noviembre', 'Diciembre']

for i in range(12):
    temps.append(float(input(f"Por favor, ingrese la temperatura de {months[i]}: ")))

print()
print("Las temperaturas medias del año son las siguientes: ")

for i in range(12):
    temp = "#" * round(temps[i])
    print(f"{months[i]:12} --> {temp}")
