"""
EXAMEN PRÁCTICO 3 - PROGRAMACIÓN

Author: Alejandro Priego Izquierdo
Date: 08-03-2023
"""

from typeguard import typechecked
from datetime import datetime


@typechecked
class Movement:

    __last_number = 0

    def __init__(self, amount: float, concept: str, date_time: 'datetime'):
        self.__number: int = Movement.__last_number + 1
        Movement.__last_number += 1
        self.__amount = amount
        self.__concept = concept
        self.__date_time = date_time

    @property
    def number(self):
        return self.__number

    @property
    def amount(self):
        return self.__amount

    @property
    def concept(self):
        return self.__concept

    @property
    def date_time(self):
        return self.__date_time
