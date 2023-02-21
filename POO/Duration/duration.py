from typeguard import typechecked


@typechecked
class Duration:
    def __init__(self, h, m: int = 0, s: int = 0):
        self.__h, self.__m, self.__s = h, m, s
        self.__check_input()
        self.__chk_time()

    def __check_input(self):
        if not self.__m and not self.__s:
            temp = self.__h
            self.__h = 0
            self + temp

    def __chk_time(self):
        total = self.__s + self.__m * 60 + self.__h * 60 * 60
        self.__h, self.__m, self.__s = 0, 0, 0

        while total > 3600:
            self.__h += 1
            total -= 3600
        while total > 60:
            self.__m += 1
            total -= 60
        self.__s = total

    def __add__(self, other):
        self.__h += other.__h
        self.__m += other.__m
        self.__s += other.__s

    def __sub__(self, other):
        self.__h -= other.__h
        self.__m -= other.__m
        self.__s -= other.__s

    def add_time(self, h: int, m: int, s: int):
        self.__h += h
        self.__m += m
        self.__s += s

        self.__chk_time()

    def sub_time(self, h: int, m: int, s: int):
        self.__h -= h
        self.__m -= m
        self.__s -= s

        self.__chk_time()

    def __str__(self):
        return f'{self.__h}h {self.__m}m {self.__s}s'
