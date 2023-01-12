SELECT user_id, CONCAT(UPPER(LEFT(name, 1)), SUBSTRING(LOWER(name), 2)) as name
from Users
ORDER BY user_id;