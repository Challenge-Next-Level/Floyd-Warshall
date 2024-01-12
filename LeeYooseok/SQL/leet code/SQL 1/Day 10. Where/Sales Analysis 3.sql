SELECT s.product_id as product_id, p.product_name as product_name
FROM Sales as s, Product as p
WHERE s.product_id = p.product_id
GROUP BY s.product_id
HAVING '2019-2024-01-2024-01' <= MIN(s.sale_date) and MAX(s.sale_date) <= '2019-03-31'