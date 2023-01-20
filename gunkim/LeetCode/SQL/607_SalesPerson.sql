SELECT name
FROM SalesPerson
WHERE sales_id NOT IN (SELECT sales_id
                        FROM Orders o, Company c
                        WHERE o.com_id = c.com_id AND c.name = 'RED')