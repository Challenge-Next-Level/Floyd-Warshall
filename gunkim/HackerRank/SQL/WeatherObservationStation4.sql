-- (총 도시의 수 - 중복을 제외한 도시의 수) 의 값은?
SELECT COUNT(*) - COUNT(DISTINCT(city)) FROM STATION;