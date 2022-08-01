-- 중성화 컬럼을 생성(중성화가 되었다면 O, 아니라면 X로 표시)
SELECT animal_id, name,
        CASE WHEN sex_upon_intake LIKE 'Neutered%' THEN 'O'
             WHEN sex_upon_intake LIKE 'Spayed%' THEN 'O'
        ELSE 'X'
        END
        AS 중성화
FROM ANIMAL_INS
ORDER BY animal_id