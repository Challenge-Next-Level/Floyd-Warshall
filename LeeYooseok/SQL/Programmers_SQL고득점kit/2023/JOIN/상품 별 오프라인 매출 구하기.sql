SELECT p.product_code, (p.price * o.total_amounts) as sales
FROM product p,
     (SELECT product_id, SUM(sales_amount) as total_amounts
      FROM offline_sale
      GROUP BY product_id) o
WHERE p.product_id = o.product_id
ORDER BY sales DESC, product_code