-- displays the avg temp by city in desc
SELECT city, AVG(value) as avg_temp FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
