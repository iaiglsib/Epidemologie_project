from Patient import *
from Epidemie import *
from os import system
from datetime import datetime

while True:
    system("cls")
    print("\t######################## WELCOME! - WEZON! #################################\n\n")
    print("\t** 1- Enregistrer patient **")
    print("\t** 2- Liste des patients **")
    print("\t** 3- Enregistrer une épidemie **")
    print("\t** 4- Liste des épidemie **")
    print("\t** 0- Quitter **")
    val = input("Faite votre choix: ")
    while val not in ("0","1","2","3","4"):
        system("cls")
        print("Veuillez ressaisir les votre Choix!")
        system("pause")
        system("cls")
        print("\t1- Enregistrer patient")
        print("\t2- Liste des patients")
        print("\t3- Enregistrer une épidemie")
        print("\t4- Liste des épidemie")
        print("\t0- Quitter")
        val = input("Faite votre choix: ")
    if val == "1":
        print("Enregistrons un patient...")
        nom = input("Entrer le nom du patient: ")
        prenom = input("Entrer le prenom du patient: ")
        adresse = input("Entrer l'adresse du patient: ")
        age = int(input("Entrer l'âge du patient: "))
        sexe = input("Entrer le sexe  du patient: ")
        epidemie=input("Choisissez l'epidemie : ")
        try:
            patient = Patient(nom, prenom, adresse, age, sexe,[])
            patient.createPatient()
        except:
            print("Erreur , veuillez reessayer l'enregistrement !!")

    elif val == "2":
        Patient.listPatient()
        system("pause")
    elif val == "3":
        print("Enregistrons une epidemie")
        nom = input("Entrer le nom de l'epidemie: ")
        type_propagation = input("Entrer le type de propagation: ")
        taux_de_letalite = float(input("Entrer le taux de letalite: "))
        incidence = float(input("Entrer l'incidence: "))
        nbre_de_cas_confirme = int(input("Entrer le nombre de cas confirme: "))
        nbre_vaccine = int(input("Entrer le nombre de vacine: "))
        personne_atteinte = int(input("Entrer le nombre de personne atteinte: "))
        try:
            epidemie = Epidemie(incidence, nom, type_propagation, taux_de_letalite, nbre_de_cas_confirme, nbre_vaccine, personne_atteinte)
            epidemie.createEpidemie()
        except:
            print("Erreur , veuillez reessayer l'enregistrement !!")
        print("Epidemie créé avec succes !")
        system("pause")
    elif val == "4":
        Epidemie.listEpidemie()
        system("pause")
    elif val == "0":
        break;
system("cls")   

