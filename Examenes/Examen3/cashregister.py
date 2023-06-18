"""
EXAMEN PRÁCTICO 3 - PROGRAMACIÓN

Author: Alejandro Priego Izquierdo
Date: 08-03-2023
"""

from typeguard import typechecked
from datetime import datetime  # , timedelta
# from dateutil.relativedelta import relativedelta
from movement import Movement

# datetime.strptime(input("Ingrese una fecha en formato (dd/mm/aaaa): "), "%d/%m/%Y").date()
# strformat


@typechecked
class CashRegister:
    def __init__(self):
        self.__movements = []
        self.__balance = 0

    def add(self, amount: float, concept: str, date_time: ('datetime', str) = "Null"):
        if date_time == "Null":
            date_time = datetime.now()
        elif isinstance(date_time, datetime):
            pass
        else:
            assert ValueError("Fecha no válida!")

        if amount < 0 and abs(amount) > self.__balance:
            raise ValueError("Cantidad a sacar mayor al saldo de la caja!")
        if self.__movements:
            if date_time <= self.__movements[-1].date_time:
                raise ValueError("Fecha anterior o igual a la del último movimiento!")
        self.__movements.append(Movement(amount, concept, date_time))

        if amount > 0:
            self.__balance += amount
        elif amount < 0:
            self.__balance -= amount
        elif amount == 0:
            self.__balance += amount
        else:
            raise TypeError("Parámetros introducidos no válidos!")

    def delete_last(self):
        if self.__movements:
            self.__balance -= self.__movements[-1].amount
            return self.__movements.pop(-1)
        raise TypeError("No existen movimientos en la caja! :(")

    def __str__(self):
        string = f''

        for i in self.__movements:
            beauty_date_time = self.__beauty_date_time(i.date_time)
            string += f'{i.number:3d}. {beauty_date_time} | {i.concept} --> {i.amount} \n'

        string += f'\n\n Total de la Caja: {round(self.__balance, 2)} €'

        return string

    @property
    def balance(self):
        return self.__balance

    @staticmethod
    def __beauty_date_time(dt: 'datetime'):
        return f'{dt.day}/{dt.month}/{dt.year} - {dt.hour}:{dt.minute}:{dt.second}'
