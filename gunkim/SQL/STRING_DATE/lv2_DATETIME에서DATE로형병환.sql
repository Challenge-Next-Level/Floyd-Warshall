-- datetime 컬럼의 날짜를 'YYYY-MM-DD'형식으로 조회하기
SELECT animal_id, name, TO_CHAR(datetime, 'YYYY-MM-DD')
FROM ANIMAL_INS
ORDER BY animal_id