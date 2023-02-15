CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    DECLARE x int;
    SET x=N-1;
    RETURN (
        SELECT salary
        FROM Employee
        GROUP BY salary
        ORDER BY salary DESC LIMIT x,1 # N-1 번부터 1개
    );
END