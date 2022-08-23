-- 모음(aeiou)으로 시작하지 않고 끝나지 않는 도시 조회
SELECT DISTINCT(city) FROM STATION
WHERE REGEXP_LIKE(LOWER(city), '^[^aeiou]')
AND REGEXP_LIKE(LOWER(city), '[^aeiou]$');