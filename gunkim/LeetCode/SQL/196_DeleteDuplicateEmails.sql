-- 스택_큐 오버플로우에 비슷한 질문이 있었다.
-- https://stackoverflow.com/questions/4685173/delete-all-duplicate-rows-except-for-one-in-mysql
DELETE p1
FROM Person p1, Person p2
WHERE p1.id > p2.id AND p1.email = p2.email;