-- 모음(aeiou)로 끝나는 도시 조회
-- REGEXP_LIKE가 많이 편리함. 다양한 기능이 있음
SELECT DISTINCT(city) FROM STATION
WHERE REGEXP_LIKE(city, '[aeiou]$');