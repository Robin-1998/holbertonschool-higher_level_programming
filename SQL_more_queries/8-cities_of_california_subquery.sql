-- Scripts qui liste toutes les villes de Californie qui sont trouvés dans la base de donnée
SELECT id, name
-- on séléctionne les deux records qui nous intéresse
FROM cities
-- on affiche les villes et non l'état de Californie. Donc la table que l'on veux interroger, c'est cities
WHERE state_id=(
	SELECT id FROM states WHERE name = 'California'
)
-- On va chercher l'ID de l'état de la californie dans la table states où le nom est California
ORDER BY id ASC;
-- On trie les résultats deu plus petits au plus grand
