-- 모음(aeiou)으로 시작하고 끝나는 도시 이름 조회
SELECT DISTINCT(city) FROM STATION
WHERE REGEXP_LIKE(LOWER(city), '^[aeiou]')
AND REGEXP_LIKE(LOWER(city), '[aeiou]$');