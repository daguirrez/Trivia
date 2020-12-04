DROP DATABASE IF EXISTS `trivia_test`;
CREATE DATABASE IF NOT EXISTS `trivia_test`;
USE `trivia_test`;

DROP TABLE IF EXISTS `categories`;
CREATE TABLE IF NOT EXISTS `categories` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

DELETE FROM `categories`;
INSERT INTO `categories` (`id`, `name`) VALUES (1, 'General Knowledge');
INSERT INTO `categories` (`id`, `name`) VALUES (2, 'Books');
INSERT INTO `categories` (`id`, `name`) VALUES (3, 'Film');
INSERT INTO `categories` (`id`, `name`) VALUES (4, 'Music');
INSERT INTO `categories` (`id`, `name`) VALUES (5, 'Video Games');
INSERT INTO `categories` (`id`, `name`) VALUES (6, 'Celebrities');
INSERT INTO `categories` (`id`, `name`) VALUES (7, 'Animals');
INSERT INTO `categories` (`id`, `name`) VALUES (8, 'Comics');
INSERT INTO `categories` (`id`, `name`) VALUES (9, 'Anime & Manga');
INSERT INTO `categories` (`id`, `name`) VALUES (10, 'Cartoon');

DROP TABLE IF EXISTS `players`;
CREATE TABLE IF NOT EXISTS `players` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(3) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

DELETE FROM `players`;
INSERT INTO `players` (`id`, `name`) VALUES (1, 'DAN');
INSERT INTO `players` (`id`, `name`) VALUES (2, 'DAV');

DROP TABLE IF EXISTS `matches`;
CREATE TABLE IF NOT EXISTS `matches` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `duration` int(11) NOT NULL,
  `score` int(11) NOT NULL,
  `id_player` int(11) NOT NULL,
  `id_category` int(11) NOT NULL,
  `difficulty` enum('EASY','MEDIUM','HARD') NOT NULL DEFAULT 'MEDIUM',
  PRIMARY KEY (`id`),
  KEY `FK_matches_players` (`id_player`),
  KEY `FK_matches_categories` (`id_category`),
  CONSTRAINT `FK_matches_categories` FOREIGN KEY (`id_category`) REFERENCES `categories` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `FK_matches_players` FOREIGN KEY (`id_player`) REFERENCES `players` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

DELETE FROM `matches`;
INSERT INTO `matches` (`id`, `duration`, `score`, `id_player`, `id_category`, `difficulty`) VALUES (1, 95, 5, 1, 1, 'MEDIUM');
INSERT INTO `matches` (`id`, `duration`, `score`, `id_player`, `id_category`, `difficulty`) VALUES (2, 0, 3, 2, 1, 'EASY');
INSERT INTO `matches` (`id`, `duration`, `score`, `id_player`, `id_category`, `difficulty`) VALUES (3, 0, 5, 1, 1, 'MEDIUM');
INSERT INTO `matches` (`id`, `duration`, `score`, `id_player`, `id_category`, `difficulty`) VALUES (4, 0, 2, 1, 9, 'EASY');
INSERT INTO `matches` (`id`, `duration`, `score`, `id_player`, `id_category`, `difficulty`) VALUES (5, 93, 4, 2, 8, 'MEDIUM');