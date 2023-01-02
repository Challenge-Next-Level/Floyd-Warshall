SELECT c.name Customers
FROM Customers C
LEFT OUTER JOIN Orders O
ON C.id = O.customerId
WHERE O.id is null