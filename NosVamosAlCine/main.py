"""
Queremos ir al cine con nuestras amistades, pero no queremos ir a ver cualquier película, para ello queremos 
información antes de decidir qué vamos a ver. Esta información la vamos a sacar de un servicio web, en concreto de TMDB.
Nuestro programa tendrá un menú (usando la clase diseñada para este fin) con las siguientes opciones:
    - Buscar código de película según su nombre.
    - Buscar información de película según su código y enlace a su web imdb.
    - Películas a recomendar si nos gusta una película concreta.
    - Queremos obtener las 5 películas "trending topic" semanal o del día en función del género de la misma. Al usuario 
        le preguntamos si quiere un género concreto o si los quiere todos.
    - Mostrar géneros disponibles. 
    
Author: Alejandro Priego Izquierdo 
Date: 19/04/23
"""
from menu import Menu
from requests import request

API = "https://api.themoviedb.org/3/"


def search_code_with_name():
    question = "Introduce el título de la película: "
    endpoint = f"{API}search/movie?api_key={MOVIEAPITOKEN.replace(' ', '%20')}&language=es-ES&"\
               f"query={input(question)}&page=1&include_adult=true"

    r = request("GET", endpoint).json()

    print(r["results"][0]["id"], "\n")


def search_info_url_with_code():
    pass


def recommendation_from_another_movie():
    pass


def ranking_5_movies():
    pass


def show_all_genders():
    pass


def main():

    args = ("Buscar código de película según su nombre.",
            "Buscar información de película según su código y enlace a su web imdb.",
            "Películas a recomendar si nos gusta una película concreta.",
            "Queremos obtener las 5 películas 'trending topic' semanal o del día en función del género de la misma. Al \
            usuario le preguntamos si quiere un género concreto o si los quiere todos.",
            "Mostrar géneros disponibles.")

    while True:
        m = Menu("Nos Vamos al Cine", args)
        option = m.print_menu()

        match option:
            case 0:
                break
            case 1:
                search_code_with_name()
            case 2:
                search_info_url_with_code()
            case 3:
                recommendation_from_another_movie()
            case 4:
                # ranking_5_movies_weekly()
                # ranking_5_movies_daily()
                ranking_5_movies()
            case 5:
                show_all_genders()


if __name__ == '__main__':
    import os

    MOVIEAPITOKEN = os.getenv('MOVIEAPITOKEN')

    main()
