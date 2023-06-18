# https://www.programiz.com/python-programming/methods/built-in/isinstance

def lista_o_tupla(entrada):
    if type(entrada[0]) == list and len(entrada) != 1:
        raise ValueError("Debes ingresar UNA lista o VARIOS valores, NO ambas cosas")
    if type(entrada[0]) == list:
        return entrada[0]
    if type(entrada[0]) == int:
        return entrada


def maximum(*x):
    filtered_input = lista_o_tupla(x)
    return max(filtered_input)


def minimum(*x):
    filtered_input = lista_o_tupla(x)
    return min(filtered_input)


def mean(*x):
    filtered_input = lista_o_tupla(x)

    media = 0
    numbers_counter = 0
    for n in filtered_input:
        media += n
        numbers_counter += 1
        media /= numbers_counter
    return media


def variance(*x):
    filtered_input = lista_o_tupla(x)

    varianza = 0
    contador_alumnos = len(filtered_input)
    for n in filtered_input:
        varianza += pow(n - mean(filtered_input), 2)
    varianza /= contador_alumnos
    varianza *= 1 / 2
    return varianza


def median(*x):
    filtered_input = sorted(lista_o_tupla(x))

    if len(filtered_input) % 2 != 0:
        return filtered_input[(len(filtered_input)//2)]

    return (filtered_input[(len(filtered_input) // 2)] + filtered_input[(len(filtered_input) // 2) + 1]) / 2


def mode(*x):
    filtered_input = lista_o_tupla(x)
    valores_unicos = []
    ocurrencias = []
    modas = []

    for n in filtered_input:
        if n in valores_unicos:
            ocurrencias[valores_unicos.index(n)] += 1
        elif n not in valores_unicos:
            valores_unicos.append(n)
            ocurrencias.append(1)

    repeticiones_maximas = max(ocurrencias)
    if ocurrencias.count(repeticiones_maximas) == 1:
        modas.append(valores_unicos[ocurrencias.index(repeticiones_maximas)])
        return modas
    elif ocurrencias.count(repeticiones_maximas) > 1:
        for n in range(len(ocurrencias)):
            if ocurrencias[n] == repeticiones_maximas:
                modas.append(valores_unicos[n])
        return modas


if __name__ == "__main__":
    print(mode(1,3,5,7,9,11,13,15,17,19, 21,4,6,2,1,2,4,6,7,8,3,2,12,3,5,53,6,4,3,3))

# assert math.isclose(median(1,2,3,4,5), 4) == True
