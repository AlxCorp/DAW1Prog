# Haz un programa que muestre un menú y, usando las funciones anteriores, ejecute las siguiente opciones:
# Author: Alejandro Priego Izquierdo
# Date: 18/12/2022

from Ejercicio1.Modificacion3Menu import menu
import Util.Statistics as St
import BibliotecaFunciones as Bf
import random as rng

opciones = ["Muestra los números primos que hay entre 1 y 1000",
            "Muestra los números capicúa que hay entre 1 y 99999",
            "Muestra la moda de 50 números enteros aleatorios entre 1 y 10",
            "Muestra la mediana de 10 números enteros aleatorios entre 1 y 50",
            "Muestra el máximo y mínimo de 1000 números enteros aleatorios entre 1 y 50000",
            "Muestra la varianza de 10 números enteros aleatorios entre 1 y 5",
            "Salir"]


def main():
    while True:
        match menu(opciones):
            case 0:
                imprimir_primos_entre_1_1000()
            case 1:
                imprimir_capicuas_entre_1_1000()
            case 2:
                imprimir_moda_50_nums_entre_1_10()
            case 3:
                imprimir_mediana_10_nums_entre_1_50()
            case 4:
                imprimir_max_min_1000_nums_entre_1_50000()
            case 5:
                imprimir_varianza_10_nums_entre_1_5()
            case 6:
                quit()
            case _:
                pass
        print()


def imprimir_primos_entre_1_1000():
    for i in range(2, 1001):
        if Bf.es_primo(i):
            print(i)


def imprimir_capicuas_entre_1_1000():
    for i in range(1, 100000):
        if Bf.es_capicua(i):
            print(i)


def imprimir_moda_50_nums_entre_1_10():
    nums = []
    for i in range(50):
        nums.append(rng.randrange(1, 10))
    print(St.mode(nums))


def imprimir_mediana_10_nums_entre_1_50():
    nums = []
    for i in range(10):
        nums.append(rng.randrange(1, 50))
    print(St.median(nums))


def imprimir_max_min_1000_nums_entre_1_50000():
    nums = []
    for i in range(1000):
        nums.append(rng.randrange(1, 50000))
    print(St.maximum(nums))
    print(St.minimum(nums))


def imprimir_varianza_10_nums_entre_1_5():
    nums = []
    for i in range(10):
        nums.append(rng.randrange(1, 5))
    print(St.variance(nums))


if __name__ == "__main__":
    main()
