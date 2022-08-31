# Group By 시 비 집계 컬럼에는 ANY_VALUE 적용 (?)
SELECT h.hacker_id AS id, ANY_VALUE(h.name), SUM(s.max_score) AS score
FROM Hackers AS h,
     (SELECT hacker_id, challenge_id, max(score) AS max_score
      FROM Submissions
      GROUP BY hacker_id, challenge_id) AS s
WHERE
        h.hacker_id = s.hacker_id
GROUP BY id
HAVING score > 0
ORDER BY score DESC, id