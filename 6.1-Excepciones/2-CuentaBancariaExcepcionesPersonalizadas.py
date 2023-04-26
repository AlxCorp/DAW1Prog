from typeguard import typechecked
from random import randrange as rng


@typechecked
class BankAccount:
    accounts = []

    def __init__(self, balance: float = 0):
        if balance < 0:
            # raise ValueError("La cuenta debe tener un saldo igual o superior a 0")
            raise BalanceMustBeGreaterThanZero()
        while True:
            self.__account_number = rng(0000000000, 9999999999)
            if self.__account_number not in BankAccount.accounts:
                BankAccount.accounts.append(self.__account_number)
                break

        self.__balance = balance

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
    cuenta1 = BankAccount()
    cuenta2 = BankAccount(1500)
    cuenta3 = BankAccount(6000)
    print(cuenta1)
    print(cuenta2)
    print(cuenta3)
    cuenta1.deposit(2000)
    cuenta2.withdraw(600)
    cuenta3.deposit(75)
    cuenta1.withdraw(55)
    cuenta2.transfer(cuenta3, 100)
    print(cuenta1)
    print(cuenta2)
    print(cuenta3)
