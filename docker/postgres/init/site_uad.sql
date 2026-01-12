-- ============================
-- Base UAD - PostgreSQL
-- ============================

-- ============================
-- Table AUTEUR
-- ============================
CREATE TABLE auteur (
    idAut INTEGER PRIMARY KEY,
    nom_auteur VARCHAR(100)
);

-- ============================
-- Table EMPLOYE_UAD
-- ============================
CREATE TABLE employe_uad (
    idEmp INTEGER PRIMARY KEY,
    nom VARCHAR(100),
    adresse VARCHAR(150),
    statut VARCHAR(50),
    bibliotheque VARCHAR(50)
);

-- ============================
-- Table ETUDIANT_UAD
-- ============================
CREATE TABLE etudiant_uad (
    idEtud INTEGER PRIMARY KEY,
    nom VARCHAR(100),
    adresse VARCHAR(150),
    universite VARCHAR(10),
    specialite VARCHAR(100),
    nbreEmprunts INTEGER DEFAULT 0
);

-- ============================
-- Table OUVRAGE_UAD
-- ============================
CREATE TABLE ouvrage_uad (
    idOuv INTEGER PRIMARY KEY,
    titre VARCHAR(150),
    idAut INTEGER,
    editeur VARCHAR(100),
    annee INTEGER,
    domaine VARCHAR(50),
    stock INTEGER,
    site VARCHAR(10),
    CONSTRAINT fk_auteur_uad
        FOREIGN KEY (idAut)
        REFERENCES auteur(idAut)
        ON DELETE SET NULL
);

-- ============================
-- Table PRET_UAD
-- ============================
CREATE TABLE pret_uad (
    idOuv INTEGER,
    idEtud INTEGER,
    date_emprunt DATE,
    date_retour DATE,
    CONSTRAINT pk_pret_uad PRIMARY KEY (idOuv, idEtud),
    CONSTRAINT fk_pret_ouvrage_uad
        FOREIGN KEY (idOuv)
        REFERENCES ouvrage_uad(idOuv)
        ON DELETE CASCADE,
    CONSTRAINT fk_pret_etudiant_uad
        FOREIGN KEY (idEtud)
        REFERENCES etudiant_uad(idEtud)
        ON DELETE CASCADE
);

-- ============================

-- ============================
-- Données de test UAD
-- ============================

INSERT INTO auteur VALUES
(1, 'Auteur UAD 1'),
(2, 'Auteur UAD 2');

INSERT INTO etudiant_uad VALUES
(1, 'Fall', 'Bambey', 'UAD', 'Informatique', 0),
(2, 'Ndiaye', 'Diourbel', 'UAD', 'Maths', 0);

INSERT INTO ouvrage_uad VALUES
(1, 'Bases de données', 1, 'Dunod', 2023, 'Informatique', 5, 'UAD'),
(2, 'Algorithmique', 2, 'Eyrolles', 2022, 'Informatique', 3, 'UAD');

INSERT INTO employe_uad VALUES
(1, 'Sarr', 'Bambey', 'Bibliothécaire', 'UAD'),
(2, 'Faye', 'Diourbel', 'Assistant', 'UAD');
