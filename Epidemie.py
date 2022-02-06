import json
from os import system
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
        print("warning erreur")
        json.dump(rollback, f,indent=4,ensure_ascii=False)
    f.close()


def lireFichier(fichier: str):
    initialisation(fichier)
    f = open(fichier, "r", encoding="utf8")
    data = json.load(f)
    f.close()
    return data

    
class Epidemie:

    def __init__(self, incidence:float, nom:str, type_propagation:str, taux_de_letalite: float, nbre_de_cas_confirme:int, nbre_vaccine:int ,personne_atteinte:int,numero:int=0):
        self.incidence = incidence
        self.nom = nom
        self.type_propagation = type_propagation
        self.taux_de_letalite = taux_de_letalite
        self.nbre_de_cas_confirme = nbre_de_cas_confirme
        self.nbre_vaccine = nbre_vaccine
        self.personne_atteinte = personne_atteinte
        if (numero == 0):
            data = lireFichier("fichier.json")
            if len(data["Epidemie"]) >0:
                self.numero = data["Epidemie"][-1]["numero"]+1
            else:
                self.numero = 1
        else:
            self.numero = numero

    #TODO Delete
    #TODO Additional attribute
    def supprimer(self):
        data = lireFichier("fichier.json")
        del data["Epidemie"][
            data["Epidemie"].index({
                "numero": self.numero,
                "incidence": self.incidence,
                "nom" : self.nom,
                "type_propagation" : self.type_propagation,
                "taux_de_letalite" : self.taux_de_letalite,
                "nbre_de_cas_confirme": self.nbre_de_cas_confirme,
                "nbre_vaccine": self.nbre_vaccine,
                "personne_atteinte": self.personne_atteinte       
            })
        ]
        ecrireFichier("fichier.json",data)
    
    def __str__(self):
        return str(self.numero)+" "+str(self.incidence)+" "+str(self.nom)+" "+str(self.type_propagation)+" "+str(self.taux_de_letalite)+" "+str(self.nbre_de_cas_confirme)+" "+str(self.nbre_vaccine)+" "+str(self.personne_atteinte)

    #TODO Ittérer sur la fonction
    def createEpidemie(self):
        data = lireFichier("D:\\Epidemologie_project\\fichier.json")
        print(data)
        system("pause")
        data["Epidemie"].append(
           {
               "numero": self.numero,
                "incidence": self.incidence,
                "nom" : self.nom,
                "type_propagation" : self.type_propagation,
                "taux_de_letalite" : self.taux_de_letalite,
                "nbre_de_cas_confirme": self.nbre_de_cas_confirme,
                "nbre_vaccine": self.nbre_vaccine,
                "personne_atteinte": self.personne_atteinte,
                "date": str(datetime.now())
            }
        )
        print(data)
        ecrireFichier("D:\\Epidemologie_project\\fichier.json",data)

    def trouver(numero: int):
        data = lireFichier("fichier.json")
        for epidemie in data["Epidemie"]:
            if numero == epidemie["numero"]:
                numero = epidemie["numero"]
                incidence = epidemie["incidence"]
                nom = epidemie["nom"]
                type_propagation = epidemie["type_propagation"]
                taux_de_letalite = epidemie["taux_de_letalite"]
                nbre_de_cas_confirme = epidemie["nbre_de_cas_confirme"]
                nbre_vaccine = epidemie["nbre_vaccine"]
                personne_atteinte = epidemie["personne_atteinte"]
                return Epidemie(incidence, nom, type_propagation, taux_de_letalite, nbre_de_cas_confirme, nbre_vaccine,personne_atteinte )
        return None


    def updateEpidemie(self):
         data = lireFichier("fichier.json")
         data["Epidemie"][
            data["Epidemie"].index({
            "numero": Epidemie.trouver(self.numero).numero,    
            "nom" : self.nom,
            "type_propagation" : self.type_propagation,
            "taux_de_letalite" : self.taux_de_letalite,
            "incidence": self.incidence,
            "nbre_de_cas_confirme": self.nbre_de_cas_confirme,
            "nbre_vaccine": self.nbre_vaccine,
            "personne_atteinte": self.personne_atteinte      
            })
        ] = {
            "numero": self.numero,
            "nom" : self.nom,
            "type_propagation" : self.type_propagation,
            "taux_de_letalite" : self.taux_de_letalite,
            "incidence": self.incidence,
            "nbre_de_cas_confirme": self.nbre_de_cas_confirme,
            "nbre_vaccine": self.nbre_vaccine,
            "personne_atteinte": self.personne_atteinte
        }
         ecrireFichier("fichier.json",data)

    def searchEpidemie(recherche: str=''):
         data = lireFichier("fichier.json")
         size = len(data["Epidemie"])
         for index in range(1,size+1):
            e = Epidemie.find(index)
            if recherche.lower() in e.nom.lower():
                print(e)


    def listEpidemie():
        data=lireFichier("D:\\Epidemologie_project\\fichier.json")
        print("\n #########  Liste des épidémies ############")
        if len(data["Epidemie"]) > 0:
            for epidemie in data["Epidemie"]:
                print(Epidemie.trouver(epidemie["numero"]))
        else:
            print("Aucune Epidemie trouvé!")