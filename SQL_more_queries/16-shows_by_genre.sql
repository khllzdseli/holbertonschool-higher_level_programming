SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_shows_genres
    ON tv_shows.id = tv_shows_genres.tv_show_id
LEFT JOIN tv_genres
    ON tv_shows_genres.tv_genre_id = tv_genres.id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;
