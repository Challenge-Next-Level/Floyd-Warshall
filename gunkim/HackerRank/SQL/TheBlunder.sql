-- 마지막 결과 값은 소수점 올림
-- salary에서 0은 모두 제거, 근데 integer도 repalce가 적용이 되네. 문자열만 돼야하는거 아닌가
SELECT CEIL(AVG(salary) - AVG(REPLACE(salary, '0'))) FROM EMPLOYEES;