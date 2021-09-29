-- https://leetcode.com/problems/game-play-analysis-i/submissions/

SELECT
    player_id,
    TO_CHAR((MIN(event_date)), 'YYYY-MM-DD') first_login

FROM
    Activity

GROUP BY
    player_id;
