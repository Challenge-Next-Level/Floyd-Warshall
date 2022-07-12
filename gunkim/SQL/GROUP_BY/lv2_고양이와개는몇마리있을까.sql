-- 고양이와 개가 몇 마리인지 확인, (고양이 -> 개) 순으로 정렬
-- GROUP BY, ORDER BY 사용
SELECT ai.animal_type, COUNT(*) cnt FROM animal_ins ai
WHERE ai.animal_type in ('Cat', 'Dog')
GROUP BY ai.animal_type
ORDER BY ai.animal_type