SELECT N, (
    CASE
        WHEN P IS NULL THEN 'Root' # 부모가 없으면, Root
        WHEN N NOT IN (SELECT DISTINCT P FROM BST WHERE P IS NOT NULL) THEN 'Leaf' # 누군가의 부모가 아니라면, Leaf
        ELSE 'Inner' # 위 두 상황이 모두 아니라면, Inner
        END
    ) AS nodeType
FROM BST
ORDER BY N