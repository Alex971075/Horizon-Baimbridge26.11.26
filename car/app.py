import os, secrets
from flask import Flask, request, render_template, session
from classes import Etudiant, Trajet, Reservation
import etudiant_dao, trajet_dao, reservation_dao

app = Flask(__name__)

#Not connected account
app.config["SECRET_KEY"] = os.environ.get("Cle_acces") or secrets.token_hex(32)

compte = Etudiant("UNKNOWN", "UNKNOWN", "UNKNOWN", "UNKNOWN", "UNKNOWN", "UNKNOWN", "UNKNOWN") #ide, email, nom, prenom, password, telephone, account_type

@app.route("/accueil")
def accueil():
    return render_template("accueil.html")

@app.route("/")
def connexion():
    message = ""
    email = request.args.get("email")
    passwd = request.args.get("passwd")
    if email and passwd:
        if etudiant_dao.compte_existe(passwd, email) == True:
            etudiants = etudiant_dao.get_etudiants()
            for etudiant in etudiants:
                if etudiant.email == email:
                    compte = etudiant

            session.clear()
            session["account"] = {
                "id": compte.id,
                "nom": compte.nom,
                "prenom": compte.prenom,
                "email": compte.email,
                "type": compte.type,
            }
            return render_template("accueil.html")
        else:
            message = "Identifiant ou mot de passe incorrects."
    return render_template("se_connecter.html", message=message)

@app.route("/ajouter_etudiant")
def ajouter_etudiant():
    message = ""
    nom = request.args.get("nom")
    prenom = request.args.get("prenom")
    email = request.args.get("email")
    telephone = request.args.get("telephone")
    passwd = request.args.get("passwd")
    passwd_bis = request.args.get("passwd_bis")
    if nom and prenom and email and telephone and passwd_bis and passwd:
        if len(telephone) == 10:
            if telephone.isdigit():
                if passwd_bis != passwd:
                    message = "Le mot de passe ne correspond pas à la confirmation."
                else:
                    etudiants = etudiant_dao.get_etudiants()
                    exist = False
                    for etudiant in etudiants:
                        if etudiant.email == email and exist == False:
                            exist = True

                    if exist == True:
                        message = "Cette adresse e-mail possède déjà un compte."
                    else:
                        etudiant = Etudiant(0, email, nom, prenom, passwd, telephone, "STUDENT")
                        etudiant_dao.ajouter_etudiant(etudiant)
                        message = "Etudiant ajouté dans la base de données."
            else:
                message = "Numéro de téléphone erroné."
        else:
            message = "Numéro de téléphone erroné."
    return render_template("ajouter_etudiant.html", message=message)

@app.route("/ajouter_trajet")
def ajouter_trajet():
    etudiants_list = etudiant_dao.get_etudiants()
    message = ""
    depart = request.args.get("depart")
    arrivee = request.args.get("arrivee")
    date = request.args.get("date")
    heure = request.args.get("heure")
    nb_places = request.args.get("nb_places")
    id_conducteur = request.args.get("id_conducteur")
    if arrivee and depart and date and heure and nb_places and id_conducteur:
        id_conducteur = id_conducteur[3]

        search = True
        etudiants = etudiant_dao.get_etudiants()
        for etudiant in etudiants:
            if str(etudiant.id) == str(id_conducteur):
                search = False
                conducteur = etudiant

        if search == True:
            message = "Conducteur non trouvé."

        elif arrivee != "LGT Baimbridge" and depart != "LGT Baimbridge":
            message = "Le départ ou l'arrivee doivent être LGT Baimbridge."
        else:
            trajet = Trajet(0, depart, arrivee, 
                date, heure, nb_places, conducteur)
            trajet_dao.ajouter_trajet(trajet)
            message = "Trajet enregistré."
    return render_template("ajouter_trajet.html", etudiants=etudiants_list, message=message)

@app.route("/ajouter_resa")
def ajouter_resa():
    message = ""
    trajets_date = trajet_dao.get_trajets_date()
    date_reservation = request.args.get("date_reservation")
    id_trajet = request.args.get("id_trajet")
    if date_reservation and id_trajet:
        search_deux = True
        trajets = trajet_dao.get_trajets()
        id_trajet = id_trajet[3]
        for trajet in trajets:
            if str(trajet.id) == str(id_trajet):
                search_deux = False
                save_trajet = trajet
        if search_deux == True:
            message = "Trajet non trouvé."
        else:
            resa = Reservation(0, 
                save_trajet, date_reservation)
            reservation_dao.ajouter_resa(resa)
            message = "Réservation ajoutée."
    return render_template("ajouter_resa.html", trajets=trajets_date, message=message)

@app.route("/etudiants")
def afficher_etudiants():
    etudiants = etudiant_dao.get_etudiants()
    return render_template("etudiants.html", etudiants=etudiants)

@app.route("/reservation")
def afficher_reservations():
    print(app.route)
    print("################################################################################################################################################################")
    reservations = reservation_dao.get_reservations()
    trajets = trajet_dao.get_trajets()
    etudiants = etudiant_dao.get_etudiants()
    for reservation in reservations:
        for trajet in trajets:
            if trajet.id == reservation.trajet:
                reservation.trajet = trajet
        for etudiant in etudiants:
            if etudiant.id == reservation.trajet.conducteur:
                reservation.trajet.conducteur = etudiant
    return render_template("reservation.html", reservations=reservations)

@app.route("/trajets")
def afficher_trajets():
    trajets = trajet_dao.get_trajets()
    etudiants = etudiant_dao.get_etudiants()
    for trajet in trajets:
        for etudiant in etudiants:
            if etudiant.id == trajet.conducteur:
                trajet.conducteur = etudiant
    return render_template("trajets.html", trajets=trajets)

if __name__ == "__main__":
    app.run(debug=True)