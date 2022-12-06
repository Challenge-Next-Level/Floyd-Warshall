SELECT ingredient_type, SUM(total_order) total_order
FROM first_half f JOIN icecream_info i
                       ON f.flavor = i.flavor
GROUP BY ingredient_type
ORDER BY total_order
