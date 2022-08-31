# 세미콜론 붙이자..., CONCAT 으로 문자열 이을 수 있음
SELECT CONCAT(Name, '(', LEFT(Occupation, 1), ')')
FROM OCCUPATIONS
ORDER BY NAME;

SELECT CONCAT('There are a total of ', COUNT(Occupation), ' ', Lower(Occupation), 's.')
FROM OCCUPATIONS
GROUP BY Occupation
ORDER BY COUNT(Occupation), Occupation;