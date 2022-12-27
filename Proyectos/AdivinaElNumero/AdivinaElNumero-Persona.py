import os


def main():
    global attemps
    input_game_number()

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


def input_game_number():
    global number
    number = int(input(f"Ingresa el número que debe adivinar el otro jugador (entre {MIN} y {MAX}): "))

    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


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
