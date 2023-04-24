"""19. Escribir un programa para calcular la nota final de un estudiante, considerando que:
    - cada respuesta correcta suma 5 puntos
    - cada respuesta incorrecta suma -1 puntos
    - cada respuesta en blanco suma 0 puntos.
Imprime la puntuación total obtenida por el estudiante y su nota normalizada entre 0 y 10.
¿Qué tendrías que hacer para facilitar que los puntos que suman los diferentes tipos de respuestas
puedan cambiar en el futuro?"""

valorCorrecta = int(input("Indica el valor de las respuestas correctas: "))  # Pedimos el valor de cada tipo de pregunta
valorBlanco = int(input("Indica el valor de las respuestas en blanco: "))
valorIncorrecta = int(input("Indica el valor de las respuestas incorrectas: "))

# Comprobamos que el valor de las preguntas incorrectas es negativo
if valorIncorrecta >= 0:
    print("ERROR: El valor de las respuestas incorrectas debe ser igual o inferior a 0")
    quit()

correctas = int(input("Indica el número de respuestas correctas: "))    # Preguntamos las preguntas contestadas
incorrectas = int(input("Indica el número de respuestas incorrectas: "))
blancas = int(input("Indica el número de respuestas en blanco: "))

preguntasTotal = correctas + incorrectas + blancas    # Sumamos el total de preguntas respondidas

# Asignamos a cada tipo de pregunta sus puntos correspondientes
correctas *= valorCorrecta
incorrectas *= valorIncorrecta
blancas *= valorBlanco

# Comprobamos que el valor de incorrectas es 0 o negativo
if incorrectas == 0:
    incorrectas = incorrectas
elif incorrectas <= 0:
    incorrectas = -incorrectas

puntosTotal = correctas + incorrectas + blancas  # Sumamos el total de puntos

resultado = round(puntosTotal * 10 / preguntasTotal, 3)  # Calculamos la nota sobre diez

print("El alumno ha tenido", preguntasTotal, "preguntas contestadas, con las cuales ha obtenido un total de",
      puntosTotal, "puntos que corresponden a un", resultado)   # Imprimimos el resultado
