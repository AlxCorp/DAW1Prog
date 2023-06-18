"""
Crea el iterador PrimeIterator que permita iterar sobre la lista de números primos, desde 2 hasta uno dado como máximo.

Ejemplo: "primes = list(PrimeIterator(15)) devolverá [2, 3, 5, 7, 11, 13]
"""


class PrimeIterator:
    def __init__(self, max_num):
        self.__max_num = max_num

    def __iter__(self):
        current = 2
        while current <= self.__max_num:
            if self.is_prime(current):
                yield current
            current += 1

    @staticmethod
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True


if __name__ == '__main__':
    primes = PrimeIterator(15)
    for n in primes:
        print(n)
    print(list(primes))
