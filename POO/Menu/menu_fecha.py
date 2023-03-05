from menu import Menu
from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta


def main():
    options = ("Introducir Fecha (dd/mm/aaaa)", "Añadir Días", "Añadir Meses", "Añadir Años",
               "Comparar Fechas (dd/mm/aaaa)", "Formato Largo")
    m = Menu("Administrador de Fechas", options)
    global dt
    dt = None
    switch = False

    while True:
        selected = m.print_menu()

        match selected:
            case 0:
                break
            case 1:
                input_date()
                switch = True
            case 2:
                if switch:
                    add_days()
                switch_error()
            case 3:
                if switch:
                    add_months()
                switch_error()
            case 4:
                if switch:
                    add_years()
                switch_error()
            case 5:
                compare_date()
            case 6:
                print_large_date()


def switch_error():
    assert ValueError("Debes haber introducido una fecha para usar esta opción.")


def input_date():
    global dt
    dt = datetime.strptime(input("Ingrese una fecha en formato (dd/mm/aaaa): "), "%d/%m/%Y").date()


def add_days():
    global dt
    dt += relativedelta(days=int(input(f"Introduce la cantidad de días a añadir a {dt.strftime('%d/%m/%Y')}: ")))


def add_months():
    global dt
    dt += relativedelta(months=int(input(f"Introduce la cantidad de meses a añadir a {dt.strftime('%d/%m/%Y')}: ")))


def add_years():
    global dt
    dt += relativedelta(years=int(input(f"Introduce la cantidad de años a añadir a {dt.strftime('%d/%m/%Y')}: ")))


def compare_date():
    global dt
    new_dt = datetime.strptime(input("Ingrese una fecha en formato (dd/mm/aaaa): "), "%d/%m/%Y").date().strftime('%d/%m/%Y')

    if dt.strftime('%d/%m/%Y') < new_dt:
        print("La fecha introducida es MAYOR a la fecha almacenada")
    elif dt.strftime('%d/%m/%Y') > new_dt:
        print("La fecha introducida es MENOR a la fecha almacenada")
    else:
        print("La fecha introducida es IGUAL a la fecha almacenada")


def print_large_date():
    global dt
    format_date = str(datetime.strptime(dt, "%d/%m/%Y"))
    print(f'{format_date[0]}{format_date[1]}')


if __name__ == '__main__':
    global dt

    main()
