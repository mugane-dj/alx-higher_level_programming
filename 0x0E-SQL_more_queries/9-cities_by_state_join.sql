-- Lists all cities contained in the database hbtn_0d_usa.
SELECT a.id, a.name, b.name 
FROM cities a, states b
ORDER BY id;
