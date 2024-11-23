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