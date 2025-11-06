import csv
from models.Movie import Movie
from exceptions.InvalidTitleException import InvalidTitleException
from exceptions.InvalidYearException import InvalidYearException
from exceptions.InvalidGenreException import InvalidGenreException
from exceptions.InvalidAgeLimitException import InvalidAgeLimitException


def creer_film():
    while True:
        try:
            titre = input("Titre du film : ")
            annee_production = int(input("Année de production : "))
            genre = input("Genre : ")
            age_limite = int(input("Âge minimum : "))

            film = Movie(titre, annee_production, genre, age_limite)
            print("Film créé avec succès :", film)
            return film

        except (InvalidTitleException, InvalidYearException,
                InvalidGenreException, InvalidAgeLimitException) as e:
            print("erreur :", e)
            print("Veuillez recommencer la saisie.\n")

        except ValueError:
            print("veuillez entrer des valeurs valides pour l'année et l'âge.")
            print("Veuillez recommencer la saisie.\n")


        finally:
            print("fin de la tentative de création.")


def ajouter_film():
    film = creer_film()
    if film == None:
        return

    try:
        with open("data/movies.csv", mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)

            writer.writerow([
                film.id,
                film.titre,
                film.annee_production,
                film.genre,
                film.age_limite
            ])

        print("film ajouté ")

    except Exception as e:
        print("erreur dans le CSV :", e)


if __name__ == "__main__":
    def check_id():
        try:
            with open("data/movies.csv", "r", encoding="utf-8") as file:
                ligne = file.readlines()
                if len(ligne) <= 1:  # fichier vide ou seulement l'en-tête
                    return 31
                else:
                    max_id = int(ligne[-1].split(",")[0])
                    return max_id + 1
        except FileNotFoundError:
            return 31

    Movie.id = check_id()

    ajouter_film()