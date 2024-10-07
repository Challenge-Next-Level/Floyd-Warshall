SELECT LEFT(product_code, 2) as category, COUNT(*)
FROM product
GROUP BY category
ORDER BY category