-- Script import data from a database
SELECT city, AVG(value) 'av_temp'
FROM temperatures
GROUP BY city
ORDER BY av_temp DESC;
