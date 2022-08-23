-- 75 점수를 넘는 학생 중 이름의 뒷부분 3글자를 기준으로 정렬 조회
SELECT name FROM STUDENTS
WHERE marks > 75
ORDER BY SUBSTR(name, -3);