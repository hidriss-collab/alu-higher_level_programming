-- Counts records for each score
-- Ordered by number descending

SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
