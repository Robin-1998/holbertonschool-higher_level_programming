-- Sript qui écrit une table unique_id dans mon serveur MySQL
CREATE TABLE IF NOT EXISTS unique_id(
	id INT DEFAULT 1,
	name VARCHAR(256),
	UNIQUE (id)
)
-- En SQL, la contrainte UNIQUE (ou UNIQUE constraint) sert à garantir que toutes les valeurs d'une colonne (ou d’un groupe de colonnes) sont uniques, c’est-à-dire sans doublons.
