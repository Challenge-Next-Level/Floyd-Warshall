SELECT S.YEAR, S.MONTH, U.GENDER, COUNT(DISTINCT(U.USER_ID)) AS USERS
FROM USER_INFO AS U,
(SELECT USER_ID, YEAR(SALES_DATE) AS YEAR, MONTH(SALES_DATE) AS MONTH
FROM ONLINE_SALE) AS S
WHERE U.USER_ID = S.USER_ID AND U.GENDER IS NOT NULL
GROUP BY S.YEAR, S.MONTH, U.GENDER
ORDER BY S.YEAR, S.MONTH, U.GENDER