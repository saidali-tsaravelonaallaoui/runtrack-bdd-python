import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password123@",
    database="laplateforme"
)

cursor = db.cursor()
request = "SELECT capacite from salle"
cursor.execute(request)
result = cursor.fetchall()
capaciteTotal = 0
for i in result:
    capaciteTotal += i[0]
    
print(f"La capacite de toutes les salles est de :", capaciteTotal)

cursor.close()
db.close()