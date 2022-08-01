-- 이름에 'el'이 들어간 Dog를 조회
-- 조건 name에 UPPER를 활용하여 검색하는 것이 포인트
SELECT animal_id, name
FROM ANIMAL_INS
WHERE UPPER(name) LIKE '%EL%'
AND animal_type = 'Dog'
ORDER BY name