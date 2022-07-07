-- 중복되는 이름, null은 제외한 name의 총 갯수
SELECT COUNT(DISTINCT ai.name) from animal_ins ai
aaa