"""
10. Un alumno desea saber cuál será su calificación final en la materia de Algoritmos. Dicha calificación se
    compone de los siguientes porcentajes:

* 55% del promedio de sus tres calificaciones parciales.
* 30% de la calificación del examen final.
* 15% de la calificación de un trabajo final.
"""

parcial1 = float(input("Indica la nota de tu primer parcial: "))    # Ingresamos todas las notas
parcial2 = float(input("Indica la nota de tu segundo parcial: "))
parcial3 = float(input("Indica la nota de tu tercer parcial: "))
examenFinal = float(input("Indica la nota de tu examen final: "))
trabajoFinal = float(input("Indica la nota de tu trabajo final: "))

parciales = round((parcial1 + parcial2 + parcial3)*0.55, 2)     # Realizamos la media de los 3 parciales
examen = round(examenFinal*0.3, 2)                              # Asignamos a cada nota su valor correspondiente
trabajo = round(trabajoFinal*0.15, 2)

notaFinal = parciales + examen + trabajo            # Sumamos los valores

print("Tu nota final en Algoritmos es un", notaFinal)   # Imprimimos el resultado
