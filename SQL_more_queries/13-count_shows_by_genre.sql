-- Import the database dump from hbtn_0d_tvshows
-- to your MySQL server: download (same as 12-no_genre.sql)
SELECT tv_genres.name AS genre,
COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id                                                        
GROUP BY tv_genres.name
HAVING number_of_shows > 0
ORDER BY number_of_shows DESC;
