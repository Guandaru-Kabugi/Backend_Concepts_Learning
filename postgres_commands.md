# Using LIKE Command
SELECT * FROM person WHERE email_address LIKE '%reuters.com';
any character that proceeds the selected % will be highlighted
SELECT * FROM person WHERE email_address LIKE '_______@%'
any email that has the identified number of underscores that represents character numbers
# Using ILIKE Command
removes case sensitivity
SELECT * FROM person WHERE country_of_birth LIKE 'p%'; return 0 results because the query has capitalized names
SELECT * FROM person WHERE country_of_birth ILIKE 'p%'; returns results due to the use of ILIKE
# Using GROUP BY Command
SELECT country_of_birth,COUNT(*) FROM person GROUP BY country_of_birth; allows to group by country and also give the count for each country
# Using GROUP BY HAVING Command
SELECT country_of_birth,COUNT(*) FROM person GROUP BY country_of_birth HAVING COUNT(*)>5 ORDER BY country_of_birth; restricts the number of output
# MAX Command
SELECT MAX(price) FROM car;
# MIN Command
SELECT MIN(price) FROM car;
# AVERAGE Command
SELECT AVG(price) FROM car;
# ROUND Command
SELECT ROUND(AVG(price)) FROM car;
# MIN GROUP BY
SELECT make,model, MIN(price) FROM car GROUP BY make,model;
# SUM Command
SELECT make, SUM(price) FROM car GROUP BY make;
# COUNT SUM GROUP BY Commands
SELECT make, SUM(price),COUNT(*) FROM car GROUP BY make;
# GET PERCENTAGE Command
SELECT id, make,model,price, price *.10 FROM car;
# ROUNDING OFF
SELECT id, make,model,price, ROUND(price *.10,2) FROM car;
SELECT id, make,model,price, ROUND(price *.10,2),ROUND(price-(price *.10),2) FROM car;
# USING ALIAS
SELECT id, make,model,price, ROUND(price *.10,2)AS ten_percent,ROUND(price-(price *.10),2)AS discount_after_10_percent FROM car;
# USING COALESCE
SELECT id,COALESCE(email,'Email Not Provided') FROM person;
# USING NULLIF
SELECT 10/NULLIF(10,2);
# DATE AND TIME
SELECT NOW(); both date and time
SELECT NOW()::DATE; date alone
SELECT NOW()::TIME; time alone
SELECT NOW() - INTERVAL '10 YEARS'; subtracting years from current time
SELECT NOW() + INTERVAL '10 YEARS'; adding with dates
SELECT (NOW() + INTERVAL '10 YEARS')::DATE; getting just the date
SELECT EXTRACT(YEAR FROM NOW()); extract the actual year
SELECT first_name,last_name,gender,country_of_birth,date_of_birth,EXTRACT(YEAR FROM AGE(NOW(),date_of_birth)) AS age FROM person; extracting the year
# DROPPING & ADDING CONSTRAINTS FOR PRIMARY KEY
ALTER TABLE person DROP CONSTRAINT person_pkey;
ALTER TABLE person ADD PRIMARY KEY(id);
# DELETE ROW DATA
DELETE FROM person WHERE id = 1;
# UNIQUE CONSTRAINTS
SELECT email, COUNT(*) FROM person GROUP BY email HAVING COUNT(*) >1; returns 432 which are blank emails
ALTER TABLE person ADD CONSTRAINT unique_email_address UNIQUE(email);
ALTER TABLE person ADD UNIQUE(email);
# USING CHECK
ALTER TABLE person ADD CONSTRAINT gender_constraint CHECK(gender = 'Female' OR gender = 'Male');
# DELETE DATA
DELETE FROM person WHERE id=1001;
# UPDATE DATA
UPDATE person SET email='eurien@gmail.com' WHERE id=5;
# ON CONFLICT DO NOTHING
INSERT INTO person(id,first_name,last_name,gender,email,date_of_birth,country_of_birth)
VALUES(17,'Jude','Drinnan','Male','jdrinnang@ed.gov',DATE '2004-02-05','China')
test-# ON CONFLICT (id) DO NOTHING;
# UPSERT ON CONFLICT DO UPDATE
NSERT INTO person(id,first_name,last_name,gender,email,date_of_birth,country_of_birth)
VALUES(17,'Jude','Drinnan','Male','jdrinnang@ed.gov',DATE '2004-02-05','China')
ON CONFLICT (id) DO UPDATE SET email=EXCLUDED.email; allows the update of a specific section, even where constraints exist
# FOREIGN KEY JOIN 
UPDATE person SET car_id = 1 WHERE id = 1; car_id is foreign key
# INNER JOIN
SELECT * FROM person JOIN car ON person.car_id = car.id;
SELECT person.first_name, car.make, car.model,car.price FROM person  JOIN car ON person.car_id = car.id; selecting few columns
# LEFT JOIN
SELECT * FROM person LEFT JOIN car ON person.car_id = car.id;
SELECT * FROM person LEFT JOIN car ON person.car_id = car.id WHERE car.* IS NULL;
# DELETE RECORD WITH FOREIGN KEY CONSTRAINT
UPDATE person SET car_id = NULL WHERE id = 1;                                    
UPDATE 1
test=# DELETE FROM car WHERE id =1;
# COPYING TO CSV
\copy (SELECT * FROM person LEFT JOIN car on car.id = person.car_id) TO '/home/pc/Downloads/results.csv' DELIMITER ',' CSV HEADER;
# ALTER SEQUENCE OF DATA RECORDS IN BIGSERIAL
\d person
ALTER SEQUENCE person_id_seq RESTART WITH 9;
# EXTENSIONS ON POSTGRES
SELECT * FROM pg_available_extensions;
# UNDERSTANDING UUIDs UNIVERSALLY UNIQUE IDENTIFIERS
