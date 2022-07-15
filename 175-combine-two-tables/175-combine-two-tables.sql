# Write your MySQL query statement below
SELECT P.firstName, P.lastName, A.city, A.state
from Person AS P
LEFT JOIN Address AS A
    ON A.personId = P.personId;