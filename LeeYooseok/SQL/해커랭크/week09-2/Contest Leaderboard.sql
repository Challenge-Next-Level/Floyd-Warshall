SELECT s.hacker_id as id, h.name, s.sum_score as score
FROM
    (SELECT SUM(max_table.score) as sum_score, hacker_id
     FROM (SELECT MAX(score) as score, challenge_id, hacker_id
           FROM Submissions
           GROUP BY challenge_id, hacker_id) as max_table
     GROUP BY hacker_id
     HAVING sum_score != 0) as s
        LEFT OUTER JOIN
    Hackers as h
    ON s.hacker_id = h.hacker_id
ORDER BY score DESC, id