import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password123@",
    database="laplateforme"
)

cursor = db.cursor()
requests = [
    "CREATE TABLE IF NOT EXISTS etage (id int NOT NULL AUTO_INCREMENT, nom varchar(255), numero int, superficie int, primary key(id))",
    "CREATE TABLE IF NOT EXISTS salle (id int NOT NULL AUTO_INCREMENT, nom varchar(255), id_etage int, capacite int, primary key(id))",
]
for request in requests:
    cursor.execute(request)
    result = cursor.fetchall()
    print(result)

cursor.close()
db.close()
