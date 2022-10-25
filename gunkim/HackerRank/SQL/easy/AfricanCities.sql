SELECT CITY.name FROM CITY
JOIN COUNTRY
ON CITY.countrycode = COUNTRY.code
WHERE COUNTRY.continent = 'Africa';