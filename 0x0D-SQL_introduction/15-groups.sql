-- Lists the number of records with the same score in the table.
SELECT score, COUNT(score) as `number` FROM second_table 
GROUP BY score HAVING COUNT(score) > 1;
ALTER TABLE second_table ADD `number` int;
SELECT score, `number` FROM second_table ORDER BY `number` DESC;
