-- 보호소에 들어올 당시 중성화가 되지 않았지만, 입양갈 당시에는 중성화된 동물 조회
-- 성별 앞에 Spayed 혹은 Neutered가 붙으면 중성화가 된 것이다.
SELECT ai.animal_id, ai.animal_type, ai.name
  FROM animal_ins ai
  INNER JOIN animal_outs ao
    ON ai.animal_id = ao.animal_id
 WHERE ai.sex_upon_intake LIKE 'Intact%'
   AND (ao.sex_upon_outcome LIKE 'Spayed%' OR
       ao.sex_upon_outcome LIKE 'Neutered%')
 ORDER BY ai.animal_id
