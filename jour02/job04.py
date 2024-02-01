import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password123@",
    database="laplateforme"
)

cursor = db.cursor()
request = "SELECT salle.nom, salle.capacite FROM salle"
cursor.execute(request)
result = cursor.fetchall()
print(result)

cursor.close()
db.close()