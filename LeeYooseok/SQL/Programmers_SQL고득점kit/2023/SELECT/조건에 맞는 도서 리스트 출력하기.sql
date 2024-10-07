SELECT book_id, DATE_FORMAT(published_date, '%Y-%m-%d') published_date
FROM book
WHERE published_date LIKE '2021%' AND CATEGORY = '인문'
ORDER BY published_date