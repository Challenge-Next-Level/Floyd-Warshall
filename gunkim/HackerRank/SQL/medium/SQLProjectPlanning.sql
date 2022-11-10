-- CONNECT_BY_ROOT: 계층형 쿼리에서 최상위 로우를 반환
-- CONNECT_BY_ISLEAF: 0(자식 노드가 있을 경우), 1(자식 노드가 없을 경우)
-- CONNECT BY PRIOR: 이전 행의 End_Date값이 현재 행의 Start_Date인 행을 찾는다
SELECT Root, End_Date
FROM (
    SELECT Start_Date, End_Date, CONNECT_BY_ROOT Start_Date AS Root, LEVEL AS duration
    FROM Projects
    WHERE CONNECT_BY_ISLEAF = 1 CONNECT BY PRIOR End_Date = Start_Date)
WHERE Root NOT IN (SELECT End_Date FROM Projects)
ORDER BY duration, Root;