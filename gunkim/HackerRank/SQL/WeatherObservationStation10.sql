-- 모음(aeiou)으로 끝나지 않는 도시 조회
SELECT DISTINCT(city) FROM STATION
WHERE REGEXP_LIKE(LOWER(city), '[^aeiou]$');