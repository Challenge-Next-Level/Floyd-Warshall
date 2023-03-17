-- SQLite는 나눗셈을 하면 '정수' 값이 나온다고 한다. 따라서 +0.00 을 통해 double형을 만들어줘야 한다.
SELECT order_date
      ,count(distinct CASE WHEN category = "Furniture" THEN order_id END) as "furniture"
      ,round(count(distinct CASE WHEN category = "Furniture" THEN order_id END)/(count(distinct order_id)+0.00)*100,2) as furniture_pct
FROM records
GROUP BY order_date
HAVING COUNT(distinct order_id) >= 10
      AND furniture_pct >= 40
ORDER BY furniture_pct desc, order_date