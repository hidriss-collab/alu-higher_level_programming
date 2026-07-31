-- Lists records with a valid name
-- Ordered by score descending

SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
