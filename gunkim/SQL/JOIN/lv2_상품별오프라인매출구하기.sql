SELECT P.product_code, SUM(P.price * OS.sales_amount) AS SALES
FROM PRODUCT P
INNER JOIN OFFLINE_SALE OS
ON P.product_id = OS.product_id
GROUP BY P.product_code
ORDER BY SUM(P.price * OS.sales_amount) DESC, P.product_code ASC