SELECT employee_id
FROM (
         SELECT e.employee_id
         FROM Employees e LEFT OUTER JOIN Salaries s ON e.employee_id = s.employee_id
         WHERE s.employee_id IS NULL
         UNION
         SELECT s.employee_id
         FROM Employees e RIGHT OUTER JOIN Salaries s ON e.employee_id = s.employee_id
         WHERE e.employee_id IS NULL
     ) as t
ORDER BY employee_id
