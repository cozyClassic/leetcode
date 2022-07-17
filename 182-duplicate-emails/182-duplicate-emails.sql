# Write your MySQL query statement below
SELECT DISTINCT P1.email
FROM Person AS P1
    LEFT JOIN 
        (SELECT id, email
        FROM Person
        GROUP BY email) AS P2
    USING (id)
WHERE P2.id IS NULL