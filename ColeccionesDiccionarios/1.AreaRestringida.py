"""
Implementa el control de acceso al área restringida de un programa. Se debe pedir un nombre de usuario y una contraseña.
Si el usuario introduce los datos correctamente, el programa dirá “Ha accedido al área restringida”. El usuario tendrá
un máximo de 3 oportunidades. Si se agotan las oportunidades el programa dirá “Lo siento, no tiene acceso al área
restringida”. Los nombres de usuario con sus correspondientes contraseñas deben estar almacenados en un diccionario.

Author: Alejandro Priego Izquierdo
Date: 12-03-2023
"""

USERS = {"Hola": "AdIoS", "Que": "tal", "Estas": "tU"}


def main():
    hints = 0
    while hints < 3:
        user = input_user()

        if not user:
            hints += 1
            continue

        password = input_password(user)

        if not password:
            hints += 1
            continue

        else:
            access_granted()
    access_denied()


def input_user():
    user = input("Por favor, ingrese el usuario: ")
    if not user:
        print("El usuario no puede estar vacío!")
        return False
    try:
        check_user(user)
        return user
    except ValueError:
        print("Usuario no encontrado!")
        return False


def input_password(user):
    password = input(f'Por favor, ingrese la contraseña para el usuario "{user}": ')
    if not password:
        print("La contraseña no puede estar vacía!")
        return False
    try:
        check_password(password)
        return password
    except ValueError:
        print("Contraseña no válida!")
        return False


def check_user(user):
    if user in USERS.keys():
        return True
    else:
        raise ValueError("Usuario no encontrado!")


def check_password(password):
    if password in USERS.values():
        return True
    else:
        raise ValueError("Contraseña no válida!")


def access_granted():
    print("Ha accedido al área restringida")
    print("""
                                             _       
                                            | |      
              ___ ___  _ __   __ _ _ __ __ _| |_ ___ 
             / __/ _ \| '_ \ / _` | '__/ _` | __/ __|
            | (_| (_) | | | | (_| | | | (_| | |_\__ \\
             \___\___/|_| |_|\__, |_|  \__,_|\__|___/
                              __/ |                  
                             |___/                   
    """)
    quit()


def access_denied():
    print("Lo siento, no tiene acceso al área restringida")
    quit(1)


if __name__ == '__main__':

    main()
