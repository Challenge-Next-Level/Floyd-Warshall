# is_evil=0 값인 non-evil 지팡이들만 골라야 한다.
# Age, Power 값이 각각 같은 지팡이들 중에서 coins_needed 값을 최소로 하는 지팡이를 골라야 한다.
# power 기준으로 내림차순 정렬하며, 동일한 power 값이 있을 때는 age 값을 기준으로 내림차순 정렬
SELECT W.id, P.age, W.coins_needed, W.power
FROM
    Wands W
        INNER JOIN
    Wands_Property P
    ON W.code = P.code
WHERE P.is_evil = 0
  AND W.coins_needed = (SELECT MIN(W1.coins_needed)
                        FROM
                            Wands W1
                                INNER JOIN
                            Wands_Property P1
                            ON W1.code = P1.code
                        WHERE P1.is_evil = 0
                          AND W1.power = W.power
                          AND P1.age = P.age)
ORDER BY W.power DESC, P.age DESC

# 서브쿼리의 WHERE 구문에서 메인쿼리에서 조인한 테이블들의 칼럼을 활용했다는 점이다.
# 이를 이용해 같은 Age, Power 값들인 지팡이 들 중에서 coins_needed 값을 최소로하는 데이터들을 찾을 수 있었다는 점이다.