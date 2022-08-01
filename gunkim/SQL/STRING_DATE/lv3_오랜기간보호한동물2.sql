-- 가장 오래 보호된 동물 2마리 조회
SELECT *
FROM
   (SELECT ai.animal_id, ai.name
    FROM ANIMAL_INS ai
    INNER JOIN ANIMAL_OUTS ao
        ON ai.animal_id = ao.animal_id
    ORDER BY ao.datetime - ai.datetime DESC)
WHERE ROWNUM <= 2