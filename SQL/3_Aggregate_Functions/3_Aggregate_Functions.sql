/*
COUNT -> Counts how many rows are in a table
SUM -> adds all values in a particular column
MIN/MAX -> sreturns highes/lowest value of col
AVG -> returns average value of col
ROUND -> takes in col name and integer, integer are the number of decimals after comma
GROUP BY -> Can group up a col entry that comes up a few times, good combo f.e. with average
its possible to group by a function value. to be prone to typing errors, you can reference names with integer ids 
HAVING -> is like the WHERE

Aggregate functions compute a single result set from a set of values
*/
SELECT COUNT(*)
  FROM fake_apps;
SELECT COUNT(*)
  FROM fake_apps
  WHERE price=0.0;

SELECT SUM(downlaods)
  FROM fake_apps;

SELECT MIN(downloads)
FROM fake_apps;
SELECT MAX(price)
FROM fake_apps;

SELECT AVG(downloads)
  FROM fake_apps;
SELECT AVG(price)
  FROM fake_apps;

SELECT ROUND( AVG(price),2)
  from fake_apps;

SELECT year, AVG(imdb_rating)
FROM movies
GROUP BY year
ORDER BY year;
SELECT price, count(*)
FROM fake_apps
GROUP BY price;
SELECT price, count(downloads)
FROM fake_apps
WHERE downloads >20000
GROUP BY price;

SELECT category, 
   price,
   AVG(downloads)
FROM fake_apps
GROUP BY category, price;

