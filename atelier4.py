class Employe:
    def __init__(self, numeroPermis, nom, prenom):
        self.numeroPermis = numeroPermis
        self.nom = nom
        self.prenom = prenom
        self.voitureService = None

    def afficherInformations(self):
            print("Employé :", self.nom, self.prenom)
            print("Permis :", self.numeroPermis)

            if self.voitureService is not None:
                print("Voiture :", self.voitureService.marque)
            else:
                print("Pas de voiture de service")

class Voiture:
    def __init__(self, matricule, annee, marque, kilometrage):
        self.matricule = matricule
        self.annee = annee
        self.marque = marque
        self.kilometrage = kilometrage
        self.chauffeur = None
    def afficherInformations(self):
        print("Matricule :", self.matricule)
        print("Année :", self.annee)
        print("Marque :", self.marque)
        print("Kilométrage :", self.kilometrage)

        if self.chauffeur is not None:
            print("Chauffeur :", self.chauffeur.nom, self.chauffeur.prenom)
        else:
            print("Aucun chauffeur")
def affecterVoiture(self, voiture):
    if self.voitureService is not None:
        print("Cet employé possède déjà une voiture")
    elif voiture.chauffeur is not None:
        print("Cette voiture est déjà attribuée")
    else:
        self.voitureService = voiture
        voiture.chauffeur = self
        print("Voiture affectée avec succès")
def retirerVoiture(self):
    if self.voitureService is None:
        print("Aucune voiture à retirer")
    else:
        self.voitureService.chauffeur = None
        self.voitureService = None
        print("Voiture retirée")
e1 = Employe("P123", "Dyhia", "Malika")
e2 = Employe("P456", "Sara", "Lina")

v1 = Voiture("AA111", 2022, "Toyota", 10000)
v2 = Voiture("BB222", 2023, "Honda", 5000)
e1.afficherInformations()
v1.afficherInformations()