SELECT player_id, MIN(event_date) as first_login
FROM Activity
GROUP BY player_id
HAVING SUM(games_played) > 0