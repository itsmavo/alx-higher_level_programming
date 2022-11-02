-- lists all genres not associated with the show
-- uses a db to list all rows not linked to one row
SELECT name
FROM tv_genres
WHERE name NOT IN
(SELECT name
FROM tv_genres
LEFT JOIN tv_show_genres on tv_genres.id = tv_show_genres.genre_id
LEFT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter')
GROUP BY name
ORDER BY name ASC;
