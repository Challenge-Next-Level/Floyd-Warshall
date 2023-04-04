select bike_id
from rental_history
where date(rent_at) between "2021-01-01" AND "2021-01-31"
group by bike_id
having SUM(distance) >= 50000
;