-- Stored Procedure 만들기
DELIMITER $$
CREATE PROCEDURE getPrime(IN n INT, OUT result VARCHAR(16383)) # 함수 선언
BEGIN
    DECLARE j, i, flag INT; # 변수 선언
    SET j:=2; # j 에 2 할당
    SET result:= ' ';
    WHILE (j<n) DO # n 보다 작은 소수 구하기
            SET i:=2;
            SET flag:=0;

            WHILE (i<=j) DO
                    IF (j%i=0) THEN # 나누어 떨어지면 -> flag 에 1 더함
                        SET flag:=flag+1;
                    END IF;
                    SET i:=i+1;
                END WHILE;

            IF (flag=1) THEN # flag 가 1이 아니면 -> 자기 자신으로 나누어 떨어지는 수 이외의 수가 있다면 -> 소수가 아님
                SET result:=CONCAT(result, j, '&');
            END IF;
            SET j:=j+1;
        END WHILE;

END $$
-- 만든 Stored Procedure 호출(call)하기
CALL getPrime(1000, @result);
SELECT SUBSTR(@result, 1, LENGTH(@result)-1); # 마지막 & 제외 하기 위해서, @result 길이의 -1 만큼 출력