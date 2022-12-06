SELECT m.category, m.max_price, p.product_name
FROM FOOD_PRODUCT as p
         JOIN
     (SELECT CATEGORY, MAX(price) as MAX_PRICE
      FROM FOOD_PRODUCT
      GROUP BY CATEGORY
      HAVING CATEGORY IN ('과자', '국', '김치', '식용유')) as m
     ON p.category = m.category AND p.price = m.max_price
ORDER BY MAX_PRICE DESC