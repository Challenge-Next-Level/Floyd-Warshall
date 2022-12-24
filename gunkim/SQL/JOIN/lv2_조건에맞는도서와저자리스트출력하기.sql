SELECT b.book_id, a.author_name, date_format(b.published_date,'%Y-%m-%d')
FROM BOOK b
INNER JOIN AUTHOR a
ON a.author_id = b.author_id
WHERE b.category = '경제'
ORDER BY b.published_date