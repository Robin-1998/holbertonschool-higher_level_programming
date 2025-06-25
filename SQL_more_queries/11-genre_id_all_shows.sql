-- Script qui répertorie toutes les émissions contenues dans la base de donnée hbtn_0d_tvshows
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
-- jointure entre deux tables en retournant toutes les lignes de la table de gauche
-- celle qui est mentionné par LEFT JOINT+ (tv_show_genre)
-- Si une ligne n'a pas de correspondance dans la table de droite, les colonnes de la
-- table de droite seront remplies avec des NULL
