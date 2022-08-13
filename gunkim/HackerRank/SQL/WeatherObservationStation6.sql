-- 모음(a,e,i,o,u)으로 시작하는 도시
-- 도시 이름 첫 글자를 SUBSTR로 자르는게 핵심
-- 추가) REGEXP_LIKE 라는 함수도 편리해서 쓰기 좋음
SELECT DISTINCT(CITY) FROM STATION
WHERE LOWER(SUBSTR(CITY,1,1)) IN ('a','e','i','o','u');