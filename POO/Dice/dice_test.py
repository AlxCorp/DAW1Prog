from dice import Dice

NUMERO_DADOS = 5
NUMERO_TIRADAS = 6

dados = [Dice()] * NUMERO_DADOS

for n in range(NUMERO_TIRADAS):
    for dado in dados:
        dado.roll()
        print(dado.__str__())
    print()
    print("------------------")
    print()
