from POO.Menu.menu import Menu
from vehicle import Vehicle
from bike import Bike
from car import Car
import random as rng

MIN_TRAVEL_BIKE = 10
MAX_TRAVEL_BIKE = 50
MIN_TRAVEL_CAR = 50
MAX_TRAVEL_CAR = 500

bike = Bike()
car = Car()


def main():
    options = ("Anda con la bicicleta", "Haz el caballito con la bicicleta", "Anda con el coche",
               "Quema rueda con el coche", "Ver kilometraje de la bicicleta", "Ver kilometraje del coche",
               "Ver kilometraje total")
    m = Menu("Vehículos", options)

    while True:
        match(m.print_menu()):
            case 1: travel_with_bike()
            case 2: bike.wheelie()
            case 3: travel_with_car()
            case 4: car.burn_wheel()
            case 5: show_bike_mileage()
            case 6: show_car_mileage()
            case 7: show_total_mileage()


def travel_with_bike():
    km = rng.randint(MIN_TRAVEL_BIKE, MAX_TRAVEL_BIKE)
    bike.travel(km)
    print("La bicicleta recorre", km, "kms.\n")


def travel_with_car():
    km = rng.randint(MIN_TRAVEL_CAR, MAX_TRAVEL_CAR)
    car.travel(km)
    print("El coche recorre", km, "kms.\n")


def show_bike_mileage():
    print("El kilometraje de la bicicleta es de", bike.km_travelled, "kms.\n")


def show_car_mileage():
    print("El kilometraje del coche es de", car.km_travelled, "kms.\n")


def show_total_mileage():
    print("El kilometraje TOTAL es de", Vehicle.total_km(), "kms.\n")


if __name__ == '__main__':
    main()
