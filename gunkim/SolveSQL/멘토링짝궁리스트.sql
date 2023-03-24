SELECT TE.EMPLOYEE_ID  AS "mentee_id"
         , TE.NAME         AS "mentee_name"
         , MTO.EMPLOYEE_ID AS "mentor_id"
         , MTO.NAME        AS "mentor_name"
FROM (
        SELECT EMPLOYEE_ID
             , NAME
             , JOIN_DATE
             , DEPARTMENT
          FROM EMPLOYEES
          WHERE STRFTIME('%Y%m%d', JOIN_DATE) BETWEEN '20210901' AND '20211231'
      ) TE
INNER JOIN EMPLOYEES MTO
ON TE.DEPARTMENT != MTO.DEPARTMENT
WHERE STRFTIME('%Y%m%d', MTO.JOIN_DATE) <= '20191231'
ORDER BY "mentee_id", "mentor_id"
;