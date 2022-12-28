SELECT order_id,product_id,DATE_FORMAT(out_date,'%Y-%m-%d'),
    CASE
    WHEN out_date <= DATE('2022-05-01')
    THEN '출고완료'
    WHEN out_date > DATE('2022-05-01')
    THEN '출고대기'
    ELSE '출고미정'
    END
FROM FOOD_ORDER
ORDER BY order_id