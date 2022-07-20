-- NULL인 값은 지정값으로 대체 출력하여 name을 조회
SELECT animal_type, NVL(name, 'No name'), sex_upon_intake
  FROM animal_ins
 ORDER BY animal_id