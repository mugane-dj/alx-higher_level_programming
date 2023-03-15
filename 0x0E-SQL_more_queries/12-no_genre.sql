-- Lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
SELECT a.title, b.genre_id
  FROM tv_shows AS a
       LEFT JOIN tv_show_genres AS b
       ON a.id = b.show_id
       WHERE b.genre_id IS NULL
ORDER BY a.title, b.genre_id; 
