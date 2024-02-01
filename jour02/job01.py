import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password123@",
    database="laplateforme"
)

cursor = db.cursor()
request = "SELECT * FROM etudiant"
cursor.execute(request)
result = cursor.fetchall()
for etudiant in result:
    print('ID : {0}, Nom : {1}, Prenom : {2}, Age : {3}, Email : {4}'.format(etudiant[0], etudiant[1], etudiant[2], etudiant[3], etudiant[4]))


cursor.close()
db.close()
