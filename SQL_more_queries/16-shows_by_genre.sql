-- Script qui liste tout les film et tous les genres liés à ces émissions, à partir de la base de données hbtn_0d_tvshows
SELECT t.title, g.name
FROM tv_shows AS t
LEFT JOIN tv_show_genres AS tsg ON t.id = tsg.show_id
LEFT JOIN tv_genres AS g ON tsg.genre_id = g.id
ORDER BY t.title, g.name;
-- alias de table de t correspond à la table tv_show donc title + id
-- alias de table de g correspond à la table tv_genres et le nom avec aussi son propre id

