-- Listabll shows contained in hbtn_0d_tvshows that have at least one genre linked.
SELECT a.title, b.genre_id
  FROM tv_shows AS a
       INNER JOIN tv_show_genres as b
       ON a.id = b.show_id
ORDER BY a.title, b.genre_id 
