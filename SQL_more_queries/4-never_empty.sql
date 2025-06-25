-- Script qui créé une table id_not_null sur mon serveur MySQL
CREATE TABLE IF NOT EXISTS id_not_null(
	id INT DEFAULT 1,
	name VARCHAR(256)
);
