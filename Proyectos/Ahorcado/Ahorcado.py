from random import randrange as rng
from DrawAhorcado import dibujo_ahorcado

DICTIONARY = "Spanish.dic"
t = open(DICTIONARY, "r")
x = t.read().split("\n")


def game():
    word = x[rng(len(x))]
    splitted_word = []
    for i in word:
        splitted_word.append(i)

    respuestas = ["_" for _ in range(len(word))]
    ganada = False
    hints = 0

    print(word)

    while not ganada:
        dibujo_ahorcado(hints)
        print()
        print(respuestas)

        letter = input("Ingrese la siguiente letra: ")

        if letter not in splitted_word:
            hints += 1

        if hints > 5:
            print("Has pedido, la palabra correcta era", word)
            break

        while letter in splitted_word:
            respuestas[splitted_word.index(letter)] = letter
            splitted_word[splitted_word.index(letter)] = "7u7"

        if "_" not in respuestas:
            ganada = True
            print("\nEnhorabuena, has ganado")


if __name__ == '__main__':
    game()

    match input("Pulse ENTER para volver a jugar, escriba 'q' para terminar").lower():
        case "q":
            quit()
        case _:
            game()
