SELECT sp.name
FROM SalesPerson sp
WHERE sp.sales_id NOT IN (
    SELECT DISTINCT o.sales_id
    FROM Orders o JOIN Company c ON o.com_id = c.com_id
    WHERE c.name = 'RED'
)
