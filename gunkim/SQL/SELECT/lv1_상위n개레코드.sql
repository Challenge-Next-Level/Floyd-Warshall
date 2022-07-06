-- datetime으로 정렬된 테이블에서 1행을 출력
SELECT ani.name
from (select * from animal_ins ai
      order by ai.datetime) ani
where ROWNUM = 1