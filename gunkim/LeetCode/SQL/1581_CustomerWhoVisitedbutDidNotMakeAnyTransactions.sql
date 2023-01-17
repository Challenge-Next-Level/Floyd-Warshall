SELECT v.customer_id, COUNT(*) as count_no_trans
FROM visits v
WHERE visit_id not in (SELECT visit_id FROM transactions)
GROUP BY v.customer_id