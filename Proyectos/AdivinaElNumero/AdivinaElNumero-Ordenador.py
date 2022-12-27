from random import randrange as rng


def main():
    global attemps
    generate_random_number()

    print(f"Debes adivinar el número, este se comprende entre {MIN} y {MAX}")

    while attemps < MAX_ATTEMPS:
        if not check_num(number):
            print("ERROR: Número incorrecto, vuelve a probar")
            attemps += 1
        else:
            break

    if attemps == MAX_ATTEMPS:
        print("\nLo siento, has agotado todos tus intentos. El número correcto era el", number)
    elif attemps < MAX_ATTEMPS:
        print("\nEnhorabuena, has ganado. Has usado", attemps + 1, "intentos, el número correcto era el", number)


def generate_random_number():
    global number
    number = rng(MIN, MAX + 1)


def check_num(y):
    temp = int(input("Ingrese el número correcto: "))
    if temp == y:
        return True
    return False


if __name__ == '__main__':
    MIN = 0
    MAX = 10
    MAX_ATTEMPS = 10
    attemps = 0
    number = 0

    main()
