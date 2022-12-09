SELECT warehouse_id,warehouse_name,address,IFNULL(freezer_yn,'N')
FROM FOOD_WAREHOUSE
WHERE address LIKE '경기도%'
ORDER BY warehouse_id