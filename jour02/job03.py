import mysql.connector

def connect_db():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password123@",
        database="laplateforme"
    )
    return db

def execute_query(db, request):
    cursor = db.cursor()
    cursor.execute(request)
    result = cursor.fetchall()
    print(result)
    cursor.close()

def insert_etage(db, nom, numero, superficie):
    request = f"INSERT INTO etage (nom, numero, superficie) VALUES ('{nom}', {numero}, {superficie})"
    execute_query(db, request)

def insert_salle(db, nom, id_etage, capacite):
    request = f"INSERT INTO salle (nom, id_etage, capacite) VALUES ('{nom}', {id_etage}, {capacite})"
    execute_query(db, request)

db = connect_db()

insert_etage(db, 'RDC', 0, 500)
insert_etage(db, 'R+1', 1, 500)
insert_salle(db, 'Lounge', 1, 100)
insert_salle(db, 'Studio Son', 1, 5)
insert_salle(db, 'Broadcasting', 2, 50)
insert_salle(db, 'Bocal Peda', 2, 4)
insert_salle(db, 'Coworking', 2, 80)
insert_salle(db, 'Studio Video', 2, 5)

db.commit()
db.close()
