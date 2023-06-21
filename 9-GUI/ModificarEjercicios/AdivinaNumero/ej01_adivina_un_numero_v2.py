"""
Aplicación que permita adivinar un número.

La aplicación genera un número aleatorio del 1 al 100. A continuación va
pidiendo números y va respondiendo si el número a adivinar es mayor o
menor que el introducido, además de los intentos que te quedan
(tienes 10 intentos para acertarlo).

El programa termina cuando se acierta el número (además te dice en
cuantos intentos lo has acertado), si se llega al limite de intentos te
muestra el número que había generado.

Fecha: 11/11/2019.

Autores: Clase de 1ºDAW

Otra versión del programa anterior.
"""

import random

# Constantes
STARTING_NUMBER = 1
FINAL_NUMBER = 100
MAXIMUM_TRIES = 10


class AdivinaNumero:
    def __init__(self):
        # Inicializamos
        self._numero_a_adivinar = random.randint(STARTING_NUMBER, FINAL_NUMBER)
        self._remaining_hints = MAXIMUM_TRIES

    def input_number(self, number):
        inputted_number = int(number)

        if inputted_number != self._numero_a_adivinar and self._remaining_hints > 1:
            self._remaining_hints -= 1
            if inputted_number < self._numero_a_adivinar:
                return f"{inputted_number} es menor que el número a adivinar. Te quedan {self.remaining_hints} intentos."
            else:
                return f"{inputted_number} es mayor que el número a adivinar. Te quedan {self.remaining_hints} intentos."
        elif inputted_number == self._numero_a_adivinar:
            return f"Has adivinado el número en {MAXIMUM_TRIES - self._remaining_hints} intentos"
        else:
            return f"Has agotado el número máximo de intentos. El número a adivinar era {self._numero_a_adivinar}"

    @property
    def remaining_hints(self):
        return self._remaining_hints
