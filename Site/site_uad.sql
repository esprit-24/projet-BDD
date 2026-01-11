-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : dim. 11 jan. 2026 à 15:14
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
-- Base de données : `site_uad`
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
-- Structure de la table `employe_uad`
--

CREATE TABLE `employe_uad` (
  `idEmp` int(11) NOT NULL,
  `nom` varchar(100) DEFAULT NULL,
  `adresse` varchar(150) DEFAULT NULL,
  `statut` varchar(50) DEFAULT NULL,
  `bibliotheque` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `employe_uad`
--

INSERT INTO `employe_uad` (`idEmp`, `nom`, `adresse`, `statut`, `bibliotheque`) VALUES
(101, 'Alioune Cissé', 'Dakar', 'Bibliothécaire', 'UAD'),
(102, 'Awa Ndiaye', 'Fann', 'Archiviste', 'UAD'),
(103, 'Mamadou Ba', 'Médina', 'Gestionnaire', 'UAD'),
(104, 'Khady Fall', 'Colobane', 'Bibliothécaire', 'UAD'),
(105, 'Ibrahima Diop', 'Parcelles Assainies', 'Archiviste', 'UAD'),
(106, 'Fatou Sow', 'Grand Yoff', 'Gestionnaire', 'UAD'),
(107, 'Cheikh Ndiaye', 'Hann', 'Bibliothécaire', 'UAD'),
(108, 'Mariama Sarr', 'Liberté 6', 'Archiviste', 'UAD'),
(109, 'Babacar Gueye', 'Ouakam', 'Gestionnaire', 'UAD'),
(110, 'Seynabou Ba', 'Point E', 'Bibliothécaire', 'UAD'),
(111, 'Lamine Fall', 'Mermoz', 'Archiviste', 'UAD'),
(112, 'Ndeye Khady Ndiaye', 'Sicap', 'Gestionnaire', 'UAD'),
(113, 'Ousmane Diallo', 'Yoff', 'Bibliothécaire', 'UAD'),
(114, 'Astou Ba', 'Ngor', 'Archiviste', 'UAD'),
(115, 'Abdoulaye Kane', 'Plateau', 'Gestionnaire', 'UAD'),
(116, 'Rokhaya Diop', 'HLM', 'Bibliothécaire', 'UAD'),
(117, 'Amadou Seye', 'Cambérène', 'Archiviste', 'UAD'),
(118, 'Aissatou Faye', 'Grand Dakar', 'Gestionnaire', 'UAD'),
(119, 'Serigne Fall', 'Dieuppeul', 'Bibliothécaire', 'UAD'),
(120, 'Coumba Ndiaye', 'Almadies', 'Archiviste', 'UAD');

-- --------------------------------------------------------

--
-- Structure de la table `etudiant_uad`
--

CREATE TABLE `etudiant_uad` (
  `idEtud` int(11) NOT NULL,
  `nom` varchar(100) DEFAULT NULL,
  `adresse` varchar(150) DEFAULT NULL,
  `universite` varchar(10) DEFAULT NULL,
  `specialite` varchar(100) DEFAULT NULL,
  `nbreEmprunts` int(11) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `etudiant_uad`
--

INSERT INTO `etudiant_uad` (`idEtud`, `nom`, `adresse`, `universite`, `specialite`, `nbreEmprunts`) VALUES
(101, 'Abdoulaye Ndiaye', 'Dakar', 'UAD', 'Informatique', 1),
(102, 'Mariama Fall', 'Fann', 'UAD', 'Mathématiques', 0),
(103, 'Moussa Diop', 'Médina', 'UAD', 'Physique', 2),
(104, 'Aissatou Ba', 'Colobane', 'UAD', 'Biologie', 1),
(105, 'Cheikh Gueye', 'Parcelles Assainies', 'UAD', 'Informatique', 0),
(106, 'Fatou Sarr', 'Grand Yoff', 'UAD', 'Maths', 1),
(107, 'Oumar Kane', 'Hann', 'UAD', 'Chimie', 0),
(108, 'Khady Sow', 'Liberté 6', 'UAD', 'Médecine', 2),
(109, 'Lamine Seck', 'Ouakam', 'UAD', 'Informatique', 1),
(110, 'Seynabou Ndiaye', 'Point E', 'UAD', 'Physique', 0),
(111, 'Ibrahima Diallo', 'Mermoz', 'UAD', 'Maths', 1),
(112, 'Ndeye Fatou Ba', 'Sicap', 'UAD', 'Biologie', 0),
(113, 'Babacar Faye', 'Yoff', 'UAD', 'Chimie', 1),
(114, 'Astou Ndiaye', 'Ngor', 'UAD', 'Informatique', 0),
(115, 'Ousmane Fall', 'Plateau', 'UAD', 'Physique', 2),
(116, 'Rokhaya Gueye', 'HLM', 'UAD', 'Maths', 1),
(117, 'Amadou Ly', 'Cambérène', 'UAD', 'Médecine', 0),
(118, 'Aissatou Seye', 'Grand Dakar', 'UAD', 'Informatique', 1),
(119, 'Serigne Mbaye', 'Dieuppeul', 'UAD', 'Biologie', 0),
(120, 'Coumba Diouf', 'Almadies', 'UAD', 'Chimie', 1);

-- --------------------------------------------------------

--
-- Structure de la table `ouvrage_uad`
--

CREATE TABLE `ouvrage_uad` (
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
-- Déchargement des données de la table `ouvrage_uad`
--

INSERT INTO `ouvrage_uad` (`idOuv`, `titre`, `idAut`, `editeur`, `annee`, `domaine`, `stock`, `site`) VALUES
(101, 'Bases de données relationnelles', 1, 'Dunod', 2021, 'Informatique', 5, 'UAD'),
(102, 'Programmation Java', 6, 'Pearson', 2020, 'Informatique', 4, 'UAD'),
(103, 'Algèbre linéaire', 10, 'Ellipses', 2019, 'Maths', 6, 'UAD'),
(104, 'Physique moderne', 9, 'Masson', 2018, 'Physique', 3, 'UAD'),
(105, 'Biologie humaine', 8, 'Elsevier', 2022, 'Biologie', 2, 'UAD'),
(106, 'Développement Web', 7, 'OReilly', 2023, 'Informatique', 7, 'UAD'),
(107, 'Statistiques', 5, 'Springer', 2020, 'Maths', 5, 'UAD'),
(108, 'Chimie générale', 4, 'Dunod', 2017, 'Chimie', 4, 'UAD'),
(109, 'Réseaux avancés', 2, 'Pearson', 2021, 'Informatique', 6, 'UAD'),
(110, 'Systèmes d’exploitation', 1, 'MIT Press', 2022, 'Informatique', 5, 'UAD'),
(111, 'Analyse numérique', 6, 'Ellipses', 2019, 'Maths', 4, 'UAD'),
(112, 'Optique avancée', 9, 'Masson', 2018, 'Physique', 3, 'UAD'),
(113, 'Génie logiciel', 10, 'Dunod', 2021, 'Informatique', 5, 'UAD'),
(114, 'Biologie moléculaire', 8, 'Elsevier', 2020, 'Biologie', 4, 'UAD'),
(115, 'Intelligence artificielle', 7, 'Springer', 2023, 'Informatique', 6, 'UAD'),
(116, 'Mathématiques discrètes', 5, 'Pearson', 2019, 'Maths', 5, 'UAD'),
(117, 'Cybersécurité', 6, 'OReilly', 2022, 'Informatique', 4, 'UAD'),
(118, 'Science des données', 1, 'Springer', 2021, 'Informatique', 6, 'UAD'),
(119, 'Physique quantique', 9, 'Masson', 2020, 'Physique', 2, 'UAD'),
(120, 'Programmation Python', 2, 'Dunod', 2023, 'Informatique', 7, 'UAD');

-- --------------------------------------------------------

--
-- Structure de la table `pret_uad`
--

CREATE TABLE `pret_uad` (
  `idOuv` int(11) NOT NULL,
  `idEtud` int(11) NOT NULL,
  `date_emprunt` date DEFAULT NULL,
  `date_retour` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `pret_uad`
--

INSERT INTO `pret_uad` (`idOuv`, `idEtud`, `date_emprunt`, `date_retour`) VALUES
(101, 101, '2025-01-11', '2025-01-21'),
(102, 115, '2025-01-20', NULL),
(103, 103, '2025-01-13', NULL),
(106, 105, '2025-01-14', '2025-01-24'),
(107, 116, '2025-01-21', '2025-01-31'),
(109, 108, '2025-01-16', NULL),
(110, 109, '2025-01-17', '2025-01-27'),
(115, 111, '2025-01-18', NULL),
(118, 113, '2025-01-19', '2025-01-29'),
(120, 118, '2025-01-22', NULL);

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `auteur`
--
ALTER TABLE `auteur`
  ADD PRIMARY KEY (`idAut`);

--
-- Index pour la table `employe_uad`
--
ALTER TABLE `employe_uad`
  ADD PRIMARY KEY (`idEmp`);

--
-- Index pour la table `etudiant_uad`
--
ALTER TABLE `etudiant_uad`
  ADD PRIMARY KEY (`idEtud`);

--
-- Index pour la table `ouvrage_uad`
--
ALTER TABLE `ouvrage_uad`
  ADD PRIMARY KEY (`idOuv`),
  ADD KEY `idAut` (`idAut`);

--
-- Index pour la table `pret_uad`
--
ALTER TABLE `pret_uad`
  ADD PRIMARY KEY (`idOuv`,`idEtud`),
  ADD KEY `idEtud` (`idEtud`);

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `ouvrage_uad`
--
ALTER TABLE `ouvrage_uad`
  ADD CONSTRAINT `ouvrage_uad_ibfk_1` FOREIGN KEY (`idAut`) REFERENCES `auteur` (`idAut`);

--
-- Contraintes pour la table `pret_uad`
--
ALTER TABLE `pret_uad`
  ADD CONSTRAINT `pret_uad_ibfk_1` FOREIGN KEY (`idOuv`) REFERENCES `ouvrage_uad` (`idOuv`),
  ADD CONSTRAINT `pret_uad_ibfk_2` FOREIGN KEY (`idEtud`) REFERENCES `etudiant_uad` (`idEtud`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
