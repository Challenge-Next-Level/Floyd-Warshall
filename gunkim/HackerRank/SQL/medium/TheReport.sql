SELECT
    CASE WHEN g.grade > 7 THEN s.name ELSE 'NULL' END AS NameOrNUll
    ,g.grade
    ,s.marks
FROM STUDENTS s
JOIN GRADES g
ON s.marks >= g.min_mark AND s.marks <= g.max_mark
ORDER BY g.grade DESC, NameOrNUll ASC, s.marks ASC;