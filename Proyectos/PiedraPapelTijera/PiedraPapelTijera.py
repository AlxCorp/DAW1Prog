from random import choice as rng


def main():
    print_header()

    while True:
        jugar_ordenador()
        jugar_persona()

        juego()
        if resultado_juego == "empate":
            marcador[2] += 1
        elif resultado_juego == "win":
            marcador[0] += 1
        elif resultado_juego == "lost":
            marcador[1] += 1

        imprimir_marcador()


def print_header():
    print()
    print("""\
8888888b.  d8b               888                      8888888b.                            888      88888888888 d8b  d8b                          
888   Y88b Y8P               888                      888   Y88b                           888          888     Y8P  Y8P                          
888    888                   888                      888    888                           888          888                                       
888   d88P 888  .d88b.   .d88888 888d888 8888b.       888   d88P 8888b.  88888b.   .d88b.  888          888     888 8888  .d88b.  888d888 8888b.  
8888888P"  888 d8P  Y8b d88" 888 888P"      "88b      8888888P"     "88b 888 "88b d8P  Y8b 888          888     888 "888 d8P  Y8b 888P"      "88b 
888        888 88888888 888  888 888    .d888888      888       .d888888 888  888 88888888 888          888     888  888 88888888 888    .d888888 
888        888 Y8b.     Y88b 888 888    888  888      888       888  888 888 d88P Y8b.     888          888     888  888 Y8b.     888    888  888 
888        888  "Y8888   "Y88888 888    "Y888888      888       "Y888888 88888P"   "Y8888  888          888     888  888  "Y8888  888    "Y888888 
                                                                         888                                         888                          
                                                                         888                                        d88P                          
                                                                         888                                      888P"                                                                                                                                                                                                                
    """)
    print()


def jugar_ordenador():
    global jugada_os

    jugada_os = rng(opciones)


def jugar_persona():
    global jugada_persona

    while True:
        seleccion = int(input(f"Introduce tu jugada (1. {opciones[0]}, 2. {opciones[1]}, 3. {opciones[2]}): "))

        if seleccion == 1 or seleccion == 2 or seleccion == 3:
            break

    jugada_persona = opciones[seleccion - 1]


def juego():
    global marcador, resultado_juego
    marcador[3] += 1

    if jugada_persona == jugada_os:
        print("\nHABÉIS EMPATADO")
        resultado_juego = "empate"
        return "empate"
    if (jugada_persona == "Piedra" and jugada_os == "Tijera") or (jugada_persona == "Papel" and jugada_os == "Piedra") \
            or (jugada_persona == "Tijera" and jugada_os == "Papel"):
        print("\nHAS GANADO")
        resultado_juego = "win"
        return "win"
    print("\nHAS PERDIDO")
    resultado_juego = "lost"
    return "lost"


def imprimir_marcador():
    print()
    print(f"{'El resultado actual es el siguiente':^23}")
    print("-" * 23)
    print(f"Ganadas: {marcador[0]}")
    print(f"Perdidas: {marcador[1]}")
    print(f"Empatadas: {marcador[2]}")
    print()
    print(f"Has jugado {marcador[2]} veces", end="\n\n\n")


if __name__ == '__main__':
    opciones = ["Piedra", "Papel", "Tijera"]
    jugada_os = ""
    jugada_persona = ""
    resultado_juego = ""
    marcador = [0, 0, 0, 0]    # Ganadas, Perdidas, Empates, Juegos

    main()
