import mysql.connector

def get_connexion():
 return mysql.connector.connect(
 host="localhost",
 user="root",
 password="",
 database="baimbridge_horizon"
 )