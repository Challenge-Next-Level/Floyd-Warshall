SELECT
  Region,
  SUM(case when category = 'Furniture' then orders end) 'Furniture',
  SUM(case when category = 'Office Supplies' then orders end) 'Office Supplies',
  SUM(case when category = 'Technology' then orders end) 'Technology'
FROM
  (SELECT region Region, category, COUNT(DISTINCT order_id) orders
   FROM records
   GROUP BY region, category)
GROUP BY region
ORDER BY region;