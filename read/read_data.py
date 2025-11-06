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

def filtre_genre(genre_recherche :str):
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

def filtre_annee(annee_recherche):
    try:
        with open("data/movies.csv", "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)

            print(f"~~~~~~ films du genre : {annee_recherche} ~~~~~~")
            trouve = False
            for row in reader:
                if row[2] == str(annee_recherche):
                    print(f"ID: {row[0]} | Titre: {row[1]} | genre: {row[3]} | Âge min: {row[4]}")
                    trouve = True

        if not trouve:
            print("aucun film de cette année n'a été trouvé")

    except FileNotFoundError:
        print("erreur lors de la recherche")



if __name__ == "__main__":
    liste_film()

    print("~~~~ filtrer les films ~~~~")
    choix = input("Filtrer par (g)enre ou (a)nnée ?")

    if choix.lower() == "g":
        genre = input("entrez le genre : ")
        filtre_genre(genre)

    elif choix.lower() == "a":
        annee = input("entrez l'année : ")
        filtre_annee(annee)

    else:
        print("choix non valide.")