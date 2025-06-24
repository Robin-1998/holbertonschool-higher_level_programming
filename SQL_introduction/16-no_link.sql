-- script qui répertorie tous les enregistrements de la table second_table
SELECT score, name
-- on récupère les deux colonnes qui nous intéresse
FROM second_table
WHERE name != ""
-- Cette condition filtre les lignes pour ne conserver que celles où la colonne name n'est pas vide
ORDER BY score DESC;
-- et trie les résultats de score par ordre décroissant
