from typeguard import typechecked


@typechecked
class Date:
    def __init__(self, day, month=False, year=False):  # Uso false en vez de None para simplificar la siguiente línea.
        if isinstance(day, Date) and not month and not year:
            self.__day, self.__month, self.__year = day.__day, day.__month, day.__year
        elif isinstance(day, int) and isinstance(month, int) and isinstance(year, int):
            self.__check_date(day, month, year)
            self.__day, self.__month, self.__year = day, month, year
        else:
            raise TypeError("Parámetros incorrectos para construir una fecha")

    @property
    def date(self):
        return f"{self.__year:04d}-{self.__month:02d}-{self.__day:02d}"

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, value: int):
        self.__check_date(value, self.month, self.year)
        self.__day = value
        self.__adjust_date()

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, value: int):
        self.__check_date(self.day, value, self.year)
        self.__month = value
        self.__adjust_date()

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value: int):
        self.__check_date(self.day, self.month, value)
        self.__year = value
        self.__adjust_date()

    def __check_date(self, day: int, month: int, year: int):
        if year < 1:
            raise ValueError("El año introducido no es válido")
        if month > 12 or month < 1:
            raise ValueError("El mes introducido no es válido")
        if month in (1, 3, 5, 7, 8, 10, 12) and day > 31 or day < 1:
            raise ValueError("El día introducido no es válido")
        if month in (4, 6, 9, 11) and day > 30 or day < 1:
            raise ValueError("El día introducido no es válido")
        if (month == 2 and self.__is_leap_year(year) and day > 29) or (
                month == 2 and not self.__is_leap_year(year) and day > 28) or day < 1:
            raise ValueError("El día introducido no es válido")

    @property
    def leap(self):
        return self.__is_leap_year(self.year)

    @staticmethod
    def __is_leap_year(year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    def __adjust_date(self):
        do_anything = False

        if self.month == 2 and self.__is_leap_year(self.year) and self.day > 29:
            self.day -= 29
            self.month += 1
            do_anything = True
        if self.month == 2 and not self.__is_leap_year(self.year) and self.day > 28:
            self.day -= 28
            self.month += 1
            do_anything = True
        if self.month in (4, 6, 9, 11) and self.day > 30:
            self.day -= 30
            self.month += 1
            do_anything = True
        if self.month in (1, 3, 5, 7, 8, 10, 12) and self.day > 31:
            self.day -= 31
            self.month += 1
            do_anything = True
        if self.month > 12:
            self.month -= 12
            self.year += 1
            do_anything = True
        if self.day == 0:
            match self.month:
                case 1:
                    self.day += 31
                    self.year -= 1
                case 2, 4, 6, 9, 11:
                    self.day += 31
                case 3:
                    if self.leap:
                        self.day += 29
                    else:
                        self.day += 28
                case 5, 7, 8, 10, 12:
                    self.day += 30

            self.month -= 1

        if do_anything:
            self.__adjust_date()

    def __month_days(self, month: int, year: int):
        months_days = {1: ("Enero", 31), 2: ("Febrero", 28), 3: ("Marzo", 31), 4: ("Abril", 30), 5: ("Mayo", 31),
                       6: ("Junio", 30), 7: ("Julio", 31), 8: ("Agosto", 31), 9: ("Septiembre", 30),
                       10: ("Octubre", 31), 11: ("Noviembre", 30), 12: ("Diciembre", 31)}

        if self.__is_leap_year(year):
            months_days[2] = ("Febrero", 29)

        return months_days[month]

    def sub_date(self, other: 'Date'):
        if self < other:
            dt1, dt2 = self, other
            sign = -1
        else:
            dt1, dt2 = other, self
            sign = 1
        days = 0
        while dt1 < dt2:
            dt1 += 1
            days += 1
        return sign * days

    def __add__(self, other: int):
        self.day += other

    def __radd__(self, n: int):
        return self + n

    def __sub__(self, other: (int, 'Date')):
        if isinstance(other, Date):
            self.sub_date(other)
        else:
            self.day -= other

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
    date1 = Date(5, 3, 2023)
    date2 = Date(2, 1, 2023)

    date2.sub_date(date1)