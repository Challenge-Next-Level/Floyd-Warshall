SELECT p.product_id, p.product_name, o.total_orders * p.price as total_sales
FROM food_product as p,
     (SELECT product_id, SUM(amount) as total_orders
      FROM food_order
      WHERE produce_date LIKE '2022-05%'
      GROUP BY product_id) as o
WHERE p.product_id = o.product_id
ORDER BY total_sales DESC, p.product_id