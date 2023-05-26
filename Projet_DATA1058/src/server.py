# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import psycopg2

hostName = "localhost"
serverPort = 1234
# Informations de connexion à la base de données PostgreSQL
db_host = "localhost"
db_port = 5432
db_name = "capteurlumiere" 
db_user = "postgres"
db_password = "admin"

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(bytes("Requête fonctionne correctement....", "utf-8"))
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        print(post_data)
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(bytes("Requête POST reçue...", "utf-8"))
        
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
        insert_query = "INSERT INTO valeurlum (valeur) VALUES (%s)"
        cursor.execute(insert_query, (post_data,))
        conn.commit()

        # Fermeture de la connexion à la base de données
        cursor.close()
        conn.close()


        
        '''comments
        '''


if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")