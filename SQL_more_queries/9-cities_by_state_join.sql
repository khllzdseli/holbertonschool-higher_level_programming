-- 9. Cities by States
-- List all cities in the database hbtn_0d_usa
-- Format: cities.id - cities.name - states.name
-- Results sorted by cities.id in ascending order

SELECT c.id, c.name, s.name
FROM cities c
JOIN states s ON c.state_id = s.id
ORDER BY c.id ASC;
