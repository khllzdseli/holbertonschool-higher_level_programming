-- 10. Genre ID by show
-- List all shows that have at least one genre linked
-- Format: tv_shows.title - tv_show_genres.genre_id
-- Results sorted by tv_shows.title and tv_show_genres.genre_id in ascending order

SELECT tv.title, tg.genre_id
FROM tv_shows AS tv
JOIN tv_show_genres AS tg ON tv.id = tg.tv_show_id
ORDER BY tv.title ASC, tg.genre_id ASC;
