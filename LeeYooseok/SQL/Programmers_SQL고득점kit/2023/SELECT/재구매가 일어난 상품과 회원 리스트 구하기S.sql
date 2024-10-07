SELECT o.user_id, o.product_id
FROM online_sale o
GROUP BY o.user_id, o.product_id
HAVING COUNT(*) >= 2
ORDER BY o.user_id ASC, o.product_id DESC