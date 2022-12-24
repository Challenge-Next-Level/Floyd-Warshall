SELECT
    YEAR(OS.sales_date) AS YEAR,
    MONTH(OS.sales_date) AS MONTH,
    COUNT(DISTINCT OS.user_id),
    ROUND(COUNT(DISTINCT OS.user_id)/(SELECT COUNT(USER_ID)
                                     FROM USER_INFO
                                     WHERE YEAR(USER_INFO.joined) = 2021)
         ,1)
FROM ONLINE_SALE OS
INNER JOIN USER_INFO UI
ON UI.user_id = OS.user_id
WHERE YEAR(UI.joined) = 2021
GROUP BY YEAR, MONTH
ORDER BY YEAR, MONTH