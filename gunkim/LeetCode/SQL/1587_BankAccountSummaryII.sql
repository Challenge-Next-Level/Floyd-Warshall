SELECT u.name AS name, SUM(t.amount) AS balance
FROM Users u, Transactions t
WHERE u.account = t.account
GROUP BY u.account
HAVING SUM(t.amount) > 10000