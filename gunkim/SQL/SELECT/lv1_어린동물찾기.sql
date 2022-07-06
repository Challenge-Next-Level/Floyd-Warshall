-- Aged 상태가 아닌 동물 출력
SELECT ai.animal_id, ai.name
from animal_ins ai
where ai.intake_condition != 'Aged'
order by ai.animal_id