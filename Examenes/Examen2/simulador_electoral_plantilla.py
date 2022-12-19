"""
El Ministerio del Interior está preparando la infraestructura para las elecciones municipales de mayo de 2023 y ha
contactado con el IES Gran Capitán para que le hagamos un simulador de resultados electorales municipales, ya que
sospecha que alguno de sus sistemas ha podido ser atacado y no se acaba de fiar de la veracidad de los datos.

La ley electoral dice que para poder tener representación en un municipio hay que superar el 5% de los votos válidos y
el reparto de escaños se hace mediante la Ley D’Hont.

Con el propósito de testear mejor el programa se incluye una opción que carga los resultados electorales municipales de
Córdoba de 2019.

Author: Alejandro Priego Izquierdo
Date: 19/12/2022
"""
from utilities import menu

MIN_PERCENT_VOTES = 5

city = None
valid_votes = 0
seats = 0
votes_parties = []
activator_menu_functions_3_4 = False    # Nos permite saber si se han usado las opciones 1 y 2
final_array_for_option_4 = []   # Array bidi. en el que albergaremos los datos finales "Partido, Escaños, Votos, Resto"


def main():
    while True:
        option = menu("Simulador electoral municipal", "Cargar datos de las elecciones municipales de Córdoba de 2019",
                      "Introducir datos electorales", "Introducir partido y votos", "Ver simulación", "Finalizar")

        if option == 1:
            load_electoral_data_cordova()
        elif option == 2:
            input_electoral_data()
        elif option == 3:
            input_party_votes()
        elif option == 4:
            print_simulation()
        else:
            break
        print()

    print("¡Hasta la próxima! ;-)")


def load_electoral_data_cordova():
    global city, valid_votes, seats, votes_parties, activator_menu_functions_3_4
    city = "CÓRDOBA"
    valid_votes = 146548
    seats = 29
    votes_parties = [[43434, "PP"], [36169, "PSOE"], [22094, "Ciudadanos"], [15656, "IU ANDALUCÍA"],
                     [11788, "VOX"], [9144, "PODEMOS"], [1653, "PACMA"], [951, "ACCIÓN POR CÓRDOBA"],
                     [380, "PCTE"], [360, "ANDALUCÍA ENTRE TOD@S"], [320, "GANEMOS"], [320, "EB"],
                     [161, "PUM+J"]]
    print("Datos de Córdoba cargados.")

    activator_menu_functions_3_4 = True


def input_electoral_data():
    global city, valid_votes, seats, activator_menu_functions_3_4

    if confirm_delete_existing_data() == "abort":
        print("Abortando...")
        return

    city = input("Municipio: ")
    valid_votes = int(input("Votos válidos: "))
    seats = int(input("Número de Ediles: "))

    activator_menu_functions_3_4 = True


def confirm_delete_existing_data():
    global votes_parties, final_array_for_option_4, activator_menu_functions_3_4

    if not votes_parties == [] or city is not None:
        erase_confirm = input("Esto implica borrar los datos ya introducidos. Responda 'Sí' para proceder: ").upper()
        if erase_confirm != "SÍ":
            return "abort"
        elif erase_confirm == "SÍ":
            votes_parties = []
            final_array_for_option_4 = []
            activator_menu_functions_3_4 = False
            return "continue"


def input_party_votes():
    global votes_parties

    if check_activated_functions() == "error_no_activated":
        print("Error: Antes de usar esta opción debes usar la '1' o la '2'")
        return

    party = input("Partido Político: ").upper()

    # Comprobamos nombre de partido existente
    for p in votes_parties:
        if p[1] == party:
            print("ERROR: Este partido ya está registrado")
            return "error_partido_registrado"

    party_votes = int(input("Número de votos obtenido: "))

    # Comprobamos que no exceda el número de votos válidos
    if check_votes_count_validation(party_votes) == "exceed_votes_error":
        print("ERROR: Con ese número de votos se supera el total de votos emitidos")
        return "exceed_votes_error"

    votes_parties.append([party_votes, party])


# Sumamos los votos de la entrada con los votos que ya hay registrados, y lo comparamos con los votos permitidos
def check_votes_count_validation(party_votes):
    global valid_votes
    sum_other_parties_votes = 0

    for n in votes_parties:
        sum_other_parties_votes += n[0]

    if (sum_other_parties_votes + party_votes) > valid_votes:
        return "exceed_votes_error"
    return "valid_votes"


def print_simulation():
    global final_array_for_option_4

    if check_activated_functions() == "error_no_activated":
        print("Error: Antes de usar esta opción debes usar la '1' o la '2'")
        return

    create_final_array_for_print()  # Creamos el array del cual sacaremos la simulación
    seats_with_dhont()  # Usamos D'Hont sobre el array anterior para el reparto de ediles

    print(f"{'REPARTO DE VOTOS EN ' + str(city):^54}")
    print("-" * 54)
    print(f'{"PARTIDO":^25}   {"EDILES":^6}   {"VOTOS":^7}   {" %":>7}\n')
    for n in final_array_for_option_4:
        porcentaje = (n[2] * 100) / valid_votes
        print(f'{n[0]:^25}   {n[1]:^6}   {n[2]:^7}   {str(round(porcentaje, 2)) + " %":>7}')


def create_final_array_for_print():
    global final_array_for_option_4, votes_parties

    final_array_for_option_4 = [[] * 5 for _ in range(len(votes_parties))]

    for n in range(len(votes_parties)):
        final_array_for_option_4[n].append(votes_parties[n][1])    # Partido
        final_array_for_option_4[n].append(0)   # Escaños
        final_array_for_option_4[n].append(votes_parties[n][0])    # Votos
        final_array_for_option_4[n].append(votes_parties[n][0])    # Resto


def seats_with_dhont():
    global final_array_for_option_4, seats
    iterator = seats    # En caso de que un partido no llegue al MIN_PERCENT_VOTES, se agrega una iteración más

    for i in range(iterator):
        max_rest = []
        for n in final_array_for_option_4:
            max_rest.append(n[3])

        max_index = max_rest.index(max(max_rest))

        porcentaje = (final_array_for_option_4[max_index][2] * 100) / valid_votes
        if porcentaje <= MIN_PERCENT_VOTES:
            iterator += 1
            break

        final_array_for_option_4[max_index][1] += 1
        final_array_for_option_4[max_index][3] = \
            final_array_for_option_4[max_index][2] / (1 + final_array_for_option_4[max_index][1])

    # En caso de coincidir el número de ediles, se ordena por número de votos
    def sort_key(item):
        return item[1], item[2]

    # final_array_for_option_4.sort(key=lambda x: x[1], reverse=True)
    final_array_for_option_4.sort(key=sort_key, reverse=True)


def check_activated_functions():
    if not activator_menu_functions_3_4:
        return "error_no_activated"
    elif activator_menu_functions_3_4:
        return "menu_activated"


if __name__ == "__main__":
    main()
