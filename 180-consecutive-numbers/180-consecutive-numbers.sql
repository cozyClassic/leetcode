# Write your MySQL query statement below
SELECT DISTINCT num AS ConsecutiveNums
FROM Logs
where 
    (Id + 1, Num) in (select * from Logs) 
    AND (Id + 2, Num) in (select * from Logs)