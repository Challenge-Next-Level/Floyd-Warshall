SELECT n.id
FROM Weather n JOIN Weather f ON DATE_SUB(n.recordDate, INTERVAL 1 DAY) = f.recordDate
WHERE n.temperature > f.temperature