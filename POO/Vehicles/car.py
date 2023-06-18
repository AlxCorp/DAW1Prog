from typeguard import typechecked
from vehicle import Vehicle


@typechecked
class Car(Vehicle):
    def __init__(self):
        super().__init__()

    @staticmethod
    def burn_wheel():
        print("ō˞̶🏎")

