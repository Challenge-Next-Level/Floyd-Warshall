-- 시간대별로 입양이 몇 건 발생했는지 조회
-- TO_CHAR 사용
SELECT HOUR, COUNT(*)
  FROM (SELECT TO_CHAR(ao.datetime, 'HH24') HOUR FROM animal_outs ao)
 GROUP BY HOUR
HAVING HOUR BETWEEN '09' AND '19'
 ORDER BY HOUR