import mysql.connector

def connect_db():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password123@",
        database="entreprise"
    )
    return db

def execute_query(db, query):
    cursor = db.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)
    cursor.close()

def create_employe_table(db):
    query = "CREATE TABLE IF NOT EXISTS employe (id int NOT NULL AUTO_INCREMENT, nom varchar(255), prenom varchar(255), salaire decimal, id_service int, primary key(id))"
    execute_query(db, query)

def insert_employe(db, nom, prenom, salaire, id_service):
    query = f"INSERT INTO employe (nom, prenom, salaire, id_service) VALUES ('{nom}', '{prenom}', {salaire}, {id_service})"
    execute_query(db, query)

def select_employe(db, condition):
    query = f"SELECT * FROM employe WHERE {condition}"
    execute_query(db, query)

def create_service_table(db):
    query = "CREATE TABLE IF NOT EXISTS service (id int NOT NULL AUTO_INCREMENT, nom varchar(255), primary key(id))"
    execute_query(db, query)

def insert_service(db, nom):
    query = f"INSERT INTO service (nom) VALUES ('{nom}')"
    execute_query(db, query)

def select_employe_service(db):
    query = "SELECT employe.nom, employe.prenom, service.nom FROM employe JOIN service ON employe.id_service = service.id"
    execute_query(db, query)

db = connect_db()

create_employe_table(db)

insert_employe(db, 'Monkey D', 'Luffy', 10000, 1)
insert_employe(db, 'Roronoa', 'Zoro', 7500, 1)
insert_employe(db, 'Nami', 'La Navigatrice', 2000, 2)
insert_employe(db, 'Usopp', 'Sniperking', 2500, 2)
insert_employe(db, 'Sanji', 'Vinsmoke', 7500, 3)
insert_employe(db, 'Tony-Tony', 'Choppy', 1000, 4)
insert_employe(db, 'Nico', 'Robin', 5000, 4)
select_employe(db, "salaire > '3000'")

create_service_table(db)

insert_service(db, 'Pirate')
insert_service(db, 'Epéiste')
insert_service(db, 'Cartographe')
insert_service(db, 'Sniper')
insert_service(db, 'Cuisinier')
insert_service(db, 'Médecin')
insert_service(db, 'Archéologue')

select_employe_service(db)

db.commit()
db.close()
