-- Select the city and average temperature value for the months between July and August
SELECT city, AVG(value) AS avg_temp

-- From the 'temperatures' table
FROM temperatures

-- Where the month is between July (7) and August (8)
WHERE month BETWEEN 7 AND 8

-- Group the results by city
GROUP BY city

-- Order the result by average temperature value in descending order
ORDER BY avg_temp DESC

-- Limit the result to the top 3 cities with the highest average temperature
LIMIT 3;

