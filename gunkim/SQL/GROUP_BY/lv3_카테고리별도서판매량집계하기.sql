SELECT B.category, SUM(BS.sales) AS TOTAL_SALES
FROM BOOK_SALES BS
INNER JOIN BOOK B
ON B.book_id = bs.book_id
WHERE BS.sales_date LIKE '2022-2024-01%'
GROUP BY B.category
ORDER BY B.category