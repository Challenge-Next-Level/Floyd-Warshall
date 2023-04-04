select A.artist_id, A.name
from artists A
left join artworks_artists B
on A.artist_id = B.artist_id
where artwork_id is null
and death_year is not null
;