SELECT DATE_FORMAT(ons.sales_date, '%Y-%m-%d') sd, product_id,user_id,sales_amount
FROM ONLINE_SALE ons
WHERE DATE_FORMAT(ons.sales_date, '%Y-%m-%d') LIKE '2022-03%'

UNION

SELECT DATE_FORMAT(ofs.sales_date, '%Y-%m-%d') sd, product_id,NULL,sales_amount
FROM OFFLINE_SALE ofs
WHERE DATE_FORMAT(ofs.sales_date, '%Y-%m-%d') LIKE '2022-03%'

ORDER BY sd, product_id, user_id