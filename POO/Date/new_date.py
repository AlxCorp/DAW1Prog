from typeguard import typechecked


@typechecked
class Date:
    def __init__(self, day, month: (bool, int) = False, year: (bool, int) = False):  # Uso true en vez de None para simplificar la siguiente línea.
        if isinstance(day, Date) and not month and not year:
            self.__day, self.__month, self.__year = day.__day, day.__month, day.__year
        elif isinstance(day, int) and isinstance(month, int) and isinstance(year, int):
            self.__check_date(day, month, year)
            self.__day, self.__month, self.__year = day, month, year
        else:
            raise TypeError("Parámetros incorrectos para construir una fecha")

    def __str__(self):
        return f'{self.day} de {self.__month_days(self.month, self.year)[0]} de {self.year}'

    @property
    def date(self):
        return f"{self.__year:04d}-{self.__month:02d}-{self.__day:02d}"

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, other: int):
        self.__check_date(other, self.month, self.year)
        self.__day = other

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, other: int):
        self.__check_date(self.day, other, self.year)
        self.__month = other

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, other: int):
        self.__check_date(self.day, self.month, other)
        self.__year = other

    def __check_date(self, day: int, month: int, year: int):
        if year < 1:
            raise ValueError("El año introducido no es válido")
        if month < 1 or month > 12:
            raise ValueError("El mes introducido no es válido")
        if day < 1 or day > self.__month_days(month, year)[1]:
            raise ValueError("El día introducido no es válido")

    def __month_days(self, month: int, year: int):
        months_days = {1: ("Enero", 31), 2: ("Febrero", 28), 3: ("Marzo", 31), 4: ("Abril", 30),
                       5: ("Mayo", 31),
                       6: ("Junio", 30), 7: ("Julio", 31), 8: ("Agosto", 31), 9: ("Septiembre", 30),
                       10: ("Octubre", 31), 11: ("Noviembre", 30), 12: ("Diciembre", 31)}

        if self.__is_leap_year(year):
            months_days[2] = ("Febrero", 29)

        return months_days[month]

    @property
    def day_of_week(self):
        first_date = Date(1, 1, 1)  # Fue lunes (o eso dicen)
        dia = (self - first_date) % 7
        return dia

    @property
    def leap(self):
        return self.__is_leap_year(self.year)

    @staticmethod
    def __is_leap_year(year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    def __add_year(self):
        self.__year += 1

    def __sub_year(self):
        if self.year > 1:
            self.__year -= 1
        else:
            raise ValueError("No se permiten años inferiores al año 1")

    def __add_month(self):
        if self.__month < 12:
            self.__month += 1
        elif self.__month == 12:
            self.__month = 1
            self.__add_year()

    def __sub_month(self):
        if self.__month > 1:
            self.__month -= 1
        elif self.__month == 1:
            self.__month = 12
            self.__sub_year()

    def __add_day(self):
        if self.__day < self.__month_days(self.month, self.year)[1]:
            self.__day += 1
        if self.__day == self.__month_days(self.month, self.year)[1]:
            self.__add_month()
            self.__day = self.__month_days(self.month, self.year)[1]

    def __sub_day(self):
        if self.__day > 1:
            self.__day -= 1
        elif self.__day == 1:
            self.__sub_month()
            self.__day = self.__month_days(self.month, self.year)[1]

    def __radd__(self, n: int):
        return self + n

    def __add__(self, other: int):
        for i in range(abs(other)):
            if other > 0:
                self.__add_day()
            if other < 0:
                self.__sub_day()

    def __sub__(self, other: (int, 'Date')):
        d1, d2, days = None, None, 0
        if isinstance(other, int):
            for i in range(other):
                self.__sub_day()
        if isinstance(other, Date):
            if self > other:
                d1, d2 = self, other
            if other > self:
                d1, d2 = other, self

            while d1 > d2:
                d2 + 1
                days += 1

            return days

    def __eq__(self, other: 'Date'):
        return (self.__day, self.__month, self.__year) == (other.__day, other.__month, other.__year)

    def __ne__(self, other: 'Date'):
        return not self == other

    def __gt__(self, other: 'Date'):
        return self.date > other.date

    def __ge__(self, other: 'Date'):
        return self > other or self == other

    def __lt__(self, other: 'Date'):
        return not self >= other

    def __le__(self, other):
        return not self > other


if __name__ == '__main__':
    f1 = Date(1, 10, 2020)  # almacena el 1 de Octubre de 2020
    f2 = Date(f1)  # almacena una copia de la fecha almacenada en f1

    print(f1.date)
    print(f1)
    print(f2.date)
    print(f2)
    f1 + 1990
    print(f1)
    print(f1 - f2)

    print(f1.day_of_week)

    f3 = Date(23, 2, 2023)
    print(f3.day_of_week)

    print("NO FUNCIONA EL OBTENER EL DIA DE LA SEMANA")
    print("NO FUNCIONA EL OBTENER EL DIA DE LA SEMANA")
    print("NO FUNCIONA EL OBTENER EL DIA DE LA SEMANA")
    print("NO FUNCIONA EL OBTENER EL DIA DE LA SEMANA")
