from db import get_connexion
from classes import Etudiant

def ajouter_etudiant(etudiant):
    connexion = get_connexion()
    curseur = connexion.cursor()
    sql = "INSERT INTO etudiant (nom, prenom, email, telephone, motDePasse, type, est_actif) VALUES(%s, %s, %s, %s, %s, %s, %s)"
    valeurs = (etudiant.nom, etudiant.prenom, etudiant.email, etudiant.telephone, etudiant.password, "STUDENT", True)
    curseur.execute(sql, valeurs)
    connexion.commit()
    curseur.close()
    connexion.close()

def get_etudiants():
    connexion = get_connexion()
    curseur = connexion.cursor()
    curseur.execute("SELECT id, email, nom, prenom, motDePasse, telephone, type FROM etudiant")
    resultats = curseur.fetchall()
    etudiants = []
    for ligne in resultats:
        etudiant = Etudiant(ligne[0], ligne[1], ligne[2], ligne[3], ligne[4], ligne[5], ligne[6])
        etudiants.append(etudiant)
    curseur.close()
    connexion.close()
    return etudiants

def compte_existe(passwd, email):
    connexion = get_connexion()
    curseur = connexion.cursor()
    sql = ("SELECT * FROM etudiant WHERE motDePasse = %s AND email = %s")
    valeurs = (passwd, email)
    curseur.execute(sql, valeurs)
    resultats = curseur.fetchall()
    curseur.close()
    connexion.close()

    if resultats == []:
        return False
    return True