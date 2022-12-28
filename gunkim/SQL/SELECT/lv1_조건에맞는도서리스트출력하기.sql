SELECT book_id, DATE_FORMAT(published_date,'%Y-%m-%d')
FROM BOOK
WHERE category = '인문' AND published_date LIKE '2021%'
ORDER BY published_date