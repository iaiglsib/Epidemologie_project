class Personne:
    def __init__(self, nom: str, prenom: str, adresse: str, age: int, sexe: str):
        self.nom = nom
        self.prenom = prenom
        self.adresse = adresse
        self.age = age
        self.sexe = sexe
    def __str__(self) :
        return self.nom + " " + self.prenom + " " + str(self.age) + " ans " + self.adresse + " " + self.sexe+ "\n"
