-- 입양을 못간 동물 중, 가장 오래 보호소에 있던 동물 3마리 조회
SELECT *
  FROM (SELECT ai.name, ai.datetime
          FROM animal_ins ai
          LEFT OUTER JOIN animal_outs ao
            ON ai.animal_id = ao.animal_id
         WHERE ao.datetime IS NULL
         ORDER BY ai.datetime)
 WHERE ROWNUM <= 3