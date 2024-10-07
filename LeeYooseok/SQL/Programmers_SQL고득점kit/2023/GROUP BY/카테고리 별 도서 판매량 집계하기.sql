SELECT b.category, SUM(s.sales) as total_sales
FROM book_sales s JOIN book b ON s.book_id = b.book_id
WHERE s.sales_date LIKE '2022-2024-01%'
GROUP BY b.category
ORDER BY category
