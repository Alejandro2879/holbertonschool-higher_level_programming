-- Script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
-- 1) Each record should display: <TV Show genre> - <Number of shows linked to this genre>
-- 2) First column must be called genre
-- 3) Second column must be called number_of_shows
-- 4) Don’t display a genre that doesn’t have any shows linked
-- 5) Results must be sorted in descending order by the number of shows linked
-- 6) You can use only one SELECT statement
-- 7) The database name will be passed as an argument of the mysql command
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.genre_id) AS number_of_shows
FROM tv_genres
INNER JOIN tv_show_genres
ON tv_genres.id=tv_show_genres.genre_id
GROUP BY tv_show_genres.genre_id
ORDER BY number_of_shows DESC;
