-- 급여*월 계산된 테이블을 먼저 만든 뒤 조인해서 해당 1행을 가져오기
SELECT *
FROM
    (SELECT MAX(MONTHS*SALARY), COUNT(EMPLOYEE_ID)
    FROM EMPLOYEE
    GROUP BY MONTHS*SALARY
    ORDER BY MONTHS*SALARY DESC)
WHERE ROWNUM = 1;