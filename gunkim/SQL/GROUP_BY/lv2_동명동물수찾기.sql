-- 동물 이름이 두 번 이상 쓰인 이름 조회
-- HAVING 사용
SELECT ai.name, COUNT(ai.name) FROM animal_ins ai
GROUP BY ai.name
HAVING COUNT(ai.name) >= 2
ORDER BY ai.name