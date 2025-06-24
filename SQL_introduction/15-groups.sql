-- script qui répertorie le nombre d'enregistrement ayant le même score dans la table second_table
-- Sélectionne deux colonnes : score, et le nombre d’occurrences de chaque score
SELECT score, COUNT(*) AS number

-- Indique que tu veux regrouper les lignes ayant le même score
FROM second_table
GROUP BY score

ORDER BY number DESC;

