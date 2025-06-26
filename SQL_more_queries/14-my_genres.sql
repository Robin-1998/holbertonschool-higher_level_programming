-- Script qui utilise la base de donnée hbtn_0d_tvshows et liste tous les genres de la série Dexter
SELECT g.name
-- On uitlise un alias de table (comme un variable) pour éviter des doublons et de rendre la requête plus claire
FROM tv_genres AS g
-- on utilise également un alias de table pour l'import de la table
JOIN tv_show_genres AS sg ON g.id = sg.genre_id
-- On relie chaque genre à ses entrées dans la table d'association tv_show_genres via genre_id
JOIN tv_shows AS s ON s.id = sg.show_id
-- Puis on relie ces associations aux shows correspondants en faisant correspondre show_id à l'id de tv_shows
WHERE s.title = 'Dexter'
-- on filtre le résultat pour avoir seulement le genre de la série demandé
ORDER BY g.name ASC;
