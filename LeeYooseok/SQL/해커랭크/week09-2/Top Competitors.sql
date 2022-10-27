SELECT h.hacker_id, h.name
FROM
    Hackers as h
        INNER JOIN
    (SELECT s.hacker_id, COUNT(s.hacker_id) as cnt
     FROM
         Submissions as s
             LEFT OUTER JOIN
         (SELECT c.challenge_id, d.score
          FROM
              Challenges as c
                  LEFT OUTER JOIN
              Difficulty as d
              ON c.difficulty_level = d.difficulty_level) as cd
         ON s.challenge_id = cd.challenge_id
     WHERE s.score = cd.score
     GROUP BY s.hacker_id
     HAVING COUNT(s.hacker_id) > 1) as cds
    ON h.hacker_id = cds.hacker_id
ORDER BY cds.cnt DESC, h.hacker_id

SELECT H.hacker_id, H.name
FROM Submissions S
         INNER JOIN Challenges C ON S.challenge_id = C.challenge_id
         INNER JOIN Difficulty D ON C.difficulty_level = D.difficulty_level
         INNER JOIN Hackers H ON S.hacker_id = H.hacker_id
WHERE S.score = D.score AND C.difficulty_level = D.difficulty_level
GROUP BY H.hacker_id, H.name
HAVING COUNT(H.hacker_id) > 1
ORDER BY COUNT(H.hacker_id) DESC, H.hacker_id