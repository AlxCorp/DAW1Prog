from typeguard import typechecked
from POO.Terminal.terminal import Terminal


@typechecked
class Mobile(Terminal):
    __rates = {"rata": 6, "mono": 12, "bisonte": 30}

    def __init__(self, number: str, rate: str):
        super().__init__(number)
        if self.__check_rate(rate):
            self.__rate = rate
        else:
            raise ValueError("Tarifa no encontrada")

        self.__total_billed = 0

    @staticmethod
    def __check_rate(rate):
        return rate in Mobile.__rates.keys()

    @property
    def rate(self):
        return self.__rate

    @rate.setter
    def rate(self, rate):
        if self.__check_rate(rate):
            self.__rate = rate
        else:
            raise ValueError("Tarifa no encontrada")

    @property
    def total_billed(self):
        return round(self.__total_billed, 2)

    def call(self, other: 'Terminal', time: int):
        if self != other and self.__check_time(time):
            self.__talk_time += time
            other.__talk_time += time

        self.__bill(time)

    def __bill(self, time: int):
        self.__total_billed += (Mobile.__rates[self.__rate]/60) * time

    def __str__(self):
        return f'No. {self.number[0]+self.number[1]+self.number[2]} {self.number[3]+self.number[4]} ' \
               f'{self.number[5]+self.number[6]} {self.number[7]+self.number[8]} - {self.talk_time}s de conversación ' \
               f'- tarificados {self.__total_billed} euros'


if __name__ == '__main__':
    m1 = Mobile("678112233", "rata")
    m2 = Mobile("644744469", "mono")
    m3 = Mobile("622328909", "bisonte")
    print(m1)
    print(m2)
    m1.call(m2, 320)
    m1.call(m3, 200)
    m2.call(m3, 550)
    print(m1)
    print(m2)
    print(m3)
