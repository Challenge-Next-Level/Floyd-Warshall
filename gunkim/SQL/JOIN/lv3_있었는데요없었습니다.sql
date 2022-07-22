-- 입양일이 보호 시작일보다 빠른 동물 조회
SELECT ao.animal_id, ao.name
  FROM animal_outs ao
 INNER JOIN animal_ins ai
    ON ao.animal_id = ai.animal_id
 WHERE ao.datetime < ai.datetime
 ORDER BY ai.datetime
