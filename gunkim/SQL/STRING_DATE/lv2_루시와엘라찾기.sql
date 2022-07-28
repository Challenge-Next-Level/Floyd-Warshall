-- 해당 이름인 동물들만 조회
SELECT animal_id, name, sex_upon_intake
FROM ANIMAL_INS
WHERE name IN ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')
ORDER BY animal_id