-- ============================
-- Base UGB - MySQL
-- ============================

-- ============================
-- Table AUTEUR
-- ============================
CREATE TABLE auteur (
    idAut INT PRIMARY KEY,
    nom_auteur VARCHAR(100)
) ENGINE=InnoDB;

-- ============================
-- Table EMPLOYE_UGB
-- ============================
CREATE TABLE employe_ugb (
    idEmp INT PRIMARY KEY,
    nom VARCHAR(100),
    adresse VARCHAR(150),
    statut VARCHAR(50),
    bibliotheque VARCHAR(50)
) ENGINE=InnoDB;

-- ============================
-- Table ETUDIANT_UGB
-- ============================
CREATE TABLE etudiant_ugb (
    idEtud INT PRIMARY KEY,
    nom VARCHAR(100),
    adresse VARCHAR(150),
    universite VARCHAR(10),
    specialite VARCHAR(100),
    nbreEmprunts INT DEFAULT 0
) ENGINE=InnoDB;

-- ============================
-- Table OUVRAGE_UGB
-- ============================
CREATE TABLE ouvrage_ugb (
    idOuv INT PRIMARY KEY,
    titre VARCHAR(150),
    idAut INT,
    editeur VARCHAR(100),
    annee INT,
    domaine VARCHAR(50),
    stock INT,
    site VARCHAR(10),
    CONSTRAINT fk_auteur_ugb
        FOREIGN KEY (idAut)
        REFERENCES auteur(idAut)
        ON DELETE SET NULL
) ENGINE=InnoDB;

-- ============================
-- Table PRET_UGB
-- ============================
CREATE TABLE pret_ugb (
    idOuv INT,
    idEtud INT,
    date_emprunt DATE,
    date_retour DATE,
    CONSTRAINT pk_pret_ugb PRIMARY KEY (idOuv, idEtud),
    CONSTRAINT fk_pret_ouvrage_ugb
        FOREIGN KEY (idOuv)
        REFERENCES ouvrage_ugb(idOuv)
        ON DELETE CASCADE,
    CONSTRAINT fk_pret_etudiant_ugb
        FOREIGN KEY (idEtud)
        REFERENCES etudiant_ugb(idEtud)
        ON DELETE CASCADE
) ENGINE=InnoDB;

-- ============================

-- ============================
-- Données de test UGB
-- ============================

INSERT INTO auteur VALUES
(1, 'Auteur UGB 1'),
(2, 'Auteur UGB 2');

INSERT INTO etudiant_ugb VALUES
(1, 'Diop', 'Saint-Louis', 'UGB', 'Informatique', 0),
(2, 'Ba', 'Louga', 'UGB', 'Physique', 0);

INSERT INTO ouvrage_ugb VALUES
(1, 'Systèmes distribués', 1, 'Springer', 2021, 'Informatique', 4, 'UGB'),
(2, 'Réseaux', 2, 'Pearson', 2020, 'Informatique', 2, 'UGB');

INSERT INTO employe_ugb VALUES
(1, 'Ndiaye', 'Saint-Louis', 'Bibliothécaire', 'UGB'),
(2, 'Diallo', 'Saint-Louis', 'Assistant', 'UGB');