-- Lists all cities contained in the database hbtn_0d_usa.
SELECT id, name FROM cities
WHERE name IN
      (SELECT name FROM states)
ORDER BY id;
