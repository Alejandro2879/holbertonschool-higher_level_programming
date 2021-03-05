-- Script import data from a database
SELECT city, AVG(value) AS 'avg_temp'
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
