SELECT (price - price%10000) as price_group, count(*) as products
FROM product
GROUP BY price_group
ORDER BY price_group