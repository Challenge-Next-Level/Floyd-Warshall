SELECT f.flavor FROM FIRST_HALF f, ICECREAM_INFO i
WHERE f.flavor = i.flavor AND i.ingredient_type = 'fruit_based' AND f.total_order > 3000
ORDER BY f.total_order DESC;