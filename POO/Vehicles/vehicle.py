from abc import ABC
from typeguard import typechecked


@typechecked
class Vehicle(ABC):
    __vehicles_created = 0
    __total_kilometers = 0

    def __init__(self):
        Vehicle.__vehicles_created += 1
        self.__kilometers_traveled = 0

    def travel(self, km: int):
        if km < 0:
            raise ValueError("No puedes recorrer kilómetros negativos.")
        self.__kilometers_traveled += km
        Vehicle.__total_kilometers += km

    @property
    def km_travelled(self):
        return self.__kilometers_traveled

    @classmethod
    def total_km(cls):
        return cls.__total_kilometers

    @classmethod
    def vehicles_created(cls):
        return cls.__vehicles_created

