-- id 값이 짝수인 것, 중복 결과는 제외
SELECT DISTINCT(city) FROM STATION
WHERE MOD(id, 2) = 0;