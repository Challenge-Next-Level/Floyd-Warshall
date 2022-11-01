-- 내가 이해하고 생각하는 답, 하지만 오답이다. coins_needed에 대한 조건을 더 추가해야 함.
SELECT w.id, p.age, w.coins_needed, w.power FROM WANDS w
JOIN WANDS_PROPERTY p ON w.code = p.code
WHERE p.is_evil = 0
ORDER BY w.power DESC , p.age DESC ;