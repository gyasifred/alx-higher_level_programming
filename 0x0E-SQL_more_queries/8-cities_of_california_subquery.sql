-- Use the specified database
USE hbtn_0d_usa;

-- Query to list cities of California without using JOIN
SELECT id, name
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;

