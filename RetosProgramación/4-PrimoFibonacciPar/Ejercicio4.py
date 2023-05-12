"""
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
"""


def main():
    n = int(input("Introduzca un número: "))
    if is_primo(n):
        primo = "es primo"
    else:
        primo = "no es primo"

    if is_fibonacci(n):
        fibonacci = "es fibonacci"
    else:
        fibonacci = "no es fibonacci"

    if is_par(n):
        par = "es par"
    else:
        par = "es impar"

    print(f"El número {n} {primo}, {fibonacci} y {par}")


def is_primo(number):
    if number <= 1:
        return False

    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False

    return True


def is_fibonacci(number):
    if number == 0 or number == 1:
        return True

    a = 0
    b = 1

    while b <= number:
        if b == number:
            return True

        a, b = b, a + b

    return False


def is_par(number):
    if number % 2 == 0:
        return True
    return False


if __name__ == '__main__':
    while True:
        main()
