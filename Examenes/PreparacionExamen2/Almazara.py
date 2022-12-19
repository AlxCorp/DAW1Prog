# Author: Alejandro Priego Izquierdo
# Date: 19/12/2022

def main():
    global precio_liquidacion_aceite

    print("Este es un programa para gestionar la producción de una Almazara")
    print("----------------------------------------------------------------")

    insertar_cosecheros()
    aportaciones_aceituna()

    precio_liquidacion_aceite = float(input("Introduzca el precio de liquidación del Aceite (€/Kg): "))

    imprimir_cosecheros()
    imprimir_total()


def insertar_cosecheros():
    global cosecheros

    num_cosecheros = int(input("Inserte el número de cosecheros de los que desea almacenar información: "))
    print()
    cosecheros = [[] * 3 for _ in range(num_cosecheros)]

    for n in range(num_cosecheros):
        cosecheros[n].append(input("Ingrese el DNI: "))
        cosecheros[n].append(input("Ingrese el NOMBRE: "))
        cosecheros[n].append(input("Ingrese la LOCALIDAD: "))
        print()


def aportaciones_aceituna():
    global contador_entregas

    while contador_entregas <= 100:
        cosechero = identificar_cosechero()

        if cosechero == "fin_entrada":
            return "Entrada de entregas finalizada"
        else:
            aportaciones.append([cosechero, cantidad_entregada(),
                                float(input("Ingrese el rendimiento de esta aceituna (en %): "))])

        contador_entregas += 1

    print("ERROR: Ya no pueden realizarse más entregas")
    return


def cantidad_entregada():
    while True:
        cantidad_aceituna_kg = float(input("Ingrese la cantidad de aceituna aportada (en Kg): "))
        if cantidad_aceituna_kg >= 0:
            break
        else:
            print("Debes ingresar un número mayor o igual a 0")

    return cantidad_aceituna_kg


def identificar_cosechero():
    while True:
        cosechero_dni = input("Introduzca el DNI del cosechero del que desea registrar su "
                              "aportación (0 para finalizar): ")
        if cosechero_dni == "0":
            return "fin_entrada"
        for n in range(len(cosecheros)):
            if cosechero_dni == cosecheros[n][0]:
                return n
        print("Cosechero no registrado, vuelva a intentarlo.")


def imprimir_cosecheros():
    def sort_key(item):
        # Devuelve el parámetro 2 como la clave de ordenamiento primaria
        # y el parámetro 1 como la clave de ordenamiento secundaria
        return item[2], item[1]

    cosecheros_ordenados = sorted(cosecheros, key=sort_key)

    print(f"{'DNI':^9}   {'NOMBRE':^20}   {'LOCALIDAD':^15}")
    print(f"{'-' * 50}")
    for c in cosecheros_ordenados:
        print(f"{c[0]:^9}   {c[1]:^20}   {c[2]:^15}")


def imprimir_total():
    aportaciones_final = []

    print()
    print(f'{"Nombre":^20}   {"Localidad":^15}   {"Kilos Uva":^20}   {"Kilos Aceite":^20}   {"Importe a Liquidar":^20}')
    print("-" * 107)
    for n in aportaciones:
        aportaciones_final.append([cosecheros[n[0]][1], cosecheros[n[0]][2], n[1], n[1]*(n[2]/100),
                                   (n[1]*(n[2]/100)) * precio_liquidacion_aceite])

    aportaciones_final.sort(key=lambda x: x[2])

    for n in aportaciones_final:
        print(f'{n[0]:^20}   {n[1]:^15}   {n[2]:^17}   {n[3]:^17}   {n[4]:^17}')


if __name__ == '__main__':
    cosecheros = []
    aportaciones = []
    MAXIMO_ENTREGAS = 100
    contador_entregas = 0
    precio_liquidacion_aceite = 0

    main()
