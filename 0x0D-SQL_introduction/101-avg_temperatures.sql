--Script
SELECT city, AVG(value) AS av_temp FROM temperatures GROUP BY city ORDER BY av_temp DESC;
