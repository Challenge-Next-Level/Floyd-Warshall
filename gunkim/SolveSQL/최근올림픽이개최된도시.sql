select year, upper(substr(city,1,3)) as city
from games
where year >= 2000
order by year desc;