"""
- es_capicua: devuelve verdadero si el número que se pasa como parámetro es capicúa y falso en caso contrario.
- es_primo: devuelve verdadero si el número que se pasa como parámetro es primo y falso en caso contrario. ??
- siguiente_primo: devuelve el menor primo que es mayor al número que se pasa como parámetro.
- digitos: devuelve el número de dígitos de un número entero.
- voltea: le da la vuelta a un número.
- digito_n: devuelve el dígito que está en la posición n de un número entero. Se empieza contando por el 0 y de
    izquierda a derecha.
- posicion_de_digito: da la posición de la primera ocurrencia de un dígito dentro de un número entero. Si no se
    encuentra, devuelve -1.
- quita_por_detras: le quita a un número n dígitos por detrás (por la derecha).
- quita_por_delante: le quita a un número n dígitos por delante (por la izquierda).
- pega_por_detras: añade un dígito a un número por detrás.
- pega_por_delante: añade un dígito a un número por delante.
- trozoDeNumero: toma como parámetros las posiciones inicial y final dentro de un número y devuelve el trozo
    correspondiente.
- junta_numeros: pega dos números para formar uno.
"""
# Author: Alejandro Priego Izquierdo
# Date: 18/12/2022

def digitos(x):
    x = abs(x)

    if x == 0:
        return 1

    contador = 0
    while x != 0:
        x //= 10
        contador += 1
    return contador


def digito_n(x, n):
    if x < 0:
        raise ValueError("Debes ingresar valores POSITIVOS")
    elif n > (digitos(x) - 1):
        raise ValueError("Esa posición no existe en este número")
    length = digitos(x)

    first_n_num_digits = x // (10 ** (length - n - 1))

    return first_n_num_digits % 10


def quita_por_detras(x, n):
    if n > digitos(x):
        raise ValueError("Has introducido más posiciones que dígitos tiene el número")

    length = digitos(x)

    x_substract_last_n_num_digits = x // (10 ** (length - n + 1))

    return x_substract_last_n_num_digits


def quita_por_delante(x, n):
    if n > digitos(x):
        raise ValueError("Has introducido más posiciones que dígitos tiene el número")

    length = digitos(x)

    x_substract_first_n_num_digits = x % (10 ** (length - n))

    return x_substract_first_n_num_digits


def junta_numeros(x, y):
    if x >= 0 and y >= 0:
        len_y = digitos(y)
        x *= 10 ** len_y

        return x + y
    raise ValueError("Debes ingresar valores POSITIVOS")


def pega_por_detras(x, y):
    if digitos(y) != 1:
        raise ValueError("Debes ingresar un solo dígito")
    elif y < 0:
        raise ValueError("Debes ingresar valores POSITIVOS")

    return x * 10 + y


def pega_por_delante(x, y):
    if digitos(y) != 1:
        raise ValueError("Debes ingresar un solo dígito")
    elif y < 0:
        raise ValueError("Debes ingresar valores POSITIVOS")

    return x + (y * (10 ** digitos(x)))


def es_primo(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    elif x % 2 == 0:
        return False
    for i in range(3, int(x ** 1/2) + 1, 2):
        if x % i == 0:
            return False
    return True


def siguiente_primo(x):
    if x < 2:
        return 2
    elif x == 2:
        return 3

    candidato_primo = x + 1
    while not es_primo(candidato_primo):
        candidato_primo += 1

    return candidato_primo


def voltea(x):
    if x < 0:
        raise ValueError("Debes ingresar valores POSITIVOS")

    numero_volteado = 0
    for n in range(digitos(x)):
        numero_volteado *= 10
        numero_volteado += digito_n(x, (digitos(x) - n - 1))

    return numero_volteado


def es_capicua(x):
    if x == voltea(x):
        return True
    return False


def trozo_de_numero(x, y, z):
    if x < 0:
        raise ValueError("Debes ingresar un número positivo")
    elif y < 0 or z > (digitos(x) - 1):
        raise ValueError("Esa posición no existe en este número")
    elif y > z:
        raise ValueError("")

    new_number = 0
    for i in range(y, (z + 1)):
        new_number += digito_n(x, i)
        new_number *= 10
    new_number //= 10

    return new_number


def posicion_de_digito(x, n):
    if x < 0:
        raise ValueError("Debes ingresar un número positivo")
    elif digitos(n) != 1:
        raise ValueError("Debes ingresar UN único dígito")

    posicion = 0
    for i in range(digitos(x)):
        candidato = digito_n(x, i)
        if candidato == n:
            return posicion
        posicion += 1
    return -1


if __name__ == "__main__":

    # Test digitos
    assert digitos(0) == 1
    assert digitos(2) == 1
    assert digitos(1243452) == 7
    assert digitos(-123432) == 6

    # Test digito_n
    # assert digito_n(-142142, 0) == "ERROR: Debes ingresar un número positivo"
    assert digito_n(0, 0) == 0
    assert digito_n(1, 0) == 1
    assert digito_n(12345, 4) == 5

    # Test quita_por_detras

    # Test quita_por_delante

    # Test junta_numeros

    # Test pega_por_detras

    # Test pega_por_delante

    # Test es_primo
    assert es_primo(-5) == False
    assert es_primo(0) == False
    assert es_primo(1) == False
    assert es_primo(2) == True
    assert es_primo(5) == True
    assert es_primo(6) == False
    assert es_primo(7) == True

    # Test siguiente_primo
    assert siguiente_primo(4993) == 4999

    # Test voltea

    # Test es_capicua

    # Test trozo_de_numero

    # Test posicion_de_digito
