-- List all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
-- List all Comedy shows in the database hbtn_0d_tvshows.
SELECT a.title, c.name
  FROM tv_shows AS a
       LEFT JOIN tv_show_genres AS b
       ON a.id = b.show_id

       LEFT JOIN tv_genres AS c
       ON c.id = b.genre_id
ORDER BY a.title, c.name
