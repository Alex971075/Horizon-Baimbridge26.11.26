-- phpMyAdmin SQL Dump
-- version 5.2.3
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : jeu. 26 nov. 2026 à 12:02
-- Version du serveur : 8.4.7
-- Version de PHP : 8.3.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `baimbridge_horizon`
--

-- --------------------------------------------------------

--
-- Structure de la table `etudiant`
--

DROP TABLE IF EXISTS `etudiant`;
CREATE TABLE IF NOT EXISTS `etudiant` (
  `email` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `nom` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `prenom` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `telephone` varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `motDePasse` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `type` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `est_actif` tinyint(1) NOT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  `empreinteHash` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `etudiant`
--

INSERT INTO `etudiant` (`email`, `nom`, `prenom`, `telephone`, `motDePasse`, `type`, `est_actif`, `id`, `empreinteHash`) VALUES
('koopa.iggy@gmail.com', 'Koopa', 'Iggy', '0690020525', 'IggyZeKoopa#02', 'STUDENT', 1, 1, ''),
('test@gmail.com', 'Test', 'Today', '0690123456', '123456789', 'STUDENT', 1, 2, ''),
('rip.ty@gmail.com', 'Rippon', 'Tyrick', '0690552525', 'Iggy2', 'ADMIN', 1, 3, ''),
('morton.koopa@gmail.com', 'Morton Jr.', 'Koopa', '0690000000', 'MortonIsCool', 'STUDENT', 1, 4, '');

-- --------------------------------------------------------

--
-- Structure de la table `reservation`
--

DROP TABLE IF EXISTS `reservation`;
CREATE TABLE IF NOT EXISTS `reservation` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_trajet` int NOT NULL,
  `date_reservation` date NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_resa_trajet` (`id_trajet`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `reservation`
--

INSERT INTO `reservation` (`id`, `id_trajet`, `date_reservation`) VALUES
(1, 1, '2026-10-05'),
(2, 1, '2026-10-05'),
(3, 2, '2026-10-06'),
(4, 2, '2026-10-06'),
(5, 3, '2026-10-07'),
(6, 4, '2026-10-08'),
(7, 4, '2026-06-01'),
(8, 5, '2026-06-01'),
(9, 4, '2026-10-15'),
(10, 6, '2026-08-26'),
(11, 6, '2026-08-26');

-- --------------------------------------------------------

--
-- Structure de la table `trajet`
--

DROP TABLE IF EXISTS `trajet`;
CREATE TABLE IF NOT EXISTS `trajet` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ville_depart` varchar(80) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `ville_arrivee` varchar(80) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `date_trajet` date NOT NULL,
  `heure_depart` time NOT NULL,
  `nb_places` int NOT NULL,
  `id_conducteur` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_trajet_conducteur` (`id_conducteur`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `trajet`
--

INSERT INTO `trajet` (`id`, `ville_depart`, `ville_arrivee`, `date_trajet`, `heure_depart`, `nb_places`, `id_conducteur`) VALUES
(1, 'Lamentin', 'LGT Baimbridge', '2026-10-12', '07:15:00', 3, 1),
(2, 'Goyave', 'LGT Baimbridge', '2026-10-12', '07:00:00', 2, 4),
(3, 'LGT Baimbridge', 'Lamentin', '2026-10-12', '17:15:00', 3, 1),
(4, 'Le Moule', 'LGT Baimbridge', '2026-10-26', '07:30:00', 2, 5),
(5, 'Baillif', 'LGT Baimbridge', '2026-10-27', '07:45:00', 3, 6),
(6, 'Basse-Terre', 'LGT Baimbridge', '2026-11-08', '20:20:00', 6, 2),
(7, 'Ste-Rose', 'LGT Baimbridge', '2026-11-30', '06:00:00', 3, 8),
(8, 'Morne-à-l\'eau', 'LGT Baimbridge', '2026-11-30', '06:30:00', 1, 6);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
