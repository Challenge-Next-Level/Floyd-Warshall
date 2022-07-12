-- 0~23시에 시간대별 입양 건수 조회
-- LEVEL, JOIN 사용
SELECT HOUR, COUNT(ao.datetime)
  FROM (SELECT LEVEL - 1 HOUR FROM DUAL CONNECT BY LEVEL <= 24) HR
  LEFT JOIN animal_outs ao
    ON HR.HOUR = TO_CHAR(ao.datetime, 'HH24')
 GROUP BY HOUR
 ORDER BY HOUR