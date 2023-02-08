SELECT u.user_id as buyer_id, u.join_date as join_date, IFNULL(COUNT(o.order_id), 0) as orders_in_2019
FROM Users u LEFT JOIN Orders o ON u.user_id = o.buyer_id AND o.order_date LIKE '2019%'
GROUP BY u.user_id