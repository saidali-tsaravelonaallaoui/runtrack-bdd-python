show database;
use laplateforme;
create table etudiant(
    id int NOT NULL AUTO_INCREMENT,
    nom varchar(255) NOT NULL,
    prenom varchar(255) NOT NULL,
    age int NOT NULL,
    email varchar(255) NOT NULL,
    PRIMARY KEY (id)
    );
