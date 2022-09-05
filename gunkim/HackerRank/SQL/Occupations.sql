--group by 는 집계함수라 하나의 결과 값을 반환
--예를 들어 rank가 1위 인 녀석은 여러개임 어느 한 직업의 1위, 나머지 null 값들(그 중에 1위에 null 인 곳도있음)
--따라서 그들 중 하나를 결과 값으로 출력해야 함. min, max는 null을 생각하지 않음. 따라서 null 외에 1위 인 곳의 이름을 가져오게 됨.
-- MIN, MAX 둘 다 같은 결과임
SELECT MIN(Doctor), MIN(Professor), MIN(Singer), MIN(Actor)
FROM
(SELECT  RANK() OVER(PARTITION BY occupation ORDER BY name) RANK,
    CASE occupation WHEN 'Doctor' THEN NAME END AS Doctor,
    CASE occupation WHEN 'Professor' THEN NAME END AS Professor,
    CASE occupation WHEN 'Singer' THEN NAME END AS Singer,
    CASE occupation WHEN 'Actor' THEN NAME END AS Actor
FROM OCCUPATIONS)
GROUP BY rank
ORDER BY rank;