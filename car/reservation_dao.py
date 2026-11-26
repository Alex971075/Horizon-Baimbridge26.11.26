from db import get_connexion
from classes import Reservation

def ajouter_resa(resa):
    connexion = get_connexion()
    curseur = connexion.cursor()
    sql = "INSERT INTO reservation (id_trajet, date_reservation) VALUES(%s, %s)"
    valeurs = (int(resa.trajet.id), resa.date_reservation)
    curseur.execute(sql, valeurs)
    connexion.commit()
    curseur.close()
    connexion.close()

def get_reservations():
    connexion = get_connexion()
    curseur = connexion.cursor()
    curseur.execute("SELECT * FROM reservation")
    resultats = curseur.fetchall()
    reservations = []
    for ligne in resultats:
        resa = Reservation(ligne[0], ligne[1], ligne[2])
        reservations.append(resa)
    curseur.close()
    connexion.close()
    return reservations
