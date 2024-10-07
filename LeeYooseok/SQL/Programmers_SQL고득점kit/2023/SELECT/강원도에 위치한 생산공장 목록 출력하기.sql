SELECT factory_id, factory_name, address
FROM food_factory
WHERE LEFT(address, 3) = '강원도'
ORDER BY factory_id ASC