-- 코드를 입력하세요
SELECT  o.user_id, o.product_id
FROM ONLINE_SALE o
GROUP BY o.user_id, o.product_id
HAVING COUNT(*) >= 2
ORDER BY o.user_id, o.product_id DESC