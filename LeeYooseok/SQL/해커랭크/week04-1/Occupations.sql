set @r1=0, @r2=0, @r3=0, @r4=0;

SELECT MIN(Doctor), MIN(Professor), MIN(Singer), MIN(Actor)
FROM(
        SELECT
            CASE
                WHEN Occupation = 'Doctor' then (@r1:=@r1+1)
                WHEN Occupation = 'Professor' then (@r2:=@r2+1)
                WHEN Occupation = 'Singer' then (@r3:=@r3+1)
                WHEN Occupation = 'Actor' then (@r4:=@r4+1) END AS rowNum,
            CASE
                WHEN Occupation = 'Doctor' then Name END AS Doctor,
            CASE
                WHEN Occupation = 'Professor' then Name END AS Professor,
            CASE
                WHEN Occupation = 'Singer' then Name END AS Singer,
            CASE
                WHEN Occupation = 'Actor' then Name END AS Actor
        FROM OCCUPATIONS
        ORDER BY Name
    ) AS temp
GROUP BY rowNum;