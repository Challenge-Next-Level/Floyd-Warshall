SET @num = 21; # 변수 선언
SELECT REPEAT('* ', @num := @num - 1)  # 반복문 repeat(s, n) : s - 반복할 string, n - 반복할 횟수
# := set 없이 변수에 값을 지정할 때 사용
FROM information_schema.TABLES # information_schema : mysql 서버 내에 존재하는 DB의 메타 정보, tables : 생성된 모든 테이블 정보를 가져옴
LIMIT 20;
