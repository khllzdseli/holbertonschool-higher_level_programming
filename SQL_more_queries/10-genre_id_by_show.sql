-- 10. Genre ID by show
-- List all shows that have at least one genre linked
-- Format: tv_shows.title - tv_show_genres.genre_id
-- Results sorted by tv_shows.title and tv_show_genres.genre_id in ascending order

SELECT t.title, g.genre_id
FROM tv_shows t
JOIN tv_show_genres g ON t.id = g.tv_show_id
ORDER BY t.title ASC, g.genre_id ASC;
