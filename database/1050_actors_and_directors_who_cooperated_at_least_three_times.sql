-- https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times

SELECT DISTINCT
    a.actor_id, a.director_id

FROM
    ActorDirector a
    
INNER JOIN
    (
        SELECT actor_id, director_id, count(director_id) as collab_count
        FROM ActorDirector
        GROUP BY actor_id, director_id
    ) b
    ON a.actor_id = b.actor_ID AND
    a.director_id = b.director_id

WHERE
    b.collab_count >= 3;
