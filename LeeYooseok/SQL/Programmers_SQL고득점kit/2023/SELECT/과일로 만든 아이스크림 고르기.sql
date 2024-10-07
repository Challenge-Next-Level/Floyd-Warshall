-- 코드를 입력하세요
SELECT f.flavor
FROM FIRST_HALF f, ICECREAM_INFO i
WHERE f.flavor = i.flavor and i.ingredient_type = 'fruit_based' and f.total_order > 3000
ORDER BY f.total_order DESC