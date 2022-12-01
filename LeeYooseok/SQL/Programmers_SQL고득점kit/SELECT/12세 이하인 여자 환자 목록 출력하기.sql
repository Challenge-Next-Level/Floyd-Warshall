SELECT pt_name, pt_no, gend_cd, age, IFNULL(tlno, 'NONE') as tlno
FROM PATIENT
WHERE age <= 12 AND gend_cd = 'W'
ORDER BY age DESC, pt_name