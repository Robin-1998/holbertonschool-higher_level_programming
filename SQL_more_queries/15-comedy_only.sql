-- Script qui liste tous les films de comédie dans la database hbtn_0d_tvshows
SELECT t.title
FROM tv_shows as t
JOIN tv_show_genres AS sg ON t.id = sg.show_id
JOIN tv_genres AS g ON g.id = sg.genre_id
WHERE g.name = 'Comedy'
ORDER BY t.title ASC;
