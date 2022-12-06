-- RANK() OVER 익숙해지기
SELECT FOOD_TYPE,REST_ID,REST_NAME,FAVORITES
FROM (
    SELECT *, RANK() OVER(PARTITION BY FOOD_TYPE ORDER BY FAVORITES DESC) FAVOR_RANK
    FROM REST_INFO
) FOOD_RANK
WHERE FOOD_RANK.FAVOR_RANK = 1
ORDER BY FOOD_TYPE DESC