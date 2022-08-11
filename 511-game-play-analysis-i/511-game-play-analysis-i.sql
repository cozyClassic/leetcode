# Write your MySQL query statement below
SELECT 
    player_id, 
    first_login
FROM (
    SELECT 
        player_id,
        event_date as first_login,
        dense_rank() over (
            partition by player_id
        order by event_date) AS poz
    FROM Activity
    ) AS src
WHERE poz = 1