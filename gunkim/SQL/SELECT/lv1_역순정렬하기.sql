-- id의 역순으로 정렬하여 출력
-- 주의: name이 아닌 id순으로 정렬
SELECT ai.name, ai.datetime from animal_ins ai
order by ai.animal_id DESC