SELECT YEAR(sales_date) as year, MONTH(sales_date) as month, COUNT(DISTINCT o.user_id) as puchased_users, ROUND(COUNT(DISTINCT o.user_id) / (SELECT COUNT(*) FROM user_info WHERE joined LIKE '2021%'), 1) as purchased_ratio
FROM online_sale as o JOIN user_info as i ON o.user_id = i.user_id
WHERE i.joined LIKE '2021%'
GROUP BY YEAR(sales_date), MONTH(sales_date)
ORDER BY year, month