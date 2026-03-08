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