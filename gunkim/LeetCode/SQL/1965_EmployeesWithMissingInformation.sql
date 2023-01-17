SELECT E.employee_id
FROM Employees E
LEFT OUTER JOIN Salaries S
ON E.employee_id = S.employee_id
WHERE S.salary is null

UNION

SELECT S.employee_id
FROM Salaries S
LEFT OUTER JOIN Employees E
ON E.employee_id = S.employee_id
WHERE E.name is null

ORDER BY employee_id