# Write your MySQL query statement below

SELECT 
    D.name AS Department,
    E.name AS Employee,
    E.salary
FROM Employee E
JOIN Department D
    ON E.departmentId = D.id
JOIN 
    (SELECT departmentId AS id, MAX(salary) AS salary
    FROM Employee
    GROUP BY departmentId) AS D2
    ON D2.id = D.id
WHERE E.salary = D2.salary