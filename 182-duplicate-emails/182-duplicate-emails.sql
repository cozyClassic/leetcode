# Write your MySQL query statement below
SELECT DISTINCT P1.email
FROM 
    Person AS P1,
    Person AS P2
WHERE
    P1.email = P2.email
    AND P1.id <> P2.id