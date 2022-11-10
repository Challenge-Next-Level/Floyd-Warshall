-- 같은 테이블을 from에 여러번 사용할 수 있구나,,,
SELECT s.name
FROM STUDENTS s, FRIENDS f, PACKAGES p, PACKAGES p2
WHERE s.id = p.id AND s.id = f.id AND f.friend_id = p2.id AND p.salary < p2.salary
ORDER BY p2.salary;