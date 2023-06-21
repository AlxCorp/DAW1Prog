# Escribir un programa que calcule el desglose mínimo en billetes y monedas de una cantidad exacta de euros. Hay
# billetes de 500, 200, 100, 50, 20, 10 y 5 € y monedas de 2 y 1 €.
# Author: Alejandro Priego Izquierdo
# Date: 21/10/2022

def desglose_euros(input_):
    amount = input_
    b500 = amount // 500
    amount -= b500*500
    b200 = amount // 200
    amount -= b200*200
    b100 = amount // 100
    amount -= b100*100
    b50 = amount // 50
    amount -= b50*50
    b20 = amount // 20
    amount -= b20*20
    b10 = amount // 10
    amount -= b10*10
    b5 = amount // 5
    amount -= b5*5
    m2 = amount // 2
    amount -= m2*2
    m1 = amount // 1

    return tuple((b500, b200, b100, b50, b20, b10, b5, m2, m1))
