SELECT f1.x, f1.y
FROM Functions f1 JOIN Functions f2
    ON f1.x = f2.y and f1.y = f2.x
GROUP BY f1.x, f1.y
HAVING COUNT(f1.x) > 1 OR f1.x < f1.y
ORDER BY f1.x