select day, sum(tip) as tip_daily
from tips
group by day
order by tip_daily desc
limit 1