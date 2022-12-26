SELECT a.author_id, author_name, category, SUM(s.sum_sales * b.price) as total_sales
FROM author a, book b,
     (SELECT book_id, SUM(sales) as sum_sales
      FROM book_sales
      WHERE sales_date LIKE '2022-01%'
      GROUP BY book_id) as s
WHERE b.book_id = s.book_id and b.author_id = a.author_id
GROUP BY a.author_id, category
ORDER BY author_id , category desc