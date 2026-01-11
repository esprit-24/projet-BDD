CREATE TABLE auteur (
  idAut INT PRIMARY KEY,
  nom_auteur VARCHAR(100)
);

CREATE TABLE employe_ugb (
  idEmp INT PRIMARY KEY,
  nom VARCHAR(100),
  adresse VARCHAR(150),
  statut VARCHAR(50),
  bibliotheque VARCHAR(50)
);

CREATE TABLE etudiant_ugb (
  idEtud INT PRIMARY KEY,
  nom VARCHAR(100),
  adresse VARCHAR(150),
  universite VARCHAR(10),
  specialite VARCHAR(100),
  nbreEmprunts INT DEFAULT 0
);

CREATE TABLE ouvrage_ugb (
  idOuv INT PRIMARY KEY,
  titre VARCHAR(150),
  idAut INT,
  editeur VARCHAR(100),
  annee INT,
  domaine VARCHAR(50),
  stock INT,
  site VARCHAR(10),
  FOREIGN KEY (idAut) REFERENCES auteur(idAut)
);

CREATE TABLE pret_ugb (
  idOuv INT,
  idEtud INT,
  date_emprunt DATE,
  date_retour DATE,
  PRIMARY KEY (idOuv, idEtud),
  FOREIGN KEY (idOuv) REFERENCES ouvrage_ugb(idOuv),
  FOREIGN KEY (idEtud) REFERENCES etudiant_ugb(idEtud)
);
