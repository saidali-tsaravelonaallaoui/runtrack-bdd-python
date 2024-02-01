import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password123@",
    database="laplateforme"
)

cursor = db.cursor()
request = "SELECT superficie from etage"
cursor.execute(request)
result = cursor.fetchall()
superficieTotal = 0
for i in result:
    superficieTotal += i[0]
    
print(f"La superficie de La Plateforme est de", superficieTotal,"m2")

cursor.close()
db.close()