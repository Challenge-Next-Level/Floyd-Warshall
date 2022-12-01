-- INNER JOIN을 깔끔하게 3개 사용하는 것이 포인트
-- HAVING 절은 GROUP BY와 꼭 함께 써야함!
SELECT h.hacker_id, h.name
FROM HACKERS h
JOIN SUBMISSIONS s ON h.hacker_id = s.hacker_id
JOIN DIFFICULTY  d ON s.score = d.score
JOIN CHALLENGES  c ON s.challenge_id = c.challenge_id AND d.difficulty_level = c.difficulty_level
GROUP BY h.hacker_id, h.name HAVING COUNT(s.challenge_id) > 1
ORDER BY COUNT(s.challenge_id) DESC , h.hacker_id ASC ;