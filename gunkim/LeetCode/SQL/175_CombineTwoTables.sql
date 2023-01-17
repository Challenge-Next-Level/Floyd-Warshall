SELECT P.firstName,P.lastName,IFNULL(A.city,null) AS city,IFNULL(A.state,null) AS state
FROM Person P
LEFT JOIN Address A
ON P.personId = A.personId