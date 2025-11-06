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

def modifier_film():
    film_id = input("entrez l'id du film à modifier : ") # on stocke l'id en string
    films = [] # liste dans laquelle on va stocker les films

    try:
        # on ouvre le fichier avec open et lit avec "r"
        with open("data/movies.csv", "r", encoding="utf-_") as file:
            reader = csv.reader(file)
            header = next(reader)
            films.append(header)

            film_trouve = False # de base il est en False
            # on va parcourir chque ligne du csv 
            for row in reader:
                # row une ligne sous forme de liste
                if row[0] == film_id:
                    print("Modification du film :")
                    nouveau_film = creer_film()
                    nouveau_film.id = int(film_id)

                    films.append([
                        nouveau_film.id,
                        nouveau_film.titre,
                        nouveau_film.annee_production,
                        nouveau_film.genre,
                        nouveau_film.age_limite
                    ])
                    film_trouve = True
                else:
                    films.append(row)

        if not film_trouve:
            print(f"Aucun film trouvé avec l'id {film_id}.")
            return

        # Réécrire le CSV avec la modification
        with open("data/movies.csv", "w", newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(films) # nouvelle liste films avec tous les films ainsi que celui modifié

        print("film modifié avec succès !")

    except Exception as e:
        print("erreur lors de la modification :", e)


def supprimer_film():
    film_sup_id = input("selectionner l'id du film a supprimer: ")
    films = []

    try:
        with open("data/movies.csv", "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            header = next(reader)

            for row in reader:
                if row[0] != film_sup_id:
                    films.append(row)

        with open("data/movies.csv", "w", newline='',encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(header)
            writer.writerows(films)

        print("film supprimé !")

    except Exception as e:
        print("erreur lors de la modification :", e)

modifier_film()
supprimer_film()
