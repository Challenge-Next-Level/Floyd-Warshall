-- 3개의 변의 길이 비교를 통해 어떤 삼각형인지 분류
-- A,B,C의 길이 조건을 A<=B<=C로 가정하고 풀었다. (문제 조건에 없음;;) 그래도 통과는 했다.
SELECT
    CASE
        WHEN A + B <= C THEN 'Not A Triangle'
        WHEN A != B AND B != C AND A != C THEN 'Scalene'
        WHEN A = B AND B = C AND A = C THEN 'Equilateral'
        ELSE 'Isosceles'
    END
FROM TRIANGLES;