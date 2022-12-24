SELECT B.author_id, A.author_name,B.category,SUM(BS.sales*B.price) AS TOTAL_SALES
FROM BOOK B, BOOK_SALES BS, AUTHOR A
WHERE B.book_id = BS.book_id AND B.author_id = A.author_id AND BS.sales_date LIKE '2022-01%'
GROUP BY B.author_id,B.category
ORDER BY B.author_id,B.category DESC