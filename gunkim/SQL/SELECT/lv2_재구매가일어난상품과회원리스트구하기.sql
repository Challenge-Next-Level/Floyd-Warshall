-- Having 절 생각이 나질 않았음
SELECT user_id, product_id FROM ONLINE_SALE
GROUP BY user_id, product_id
HAVING COUNT(sales_date) > 1
ORDER BY user_id ASC, product_id DESC;