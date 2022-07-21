-- 입양을 간 기록은 있고, 보호소에 들어온 기록이 없는 동물 조회
SELECT ao.animal_id, ao.name
  FROM animal_outs ao
  LEFT OUTER JOIN animal_ins ai
    ON ao.animal_id = ai.animal_id
 WHERE ai.intake_condition IS NULL
 ORDER BY ao.animal_id
