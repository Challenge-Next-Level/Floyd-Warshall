select r.athlete_id
from events e, records r
where e.id = r.event_id and e.SPORT = 'Golf'
group by r.athlete_id