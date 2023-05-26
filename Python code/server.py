# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
from flask import Flask, request
import time
import psycopg2

hostName = "localhost"
serverPort = 1234
# Informations de connexion à la base de données PostgreSQL
db_host = "localhost"
db_port = 5432
db_name = "AIOTCanadaTest" 
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
        '''
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
        insert_query = "INSERT INTO telemetrie (valeur) VALUES (%s)"
        cursor.execute(insert_query, (data,))
        conn.commit()

        # Fermeture de la connexion à la base de données
        cursor.close()
        conn.close()
        # Traitez les données reçues du microcontrôleur ici
        '''
        return 'Données reçues...'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

