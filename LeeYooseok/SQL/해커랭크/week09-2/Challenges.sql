# 모르겠다... 다시 풀기
SELECT Hackers.hacker_id, Hackers.name, COUNT(*) AS challenges_created
FROM Hackers
         INNER JOIN Challenges ON Hackers.hacker_id = Challenges.hacker_id
GROUP BY Hackers.hacker_id, Hackers.name
HAVING challenges_created IN (SELECT sub2.challenges_created
                              FROM (SELECT hacker_id, COUNT(*) AS challenges_created
                                    FROM Challenges
                                    GROUP BY Challenges.hacker_id) sub2
                              GROUP BY sub2.challenges_created
                              HAVING COUNT(*) = 1)
    OR challenges_created = (SELECT MAX(sub1.challenges_created)
                             FROM (SELECT COUNT(*) AS challenges_created
                                   FROM Challenges
                                   GROUP BY Challenges.hacker_id) sub1)
ORDER BY challenges_created DESC, Hackers.hacker_id