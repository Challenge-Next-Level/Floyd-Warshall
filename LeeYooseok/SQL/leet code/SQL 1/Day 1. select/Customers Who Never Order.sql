SELECT c.name as Customers
FROM Customers c
WHERE c.id not in (SELECT DISTINCT customerId FROM Orders)