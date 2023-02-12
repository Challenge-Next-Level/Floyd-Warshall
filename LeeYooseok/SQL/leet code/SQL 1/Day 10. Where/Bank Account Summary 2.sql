SELECT u.name as name, SUM(t.amount) as balance
FROM Transactions as t, Users as u
WHERE t.account = u.account
GROUP BY t.account
HAVING balance > 10000