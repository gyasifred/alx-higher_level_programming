-- Select the state and the maximum temperature value for each state
SELECT state, MAX(value) AS max_temp

-- From the 'temperatures' table
FROM temperatures

-- Group the results by state
GROUP BY state

-- Order the result by state
ORDER BY state;

