# user_id 중복이 있을 수 있으므로
SELECT o.year, o.month, u.gender, COUNT(DISTINCT(u.user_id)) as 'USERS'
FROM
    user_info as u,
    (SELECT YEAR(sales_date) year, MONTH(sales_date) month, user_id
     FROM online_sale) as o
WHERE u.user_id = o.user_id AND u.gender IS NOT NULL
GROUP BY o.year, o.month, u.gender
ORDER BY o.year, o.month, u.gender