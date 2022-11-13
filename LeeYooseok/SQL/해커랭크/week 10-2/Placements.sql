SELECT s.name
FROM Students s, Friends f, Packages p, Packages p2
WHERE s.id = p.id AND s.id = f.id AND f.friend_id = p2.id AND p.salary < p2.salary
ORDER BY p2.salary;