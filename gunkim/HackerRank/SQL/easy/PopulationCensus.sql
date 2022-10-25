SELECT SUM(CITY.population) FROM CITY
JOIN COUNTRY
ON CITY.countrycode = COUNTRY.code
WHERE COUNTRY.continent = 'Asia';