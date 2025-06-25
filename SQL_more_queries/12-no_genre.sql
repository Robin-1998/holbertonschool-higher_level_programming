-- Script qui liste toutes les émissions contenus dans hbtn_0d_tvshows sans genre lié
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
-- va rassembler tous les enregistrements de tv_shows et les enregistrements
-- correspondant de tv_show_genres
WHERE tv_show_genres.genre_id IS NULL
-- permet de filtrer uniquement les shows(film) dont le genre n'est pas lié
ORDER BY tv_shows.title, tv_show_genres.genre_id;
