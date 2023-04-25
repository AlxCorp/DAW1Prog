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
import os
import sys
# import webbrowser
from PIL import Image
from requests import request, get
from menu import Menu

MOVIEAPITOKEN = os.getenv('MOVIEAPITOKEN')
API = "https://api.themoviedb.org/3/"
genres = []


def main():
    check_connection()

    show_all_genders(first=True)

    args = ("Buscar código de película por nombre",
            "Buscar información de película por código TMDB y enlace a web imdb",
            "Recomendaciones en base a otra película",
            "Obtener las 5 películas 'trending topic' semanal o del día en función del género de la misma",
            "Mostrar géneros disponibles")

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
                ranking_5_movies()
            case 5:
                show_all_genders()


def check_connection():
    try:
        r = request("GET", "https://www.cuatro.com/cuarto-milenio/")
    except ConnectionError:
        print("ERROR: No tienes conexión a internet, revisa tu conexión y ejecuta el programa de nuevo",
              file=sys.stderr)
        exit(1)
    except:
        print("ERROR: Ha ocurrido un problema, revisa tu conexión y ejecuta el programa de nuevo",
              file=sys.stderr)
        exit(1)


def search_code_with_name(internal=False):
    """
    Esta función nos permite buscar el código e información básica de una película en base al nombre.
    :param internal: Este parámetro sirve para que devuelva el código de la primera película encontrada, pero no lo imprima
    :return: Devuelve el código de la primera línea encontrada.
    """
    # https://developers.themoviedb.org/3/search/search-companies
    question = "Introduce el título de la película: "
    endpoint = f"{API}search/movie?api_key={MOVIEAPITOKEN}&language=es-ES&" \
               f"query={input(question)}&page=1&include_adult=true"

    r = request("GET", endpoint)
    r_json = r.json()

    if r.status_code == 404:
        print(f"ERROR: Película no encontrada, código de error {r.status_code}", file=sys.stderr)
        return "not_found"

    if r.status_code != 200:
        print(f"ERROR: El servidor no responde, código de error {r.status_code}", file=sys.stderr)
        return "server_error"

    if not internal:
        for n in range(len(r_json["results"])):
            print("\n", r_json["results"][n]["title"], "\n",  r_json["results"][n]["overview"],
                  "\n", r_json["results"][n]["release_date"], "\n", r_json["results"][n]["id"], "\n")
    elif internal:
        return r_json["results"][0]["id"]


def search_info_url_with_code():
    """
    Esta función nos permite buscar información detallada de una película y su url de IMDB en base al código.
    :return: Esta función no devuelve nada.
    """
    # https://developers.themoviedb.org/3/movies/get-movie-details
    question = "Introduce el código de la película: "
    endpoint = f"{API}movie/{input(question)}?api_key={MOVIEAPITOKEN}&language=es-ES"

    r = request("GET", endpoint)
    r_json = r.json()

    if r.status_code == 404:
        print(f"ERROR: Película no encontrada, código de error {r.status_code}", file=sys.stderr)
        return "not_found"

    if r.status_code != 200:
        print(f"ERROR: El servidor no responde, código de error {r.status_code}", file=sys.stderr)
        return "server_error"

    print(f'Título: {r_json["title"]} \n '
          f'Géneros: {[n["name"] for n in r_json["genres"]]} \n '
          f'Descripción: {r_json["overview"]} \n '
          f'Duración: {r_json["runtime"]} \n '
          f'Fecha de Publicación: {r_json["release_date"]} \n'
          f'Puntuación (0-10): {r_json["vote_average"]} \n'
          f'IMDB URL: https://www.imdb.com/title/{r_json["imdb_id"]}/ \n')

    poster = input("¿Quieres ver el poster de la película? (S/N): ").upper()

    if poster == "S":
        """ Nos permite mostrar el poster de la película """
        r = get(f'https://image.tmdb.org/t/p/w500{r_json["poster_path"]}')
        open('temp_poster.jpg', 'wb').write(r.content)
        img = Image.open("temp_poster.jpg")
        img.show()
        print("\n")
        # webbrowser.open(f'https://image.tmdb.org/t/p/w500{r_json["poster_path"]}') Podríamos abrir imagen en navegador
    print()


def recommendation_from_another_movie(page: int = 1, code: int = 0):
    """
    Esta función nos recomienda películas en base a otra.
    :return: Esta función no devuelve nada.
    """
    # https://developers.themoviedb.org/3/movies/get-similar-movies
    if page == 1:
        question = input("¿Quieres buscar por nombre(N) o por código(C)?: ").upper()
        if question == "N":
            question = search_code_with_name(internal=True)
        elif question == "C":
            question = input("Introduce el código de la película: ")
        else:
            print("\n\nERROR: Debes introducir una de las opciones válidas.\n\n", file=sys.stderr)
            return

        endpoint = f"{API}movie/{question}/similar?api_key={MOVIEAPITOKEN}&language=es-ES"
        movie_code = question
    else:
        endpoint = f"{API}movie/{code}/similar?api_key={MOVIEAPITOKEN}&language=es-ES&page={page}"
        movie_code = code

    r = request("GET", endpoint)
    r_json = r.json()

    if r.status_code == 404:
        print(f"ERROR: Película no encontrada, código de error {r.status_code}", file=sys.stderr)
        return "not_found"

    if r.status_code != 200:
        print(f"ERROR: El servidor no responde, código de error {r.status_code}", file=sys.stderr)
        return "server_error"

    for n in r_json["results"]:
        print("\n", n["title"], "\n", n["overview"], "\n", n["release_date"], "\n", n["id"], "\n")

    more_pages = input("¿Deseas mostrar más recomendaciones? (S/N): ").upper()
    if more_pages == "S":
        recommendation_from_another_movie(page=page+1, code=movie_code)

    print("\n")


def ranking_5_movies():
    """
    Muestra el ranking diario o semanal de 5 películas. Podemos indicar categoría específica.
    :return:
    """
    # https://developers.themoviedb.org/3/trending/get-trending
    question = input('¿Deseas el "trending topic" Diario(D) o Semanal(S)?: ').upper()
    if question == "D":
        question = "day"
    elif question == "S":
        question = "week"
    else:
        raise ValueError('Debes ingresar "D" o "S"')

    page = 1
    endpoint = f"{API}trending/movie/{question}?api_key={MOVIEAPITOKEN}&page={page}"

    r = request("GET", endpoint)
    r_json = r.json()

    if r.status_code == 404:
        print(f"ERROR: Película no encontrada, código de error {r.status_code}", file=sys.stderr)
        return "not_found"

    if r.status_code != 200:
        print(f"ERROR: El servidor no responde, código de error {r.status_code}", file=sys.stderr)
        return "server_error"

    ask_genre_search = input('¿Deseas buscar películas de algún género en concreto? (S/N): ').upper()
    if ask_genre_search == "S":
        ask_genre = input('Introduce el género a filtrar (Tal y como aparece en el listado): ')
        genres_names = [g["name"] for g in genres]
        genres_ids = [g["id"] for g in genres]
        if ask_genre in genres_names:
            selected_genre_id = genres_ids[genres_names.index(ask_genre)]
        else:
            print(f"\n\nERROR: El género introducido es erróneo\n\n", file=sys.stderr)
            return

        limiter = 0

        def movie_printer():
            nonlocal limiter
            for z in r_json["results"]:
                if selected_genre_id in z["genre_ids"]:
                    print("\n", z["title"], "\n", z["id"])
                    limiter += 1
                    if limiter > 4:
                        break

        while limiter < 5:
            movie_printer()
            page += 1
            endpoint = f"{API}trending/movie/{question}?api_key={MOVIEAPITOKEN}&page={page}"
            r = request("GET", endpoint)
            r_json = r.json()

    else:
        limiter = 0
        for n in r_json["results"]:
            print("\n", n["title"], "\n", n["overview"], "\n", n["release_date"], "\n", n["id"])
            limiter += 1
            if limiter > 4:
                break
    print("\n")


def show_all_genders(first=False):
    """
    Esta función consulta y muestra todos los géneros posibles.
    :param first: Nos permite ejecutarlo al comenzar el programa para poder tener el listado y usarlo en otras funciones
    :return: Esta función no devuelve nada.
    """
    # https://developers.themoviedb.org/3/genres/get-movie-list
    global genres
    if first:
        endpoint = f"{API}genre/movie/list?api_key={MOVIEAPITOKEN}&language=es-ES"

        r = request("GET", endpoint)
        r_json = r.json()

        if r.status_code == 404:
            print(f"ERROR: Película no encontrada, código de error {r.status_code}", file=sys.stderr)
            return "not_found"

        if r.status_code != 200:
            print(f"ERROR: El servidor no responde, código de error {r.status_code}", file=sys.stderr)
            return "server_error"

        genres = r_json["genres"]
    #        r_json = r.json()["genres"]
    #        genres = [n["name"] for n in r_json]
    else:
        #        print(genres, "\n\n")
        print("Lista de Géneros Disponibles")
        print("----------------------------")
        for n in genres:
            print(f'\t - {n["name"]}')
        print("\n")


if __name__ == '__main__':
    main()
