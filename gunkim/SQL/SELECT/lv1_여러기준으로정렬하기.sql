-- name 순 정렬 후 datetime의 역순으로 정렬하고 출력
SELECT ai.animal_id, ai.name, ai.datetime from animal_ins ai
order by ai.name, ai.datetime DESC