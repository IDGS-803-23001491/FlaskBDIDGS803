/*
MySQL Backup
Database: bdidgs803
Backup Time: 2026-02-26 20:49:19
*/

SET FOREIGN_KEY_CHECKS=0;
DROP TABLE IF EXISTS `bdidgs803`.`alembic_version`;
DROP TABLE IF EXISTS `bdidgs803`.`alumnos`;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
CREATE TABLE `alumnos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `email` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `creates_date` datetime DEFAULT NULL,
  `apellidos` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `telefono` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
BEGIN;
LOCK TABLES `bdidgs803`.`alembic_version` WRITE;
DELETE FROM `bdidgs803`.`alembic_version`;
INSERT INTO `bdidgs803`.`alembic_version` (`version_num`) VALUES ('f245d38a89f9')
;
UNLOCK TABLES;
COMMIT;
BEGIN;
LOCK TABLES `bdidgs803`.`alumnos` WRITE;
DELETE FROM `bdidgs803`.`alumnos`;
INSERT INTO `bdidgs803`.`alumnos` (`id`,`nombre`,`email`,`creates_date`,`apellidos`,`telefono`) VALUES (1, 'Juan', 'juan@gmail.com', '2026-02-26 20:46:39', 'Pérez Lopez', '4778942768'),(2, 'Damian', 'damian@gmail.com', '2026-02-26 20:47:14', 'Rodríguez Alarcón', '4776879923'),(3, 'Pablo', 'pablo@gmail.com', '2026-02-26 20:47:45', 'Pérez Landa', '4776890263'),(4, 'Jose', 'jose@gmail.com', '2026-02-26 20:48:14', 'Juárez Jaramillo', '4772638490'),(5, 'Carlos', 'carlos@gmail.com', '2026-02-26 20:48:37', 'Rizo Mendoza', '4770298317')
;
UNLOCK TABLES;
COMMIT;
