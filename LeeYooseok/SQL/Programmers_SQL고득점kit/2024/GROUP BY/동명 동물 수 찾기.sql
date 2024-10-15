SELECT NAME, COUNT(*) AS COUNT
FROM ANIMAL_INS
GROUP BY NAME
HAVING COUNT(*) >= 2
ORDER BY NAME