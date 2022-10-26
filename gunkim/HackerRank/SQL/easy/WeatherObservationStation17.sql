-- 조건절에 ROWNUM = 1를 쓰고 싶은데 하나의 쿼리문으로 해결되지 않으니 서브쿼리로 테이블 생성 후 사용을 한다.
SELECT *
FROM (
    SELECT ROUND(long_w,4)
    FROM STATION
    WHERE lat_n > 38.7780
    ORDER BY lat_n)
WHERE ROWNUM = 1;