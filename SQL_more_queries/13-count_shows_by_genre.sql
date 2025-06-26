-- Sript qui liste tous les genre de hbtn_0d_tvshows et affiche le nombre de spectacles (shows) liés à chacun d'eux
-- Script sans alias de table
SELECT tv_genres.name AS genre, COUNT(*) AS tv_shows
FROM tv_show_genres
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
GROUP BY tv_genres.name
ORDER BY tv_shows DESC;

-- Script avec les alias de table
-- SELECT film.name AS genre, COUNT(*) AS tv_shows
-- Après SELECT on utilise un alias de table, lors de l'utilisation d'un SELECT il faut un nom devant la colonne à utiliser de la table pour pouvoir ensuite l'utiliser
-- COUNT permet de compter le nombre total de film et le mot AS permet de retourner le compteur tv_shows plutôt qu'un COUNT
-- FROM tv_show_genres AS sg
-- lors de l'utilisation de FROM, l'alias de table est différent lors de son utilisation
-- JOIN tv_genres film ON sg.genre_id = film.id
-- On associe chaque émission à son genre en reliant sg.genre_id à film.id (tv_genres)
-- GROUP BY film.name
-- On retourne les valeurs de chaque film
-- ORDER BY tv_shows DESC;
-- les résultats sont triés par ordre décroissant du nombre de spectacle 


