from read.models.Movie import Movie
from write.exceptions.InvalidTitleException import InvalidTitleException
from write.exceptions.InvalidYearException import InvalidYearException
from write.exceptions.InvalidGenreException import InvalidGenreException
from write.exceptions.InvalidAgeLimitException import InvalidAgeLimitException

def creer_film():
    try:
        titre = input("Titre du film : ")
        annee = int(input("Année de production : "))
        genre = input("Genre : ")
        age = int(input("Âge minimum : "))

        film = Movie(titre, annee, genre, age)
        print("✅ Film créé avec succès :", film)

    except (InvalidTitleException, InvalidYearException, InvalidGenreException, InvalidAgeLimitException) as e:
        print(" Erreur :", e)

    finally:
        print("Fin de la tentative de création.\n")


if __name__ == "__main__":
    creer_film()