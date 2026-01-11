-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : dim. 11 jan. 2026 à 15:15
-- Version du serveur : 10.4.32-MariaDB
-- Version de PHP : 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `site_ugb`
--

-- --------------------------------------------------------

--
-- Structure de la table `auteur`
--

CREATE TABLE `auteur` (
  `idAut` int(11) NOT NULL,
  `nom_auteur` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `auteur`
--

INSERT INTO `auteur` (`idAut`, `nom_auteur`) VALUES
(1, 'Cheikh Anta Diop'),
(2, 'Alioune Badara Bèye'),
(3, 'Ousmane Sembène'),
(4, 'Birago Diop'),
(5, 'Felwine Sarr'),
(6, 'Souleymane Bachir Diagne'),
(7, 'Fatou Diome'),
(8, 'Mariama Bâ'),
(9, 'Abdoulaye Wade'),
(10, 'Papa Malick Ngom');

-- --------------------------------------------------------

--
-- Structure de la table `employe_ugb`
--

CREATE TABLE `employe_ugb` (
  `idEmp` int(11) NOT NULL,
  `nom` varchar(100) DEFAULT NULL,
  `adresse` varchar(150) DEFAULT NULL,
  `statut` varchar(50) DEFAULT NULL,
  `bibliotheque` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `employe_ugb`
--

INSERT INTO `employe_ugb` (`idEmp`, `nom`, `adresse`, `statut`, `bibliotheque`) VALUES
(1, 'Modou Diouf', 'Sanar', 'Bibliothécaire', 'UGB'),
(2, 'Samba Fall', 'Pikine', 'Archiviste', 'UGB'),
(3, 'Awa Ba', 'Vaut Vert', 'Gestionnaire', 'UGB'),
(4, 'Ibrahima Kane', 'Khor', 'Bibliothécaire', 'UGB'),
(5, 'Fatou Ndiaye', 'Sanar', 'Archiviste', 'UGB'),
(6, 'Cheikh Diop', 'Guédiawaye', 'Gestionnaire', 'UGB'),
(7, 'Moussa Ba', 'Rufisque', 'Bibliothécaire', 'UGB'),
(8, 'Astou Fall', 'Sanar', 'Archiviste', 'UGB'),
(9, 'Babacar Seck', 'Pikine', 'Gestionnaire', 'UGB'),
(10, 'Khady Ndiaye', 'Vaut Vert', 'Bibliothécaire', 'UGB'),
(11, 'Oumar Diallo', 'Khor', 'Archiviste', 'UGB'),
(12, 'Seynabou Sow', 'Sanar', 'Gestionnaire', 'UGB'),
(13, 'Lamine Diop', 'Pikine', 'Bibliothécaire', 'UGB'),
(14, 'Rokhaya Ba', 'Vaut Vert', 'Archiviste', 'UGB'),
(15, 'Amadou Kane', 'Guédiawaye', 'Gestionnaire', 'UGB'),
(16, 'Aissatou Fall', 'Rufisque', 'Bibliothécaire', 'UGB'),
(17, 'Serigne Ba', 'Sanar', 'Archiviste', 'UGB'),
(18, 'Ndeye Khady Sow', 'Pikine', 'Gestionnaire', 'UGB'),
(19, 'Abdoulaye Diop', 'Vaut Vert', 'Bibliothécaire', 'UGB'),
(20, 'Mariama Seck', 'Khor', 'Archiviste', 'UGB');

-- --------------------------------------------------------

--
-- Structure de la table `etudiant_ugb`
--

CREATE TABLE `etudiant_ugb` (
  `idEtud` int(11) NOT NULL,
  `nom` varchar(100) DEFAULT NULL,
  `adresse` varchar(150) DEFAULT NULL,
  `universite` varchar(10) DEFAULT NULL,
  `specialite` varchar(100) DEFAULT NULL,
  `nbreEmprunts` int(11) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `etudiant_ugb`
--

INSERT INTO `etudiant_ugb` (`idEtud`, `nom`, `adresse`, `universite`, `specialite`, `nbreEmprunts`) VALUES
(1, 'Mamadou Diallo', 'Sanar', 'UGB', 'Informatique', 1),
(2, 'Awa Ndiaye', 'Sanar', 'UGB', 'Mathématiques', 0),
(3, 'Cheikh Fall', 'Pikine', 'UGB', 'Physique', 2),
(4, 'Fatou Sow', 'Vaut Vert', 'UGB', 'Biologie', 1),
(5, 'Ibrahima Sarr', 'Khor', 'UGB', 'Informatique', 0),
(6, 'Aminata Ba', 'Guédiawaye', 'UGB', 'Maths', 1),
(7, 'Abdou Diop', 'Rufisque', 'UGB', 'Chimie', 0),
(8, 'Khady Fall', 'Sanar', 'UGB', 'Médecine', 2),
(9, 'Lamine Gueye', 'Pikine', 'UGB', 'Informatique', 1),
(10, 'Seynabou Kane', 'Vaut Vert', 'UGB', 'Physique', 0),
(11, 'Moussa Ndoye', 'Khor', 'UGB', 'Maths', 1),
(12, 'Ndeye Fatou Fall', 'Sanar', 'UGB', 'Biologie', 0),
(13, 'Babacar Ndiaye', 'Pikine', 'UGB', 'Chimie', 1),
(14, 'Astou Diop', 'Vaut Vert', 'UGB', 'Informatique', 0),
(15, 'Omar Ba', 'Guédiawaye', 'UGB', 'Physique', 2),
(16, 'Rokhaya Sow', 'Rufisque', 'UGB', 'Maths', 1),
(17, 'Amadou Ly', 'Sanar', 'UGB', 'Médecine', 0),
(18, 'Aissatou Diallo', 'Khor', 'UGB', 'Informatique', 1),
(19, 'Serigne Fall', 'Pikine', 'UGB', 'Biologie', 0),
(20, 'Coumba Seck', 'Vaut Vert', 'UGB', 'Chimie', 1);

-- --------------------------------------------------------

--
-- Structure de la table `ouvrage_ugb`
--

CREATE TABLE `ouvrage_ugb` (
  `idOuv` int(11) NOT NULL,
  `titre` varchar(150) DEFAULT NULL,
  `idAut` int(11) DEFAULT NULL,
  `editeur` varchar(100) DEFAULT NULL,
  `annee` int(11) DEFAULT NULL,
  `domaine` varchar(50) DEFAULT NULL,
  `stock` int(11) DEFAULT NULL,
  `site` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `ouvrage_ugb`
--

INSERT INTO `ouvrage_ugb` (`idOuv`, `titre`, `idAut`, `editeur`, `annee`, `domaine`, `stock`, `site`) VALUES
(1, 'Bases de données distribuées', 1, 'PUF', 2021, 'Informatique', 5, 'UGB'),
(2, 'Algorithmique avancée', 6, 'Dunod', 2020, 'Informatique', 4, 'UGB'),
(3, 'Analyse mathématique', 10, 'Ellipses', 2019, 'Maths', 6, 'UGB'),
(4, 'Physique générale', 9, 'Masson', 2018, 'Physique', 3, 'UGB'),
(5, 'Introduction à la médecine', 8, 'Elsevier', 2022, 'Médecine', 2, 'UGB'),
(6, 'Programmation Python', 7, 'OReilly', 2023, 'Informatique', 7, 'UGB'),
(7, 'Statistiques appliquées', 5, 'Springer', 2020, 'Maths', 5, 'UGB'),
(8, 'Chimie organique', 4, 'Dunod', 2017, 'Chimie', 4, 'UGB'),
(9, 'Réseaux informatiques', 2, 'Pearson', 2021, 'Informatique', 6, 'UGB'),
(10, 'Systèmes distribués', 1, 'MIT Press', 2022, 'Informatique', 5, 'UGB'),
(11, 'Calcul numérique', 6, 'Ellipses', 2019, 'Maths', 4, 'UGB'),
(12, 'Optique physique', 9, 'Masson', 2018, 'Physique', 3, 'UGB'),
(13, 'Bases du génie logiciel', 10, 'Dunod', 2021, 'Informatique', 5, 'UGB'),
(14, 'Biologie cellulaire', 8, 'Elsevier', 2020, 'Biologie', 4, 'UGB'),
(15, 'IA et Machine Learning', 7, 'Springer', 2023, 'Informatique', 6, 'UGB'),
(16, 'Maths discrètes', 5, 'Pearson', 2019, 'Maths', 5, 'UGB'),
(17, 'Sécurité informatique', 6, 'OReilly', 2022, 'Informatique', 4, 'UGB'),
(18, 'Analyse de données', 1, 'Springer', 2021, 'Informatique', 6, 'UGB'),
(19, 'Physique quantique', 9, 'Masson', 2020, 'Physique', 2, 'UGB'),
(20, 'Programmation Java', 2, 'Dunod', 2023, 'Informatique', 7, 'UGB');

-- --------------------------------------------------------

--
-- Structure de la table `pret_ugb`
--

CREATE TABLE `pret_ugb` (
  `idOuv` int(11) NOT NULL,
  `idEtud` int(11) NOT NULL,
  `date_emprunt` date DEFAULT NULL,
  `date_retour` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `pret_ugb`
--

INSERT INTO `pret_ugb` (`idOuv`, `idEtud`, `date_emprunt`, `date_retour`) VALUES
(1, 1, '2025-01-10', '2025-01-20'),
(2, 15, '2025-01-21', NULL),
(3, 3, '2025-01-12', NULL),
(6, 5, '2025-01-15', '2025-01-25'),
(7, 16, '2025-01-22', '2025-02-01'),
(9, 8, '2025-01-16', NULL),
(10, 9, '2025-01-18', '2025-01-28'),
(15, 11, '2025-01-19', NULL),
(18, 13, '2025-01-20', '2025-01-30'),
(20, 18, '2025-01-23', NULL);

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `auteur`
--
ALTER TABLE `auteur`
  ADD PRIMARY KEY (`idAut`);

--
-- Index pour la table `employe_ugb`
--
ALTER TABLE `employe_ugb`
  ADD PRIMARY KEY (`idEmp`);

--
-- Index pour la table `etudiant_ugb`
--
ALTER TABLE `etudiant_ugb`
  ADD PRIMARY KEY (`idEtud`);

--
-- Index pour la table `ouvrage_ugb`
--
ALTER TABLE `ouvrage_ugb`
  ADD PRIMARY KEY (`idOuv`),
  ADD KEY `idAut` (`idAut`);

--
-- Index pour la table `pret_ugb`
--
ALTER TABLE `pret_ugb`
  ADD PRIMARY KEY (`idOuv`,`idEtud`),
  ADD KEY `idEtud` (`idEtud`);

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `ouvrage_ugb`
--
ALTER TABLE `ouvrage_ugb`
  ADD CONSTRAINT `ouvrage_ugb_ibfk_1` FOREIGN KEY (`idAut`) REFERENCES `auteur` (`idAut`);

--
-- Contraintes pour la table `pret_ugb`
--
ALTER TABLE `pret_ugb`
  ADD CONSTRAINT `pret_ugb_ibfk_1` FOREIGN KEY (`idOuv`) REFERENCES `ouvrage_ugb` (`idOuv`),
  ADD CONSTRAINT `pret_ugb_ibfk_2` FOREIGN KEY (`idEtud`) REFERENCES `etudiant_ugb` (`idEtud`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
