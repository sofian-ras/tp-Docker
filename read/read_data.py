import csv

def liste_film():
    try:
        with open("data/movies.csv", "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)

            print("~~~~~~ liste des films ~~~~~~")
            for row in reader:
                print(f"ID: {row[0]} | titre: {row[1]} | année: {row[2]} | genre: {row[3]} | age minimum: {row[4]}")

    except FileNotFoundError:
        print("erreur lors de la saisie (*~*)")


# 1) Récupérer un film par son titre
def recherche_par_titre(titre_recherche):
    try:
        with open("data/movies.csv", "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)

            trouve = False
            for row in reader:
                if row[1].lower() == titre_recherche.lower():
                    print(f"\nFilm trouvé : ")
                    print(f"ID: {row[0]} | Titre: {row[1]} | Année: {row[2]} | Genre: {row[3]} | Âge min: {row[4]}")
                    trouve = True

        if not trouve:
            print("Aucun film avec ce titre n'a été trouvé.")

    except FileNotFoundError:
        print("Erreur lors de la recherche")


# 2) Films avec limite d’âge <= valeur donnée
def films_par_age(max_age):
    try:
        with open("data/movies.csv", "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)

            print(f"\n~~~~~~ Films avec âge ≤ {max_age} ~~~~~~")
            trouve = False
            for row in reader:
                if int(row[4]) <= int(max_age):
                    print(f"ID: {row[0]} | {row[1]} | Genre: {row[3]} | Âge min: {row[4]}")
                    trouve = True

        if not trouve:
            print("Aucun film ne respecte cette limite d'âge.")

    except FileNotFoundError:
        print("Erreur lors de la recherche")


# 3) Films d’un certain genre (déjà existant)
def filtre_genre(genre_recherche):
    try:
        with open("data/movies.csv", "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)

            print(f"~~~~~~ films du genre : {genre_recherche} ~~~~~~")
            trouve = False
            for row in reader:
                if row[3].lower() == genre_recherche.lower():
                    print(f"ID: {row[0]} | Titre: {row[1]} | Année: {row[2]} | Âge min: {row[4]}")
                    trouve = True

        if not trouve:
            print("aucun film de ce genre n'a été trouvé")

    except FileNotFoundError:
        print("erreur lors de la recherche")


# 4) Films entre deux années
def films_entre_annees(debut, fin):
    try:
        with open("data/movies.csv", "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)

            print(f"\n~~~~~~ Films entre {debut} et {fin} ~~~~~~")
            trouve = False
            for row in reader:
                if int(debut) <= int(row[2]) <= int(fin):
                    print(f"ID: {row[0]} | {row[1]} | Année: {row[2]} | Genre: {row[3]}")
                    trouve = True

        if not trouve:
            print("Aucun film trouvé dans cette période.")

    except FileNotFoundError:
        print("Erreur lors de la recherche")


# Menu principal
if __name__ == "__main__":
    liste_film()

    print("\n~~~~ Actions disponibles ~~~~")
    print("1: Chercher par titre")
    print("2: Films avec âge maximum")
    print("3: Films d'un genre")
    print("4: Films entre deux années")

    choix = input("Votre choix : ")

    if choix == "1":
        titre = input("Entrez le titre : ")
        recherche_par_titre(titre)

    elif choix == "2":
        age = input("Âge maximum : ")
        films_par_age(age)

    elif choix == "3":
        genre = input("Genre : ")
        filtre_genre(genre)

    elif choix == "4":
        debut = input("Année début : ")
        fin = input("Année fin : ")
        films_entre_annees(debut, fin)

    else:
        print("Choix non valide.")
