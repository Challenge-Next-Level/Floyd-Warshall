-- 도시 이름이 가장 짧은 도시와 가장 긴 도시 하나씩 출력
-- 서로 다른 조건이라 각각의 테이블로 뽑아서 합쳐야 했음
SELECT *
FROM
    (SELECT city, LENGTH(city)
    FROM STATION
    ORDER BY LENGTH(city), city)
WHERE ROWNUM = 1
UNION
SELECT *
FROM
    (SELECT city, LENGTH(city)
    FROM STATION
    ORDER BY LENGTH(city) DESC, city)
WHERE ROWNUM = 1;