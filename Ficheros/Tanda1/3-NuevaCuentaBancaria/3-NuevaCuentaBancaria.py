"""
Modifica el ejercicio de POO que gestiona una cuenta bancaria con movimientos, de forma que añadas a la clase un método
para guardar todos los datos de la cuenta bancaria (número, saldo y movimientos) en un fichero elegido por el cliente,
y un nuevo constructor que reciba como parámetro un fichero como el anterior y cree el objeto con esos datos. Pruébalo
con un programa.

Author: Alejandro Priego Izquierdo
Date: 25/04/2023
"""
from typeguard import typechecked
from random import randrange as rng


@typechecked
class BankAccount:
    accounts = []

    def __init__(self, file):
        with open(file, mode="r") as f:
            lines = f.readlines()
        self.__account_number = int(lines[0])
        self.__balance = float(lines[1])

    @property
    def account_number(self):
        return self.__account_number

    @property
    def balance(self):
        return self.__balance

    def deposit(self, deposit):
        if deposit > 0:
            self.__balance += deposit
        else:
            # raise ValueError("No puedes hacer un ingreso negativo")
            raise NegativeIncomeNotAccepted()

    def withdraw(self, withdraw):
        if withdraw > 0:
            if withdraw > self.__balance:
                # raise ValueError("La cuenta no puede quedar en negativo")
                raise AccountCannotBeNegative()
            else:
                self.__balance += withdraw
        else:
            # raise ValueError("El número debe ser positivo")
            raise NumberMustBePositive()

    def transfer(self, account: 'BankAccount', amount: float):
        self.withdraw(amount)  # No verificar cantidad, al quitarlo ya da error si no tiene suficiente.
        account.deposit(amount)

    def __str__(self):
        return f'Número de cta: {self.__account_number} | Saldo: {self.balance:.2f} €'

    def save_to_file(self, filename: str):
        with open(filename, mode="w") as f:
            f.writelines((str(self.account_number), "\n", str(self.balance)))

class BalanceMustBeGreaterThanZero(Exception):
    def __init__(self, *args, **kwargs):
        pass


class NegativeIncomeNotAccepted(Exception):
    def __init__(self, *args, **kwargs):  # real signature unknown
        pass


class AccountCannotBeNegative(Exception):
    def __init__(self, *args, **kwargs):  # real signature unknown
        pass


class NumberMustBePositive(Exception):
    def __init__(self, *args, **kwargs):  # real signature unknown
        pass


if __name__ == '__main__':
    cuenta1 = BankAccount("patata1.txt")
    cuenta2 = BankAccount("patata2.txt")
    print(cuenta1)
    print(cuenta2)
    cuenta1.deposit(2000)
    cuenta2.withdraw(600)
    cuenta1.withdraw(55)
    print(cuenta1)
    print(cuenta2)
    cuenta1.save_to_file("patata3.txt")
