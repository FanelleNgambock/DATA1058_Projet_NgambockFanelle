# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
from flask import Flask, request
import time
import psycopg2
import urllib.parse

hostName = "localhost"
serverPort = 1234
# Informations de connexion à la base de données PostgreSQL
db_host = "localhost"
db_port = 5432
db_name = "suivi_croissance" 
db_user = "postgres"
db_password = "admin"

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def handle_request():
    if request.method == 'GET':
        return 'Requête GET reçue.'
    elif request.method == 'POST':
        data = request.get_data(as_text=True)
        print(data)

        # Analyse de la chaîne de requête
        parsed_query = urllib.parse.parse_qs(data)

        # Extraction des valeurs
        mac_address = parsed_query.get('mac_address', [None])[0]
        vapeurEau = int(parsed_query.get('vapeurEau', [0])[0])
        luminosite = int(parsed_query.get('luminosite', [0])[0])
        humidite = int(parsed_query.get('humidite', [0])[0])
        co2 = int(parsed_query.get('co2', [0])[0])

        # Affichage des valeurs extraites
        print("MAC address:", mac_address)
        print("Vapeur d'eau:", vapeurEau)
        print("Luminosité:", luminosite)
        print("Humidité:", humidite)
        print("CO2:", co2)
        
        # Connexion à la base de données PostgreSQL
        conn = psycopg2.connect(
            host=db_host,
            port=db_port,
            database=db_name,
            user=db_user,
            password=db_password
        )
        # Création d'un curseur pour exécuter des requêtes
        cursor = conn.cursor()

        # Exemple d'insertion des données dans une table nommée "temperature_data"
        insert_query = "INSERT INTO record (mac_address, vapeur_eau, luminosite, humidite, co2_value) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(insert_query, (mac_address, vapeurEau, luminosite, humidite, co2,))
        conn.commit()

        # Fermeture de la connexion à la base de données
        cursor.close()
        conn.close()
        # Traitez les données reçues du microcontrôleur ici
        
        return 'Données reçues...'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

