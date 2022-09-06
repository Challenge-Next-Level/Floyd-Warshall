SELECT a.company_code
     , a.founder
     , COUNT(DISTINCT b.lead_manager_code)
     , COUNT(DISTINCT c.senior_manager_code)
     , COUNT(DISTINCT d.manager_code)
     , COUNT(DISTINCT e.employee_code)
FROM Company a
         LEFT JOIN Lead_manager b on a.company_code = b.company_code
         LEFT JOIN Senior_manager c on b.lead_manager_code = c.lead_manager_code
         LEFT JOIN Manager d on c.senior_manager_code = d.senior_manager_code
         LEFT JOIN Employee e on e.manager_code = d.manager_code
GROUP BY a.company_code, a.founder
ORDER BY a.company_code