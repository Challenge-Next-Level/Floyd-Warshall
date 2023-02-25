select a.name
from records r
left outer join games g on r.game_id = g.id
left outer join teams t on r.team_id = t.id
left outer join athletes a on r.athlete_id = a.id
where g.year >= 2000 and r.medal in ('Gold', 'Silver', 'Bronze')
group by r.athlete_id having count(distinct t.team) >= 2
order by a.name