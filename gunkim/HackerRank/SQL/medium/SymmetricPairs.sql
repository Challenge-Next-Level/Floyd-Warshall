-- <> : 같지 않다의 의미(SQL은 어느 DB든 기본적으로 <>를 같지 않다의 의미로 사용한다고 함)
SELECT DISTINCT f1.x,f1.y
FROM FUNCTIONS f1
JOIN FUNCTIONS f2
ON (f1.x = f2.y AND f1.y = f2.x AND f1.rowid <> f2.rowid)
WHERE f1.x <= f1.y
ORDER BY f1.x;