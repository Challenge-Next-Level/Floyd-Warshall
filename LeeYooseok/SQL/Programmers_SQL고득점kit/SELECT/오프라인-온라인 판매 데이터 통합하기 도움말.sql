SELECT *
FROM
    (SELECT DATE_FORMAT(sales_date, '%Y-%m-%d') as sales_date, product_id, NULL as user_id, sales_amount
     FROM offline_sale
     UNION
     SELECT DATE_FORMAT(sales_date, '%Y-%m-%d') as sales_date, product_id, user_id, sales_amount
     FROM online_sale) as t
WHERE YEAR(t.sales_date) = 2022 AND MONTH(t.sales_date) = 03
ORDER BY sales_date, product_id, user_id