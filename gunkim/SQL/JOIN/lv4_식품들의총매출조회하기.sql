SELECT FP.product_id, FP.product_name, SUM(FP.price * FO.amount) AS TOTAL_SALES
FROM FOOD_PRODUCT FP
INNER JOIN FOOD_ORDER FO
ON FP.product_id = FO.product_id
WHERE FO.produce_date LIKE '2022-05%'
GROUP BY FP.product_id, FP.product_name
ORDER BY SUM(FP.price * FO.amount) DESC, FP.product_id