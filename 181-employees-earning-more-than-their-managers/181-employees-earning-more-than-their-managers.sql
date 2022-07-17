# Write your MySQL query statement below
SELECT
    E.name AS Employee
FROM 
    Employee AS E
    JOIN
        (SELECT * FROM Employee) AS M
        ON
            M.id = E.managerId
            AND E.salary > M.salary