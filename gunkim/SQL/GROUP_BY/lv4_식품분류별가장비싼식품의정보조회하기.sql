-- RANK()로 partition by, order by 사용하기
SELECT category,price MAX_PRICE,product_name
FROM (
    SELECT *, RANK() OVER(PARTITION BY CATEGORY ORDER BY PRICE DESC) PRICE_RANK
    FROM FOOD_PRODUCT
    WHERE CATEGORY IN ('과자', '국', '김치', '식용유')
) RANKED_PRODUCT
WHERE RANKED_PRODUCT.PRICE_RANK = 1
ORDER BY MAX_PRICE DESC