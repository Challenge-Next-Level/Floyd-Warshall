SELECT weather.id AS 'Id'
FROM weather
JOIN weather before_weather
ON DATEDIFF(weather.recordDate, before_weather.recordDate) = 1
AND weather.Temperature > before_weather.Temperature
;