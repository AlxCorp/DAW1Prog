# Diseña un programa que lea un carácter de teclado y muestre por pantalla el mensaje «Es signo de puntuación» solo
# si el carácter leído es un signo de puntuación, «Es una letra» si es una letra (da igual que sea mayúscula,
# minúscula o acentuada), «Es un dígito» si es un dígito, «Es otro carácter» si no es ninguno de los anteriores y «No
# es un carácter» si el usuario ha introducido más de un carácter.
# Author: Alejandro Priego Izquierdo
# Date: 19/10/2022

# Encabezado del ejercicio
print("")
print("Este programa el tipo de carácter ingresado")
print("-------------------------------------------")

# Preguntamos los números
character = input("Ingrese un carácter para determinar el tipo del mismo: ")

characterASCI = ord(character)

match characterASCI:
    case 44 | 46 | 58 | 59:
        print("El signo", character, "Es un signo de Puntuación")

if character.isalpha():
    print("El carácter es una Letra")