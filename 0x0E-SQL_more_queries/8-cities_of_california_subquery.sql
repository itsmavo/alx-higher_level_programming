-- lists all cities of California
-- lists all rows of a column in a db
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;
