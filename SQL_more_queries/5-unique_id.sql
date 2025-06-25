-- Sript qui écrit une table unique_id dans mon serveur MySQL
CREATE TABLE IF NOT EXISTS unique_id(
	id INT DEFAULT 1,
	name VARCHAR(256),
	UNIQUE (id)
)
