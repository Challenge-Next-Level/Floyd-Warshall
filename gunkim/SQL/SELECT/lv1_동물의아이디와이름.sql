-- animal_id 순으로 정렬 출력
SELECT ai.animal_id, ai.name from animal_ins ai
group by ai.animal_id