from typeguard import typechecked


@typechecked
class Terminal:
    __terminal_numbers = []

    def __init__(self, number: str):
        if self.__check_number(number):
            Terminal.__terminal_numbers.append(number)
            self.__number = number
        else:
            raise TypeError("El número del terminal no es correcto")

        self.__talk_time = 0

    @property
    def number(self):
        return self.__number

    @property
    def talk_time(self):
        return self.__talk_time

    @staticmethod
    def __check_number(number: str):
        return len(number) == 9 and number[0] in ('6', '7', '9') and number not in Terminal.__terminal_numbers

    @staticmethod
    def __check_time(time: int):
        return time > 0

    def call(self, other: 'Terminal', time: int):
        if self != other and self.__check_time(time):
            self.__talk_time += time
            other.__talk_time += time

    def __str__(self):
        return f'No. {self.number[0]+self.number[1]+self.number[2]} {self.number[3]+self.number[4]} ' \
               f'{self.number[5]+self.number[6]} {self.number[7]+self.number[8]} - {self.talk_time}s de conversación'


if __name__ == '__main__':
    t1 = Terminal("678112233")
    t2 = Terminal("644744469")
    t3 = Terminal("622328909")
    t4 = Terminal("664739818")
    print(t1)
    print(t2)
    t1.call(t2, 320)
    t1.call(t3, 200)
    print(t1)
    print(t2)
    print(t3)
    print(t4)