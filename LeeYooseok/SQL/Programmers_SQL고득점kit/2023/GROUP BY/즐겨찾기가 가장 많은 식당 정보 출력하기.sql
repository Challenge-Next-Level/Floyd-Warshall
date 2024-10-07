SELECT i.food_type, i.rest_id, i.rest_name, i.favorites
FROM
    rest_info i
        JOIN
    (SELECT food_type, MAX(favorites) as favorites
     FROM rest_info
     GROUP BY food_type) f
    ON i.food_type = f.food_type AND i.favorites = f.favorites
ORDER BY food_type DESC