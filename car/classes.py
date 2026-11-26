class Etudiant:

    def __init__(self, ide, email, nom, prenom, password, telephone, account_type):
        self.id = ide
        self.password = password
        self.nom = nom
        self.prenom = prenom
        self.email = email
        self.telephone = telephone
        self.type = account_type
        self.trajets = []
        self.est_actif = True
        empreinteHash = ""

    def consulter_trajets(self):
        if len(self.trajets) == 0:
            print("Aucun trajet")
        else:
            for trajet in self.trajets:
                print(trajet.afficher())

    def consulter_reservations(self):
        return ("pas de reservations")

    def consulter_trajet(self, id_trajet):
            if len(self.trajets) < id_trajet:
                print("Ce trajet n'existe pas")
            else:
                print(self.trajets[id_trajet].afficher())

class Trajet:
    def __init__(self, id, ville_depart, ville_arrivee, 
                date_trajet, heure_depart, nb_places, conducteur):
        self.id = id
        self.ville_depart = ville_depart
        self.ville_arrivee = ville_arrivee
        self.date_trajet = date_trajet
        self.heure_depart = heure_depart
        self.nb_places = nb_places
        self.conducteur = conducteur

    def afficher(self):
        return "Trajet " + self.id + " - Départ de " + self.ville_depart + " pour " + self.ville_arrivee + "à la date du " + str(self.date_trajet) + str(self.heure_depart) + " comptant " + str(self.nb_places) + " places."

class Reservation:
    def __init__(self, id, trajet, date_reservation):
        self.id = id
        self.trajet = trajet
        self.date_reservation = date_reservation