-- List the number of records with the same score
-- Display the score, the number of records for each score, and sort the result by the number of records (descending)

SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;

