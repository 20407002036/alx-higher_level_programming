-- Script to list all records with a name value in the second_table of hbtn_0c_0 database, ordered by descending score
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
