select min(Doctor), min(Professor), min(Singer), min(Actor)
from
(Select  RANK() OVER(PARTITION BY occupation ORDER BY name) rank,
    case OCCUPATION when 'Doctor' then NAME end AS Doctor,
    case OCCUPATION when 'Professor' then NAME end AS Professor,
    case OCCUPATION when 'Singer' then NAME end AS Singer,
    case OCCUPATION when 'Actor' then NAME end AS Actor
from occupations)
group by rank
order by rank;