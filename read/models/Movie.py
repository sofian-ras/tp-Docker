class Movie():
    id = 31
    def __init__(self, titre :str, annee_production :int, genre :str, age_limite :int):

      
        

        self.id= Movie.id
        Movie.id += 1
        self.titre=titre
        self.annee_production=annee_production
        self.genre=genre
        self.age_limite=age_limite

    def __str__(self):
        return f"{self.titre}, sortie en {self.annee_production} est un genre {self.genre} et est destiné aux plus de {self.age_limite}"
