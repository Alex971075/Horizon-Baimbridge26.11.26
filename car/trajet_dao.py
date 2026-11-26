from db import get_connexion
from classes import Trajet

def ajouter_trajet(trajet):
    connexion = get_connexion()
    curseur = connexion.cursor()
    sql = "INSERT INTO trajet (date_trajet, heure_depart, ville_depart, ville_arrivee, nb_places, id_conducteur) VALUES(%s, %s, %s, %s, %s, %s)"
    valeurs = (trajet.date_trajet, trajet.heure_depart, trajet.ville_depart, trajet.ville_arrivee, int(trajet.nb_places), int(trajet.conducteur.id))
    curseur.execute(sql, valeurs)
    connexion.commit()
    curseur.close()
    connexion.close()

def get_trajets():
    connexion = get_connexion()
    curseur = connexion.cursor()
    curseur.execute("SELECT id, date_trajet, heure_depart, ville_depart, nb_places, id_conducteur, ville_arrivee FROM trajet")
    resultats = curseur.fetchall()
    trajets = []
    for ligne in resultats:
        trajet = Trajet(ligne[0], ligne[3], ligne[6], ligne[1], ligne[2], ligne[4], ligne[5])
        trajets.append(trajet)
    curseur.close()
    connexion.close()
    return trajets

def get_trajets_date():
    connexion = get_connexion()
    curseur = connexion.cursor()
    curseur.execute("SELECT id, date_trajet, heure_depart, ville_depart, nb_places, id_conducteur, ville_arrivee FROM trajet WHERE date_trajet > CURDATE()")
    resultats = curseur.fetchall()
    trajets = []
    for ligne in resultats:
        trajet = Trajet(ligne[0], ligne[3], ligne[6], ligne[1], ligne[2], ligne[4], ligne[5])
        trajets.append(trajet)
    curseur.close()
    connexion.close()
    return trajets
