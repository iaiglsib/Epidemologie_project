from os import system
from Epidemie import *
from Personne import Personne
import json
from datetime import datetime

def initialisation(fichier: str):
    try:
        f = open(fichier,"r", encoding="utf8")
        if f.read() == "":
            data = {
                "Patient": [],
                "Epidemie": []
            }
            f.close()
            f = open(fichier, "w",encoding="utf8")
            json.dump(data, f, ensure_ascii=False, indent=4)
        f.close()
    except:
        f = open(fichier,"w+",encoding="utf8")
        data = {
                "Patient": [],
                "Epidemie": []
        }
        f.close()

def ecrireFichier(fichier: str, data):
    initialisation(fichier)
    rollback = lireFichier("fichier.json")
    f = open(fichier, "w", encoding="utf8")
    try:
        json.dump(data, f,indent=4,ensure_ascii=False)
    except:
        print("warning!!! erreur")
        json.dump(rollback, f,indent=4,ensure_ascii=False)
    f.close()

def lireFichier(fichier: str):
    initialisation(fichier)
    f = open(fichier, "r", encoding="utf8")
    data = json.load(f)
    f.close()
    return data


class Patient(Personne):
    def __init__(self, nom: str, prenom: str, adresse: str, age: int, sexe:str, Epidemie = [], numero: int=0):
        Personne.__init__(Patient,nom,prenom, adresse,age,sexe)
        self.Epidemie = Epidemie
        if (numero == 0):
            data = lireFichier("fichier.json")
            if len(data["Patient"]) >0:
                self.numero = data["Patient"][-1]["numero"]+1
            else:
                self.numero = 1
        else:
            self.numero = numero

    def supprPatient(self):
        data = lireFichier("fichier.json")
        del data["Patient"][
            data["Patient"].index({
                "numero": self.numero,
                "nom" : self.nom,
                "prenom" : self.prenom,
                "adresse" : self.adresse,
                "sexe" : self.sexe,
                "age" : self.age,
                "epidemie" : []
            })
        ]
        ecrireFichier("fichier.json", data)
        print("Patient supprimer avec succes !")

    def  __str__(self):
        return str(self.numero) + " " +super().__str__() #+" "+", ".join(self.Epidemie)

    def createPatient(self):
        data = lireFichier("D:\\Epidemologie_project\\fichier.json")
        print(data)
        system("pause")
        data["Patient"].append(
            {
                "numero": self.numero,
                "nom" : self.nom,
                "prenom" : self.prenom,
                "adresse" : self.adresse,
                "sexe" : self.sexe,
                "age" : self.age,
                "epidemie" :[],
                "date": str(datetime.now())
        })
        print(data)
        ecrireFichier("D:\\Epidemologie_project\\fichier.json",data)
        system("pause")


    def trouver(numero: int):
        data = lireFichier("fichier.json")
        for patient in data["Patient"]:
            if numero == patient["numero"]:
                numero = patient["numero"]
                nom = patient["nom"]
                prenom = patient["prenom"]
                adresse = patient["adresse"]
                sexe = patient["sexe"]
                age = patient["age"]
                #epidemie =patient["epidemie"]
                return Patient(nom, prenom, adresse, age, sexe, numero)
        return None


    def updatePatient(self):
        data = lireFichier("fichier.json")
        data["Patient"][
            data["Patient"].index({
                "numero": Patient.trouver(self.numero).numero,
                "nom" : Patient.trouver(self.nom).nom,
                "prenom" : Patient.trouver(self.prenom).prenom,
                "adresse" : Patient.trouver(self.adresse).adresse,
                "sexe" : Patient.trouver(self.sexe).sexe,
                "age" : Patient.trouver(self.age).age,
                "epidemie" : Patient.trouver(self.Epidemie).Epidemie
            })
        ] = {
             "numero": self.numero,
                "nom" : self.nom,
                "prenom" : self.prenom,
                "adresse" : self.adresse,
                "sexe" : self.sexe,
                "age" : self.age,
                "epidemie" : self.Epidemie
        }
        
        ecrireFichier("fichier.json",data)

    def searchPatient(recherche: str=''):
        data = lireFichier("fichier.json")
        for patient in data["Patient"]:
            p = Patient.find(patient["numero"])
            if (recherche.lower() in p.nom.lower()) or (recherche.lower() in p.prenom.lower()):
                print(p)
        """size = len(data["Patient"])
        for index in range(1,size+1):
            p = Patient.find(index)
            if (recherche.lower() in p.nom.lower()) or (recherche.lower() in p.prenom.lower()):
                print(p)
        """

    def listPatient():
        data=lireFichier("D:\\Epidemologie_project\\fichier.json")
        print("\n#########  Liste des patients  ############ \n")
        if len(data["Patient"]) > 0:
            for patient in data["Patient"]:
                print(Patient.trouver(patient["numero"]))
        else:
            print("Aucun patient trouvé!")
        
