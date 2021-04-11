/*
- Core purpose SQL(=Structured Query Language): Retrieve Information from DB
-> SELECT used to query data from database. * = all cols; FROM = from where (Tablename)
-> AS keyword allows to rename column in query; Use single quotation marks (best practice=)
-> DISTINCT is used to return unique values in output; meaning it appears only once in the query
-> WHERE is the if clause of SQL: following operators are possible: =,!=,<,>,>=,<=
-> LIKE useful when comparing similar values: f.e. WHERE name LIKE 'Se_en' -> all names starting with Se and ending with en;
-> _ = One space for a char in the LIKE statement, % = is for any amount of chars
-> Is Null = Empty cols, can't be tested with = operator, just with IS (NOT) NULL
-> BETWEEN Operator used in a WHERE: filters result set within certain range (IS INCLUSIVE), be careful tho: with strings f.e. the second letter is included, but everything else after it not!
-> AND operator is like the Intersection Set of 2 conditions (huehue, this is math evolved right thereeee); nice info graphic here: https://content.codecademy.com/courses/learn-sql/queries/AND.svg
-> OR operator is like the Union Set of 2 conditions (huehue, this is math evolved right thereeee); nice info graphic here: https://content.codecademy.com/courses/learn-sql/queries/OR.svg
-> ORDER BY sorts query by a col name. DESC/ASC are keywords?
-> LIMIT is keyword to limit resultamount down to a number of your preference // not supported in every DB!
-> CASE Statement is like a switch case i guess Syntax is taken from below: 
SELECT name,
  CASE
    WHEN <condtion> THEN <action>
    WHEN <condtion> THEN <action>
    WHEN <condtion> THEN <action>
    ELSE <action>
  END
FROM <tablename>
*/

SELECT * FROM movies;

SELECT name,genre FROM movies;
SELECT name,genre, year FROM movies;


SELECT name AS '______' FROM movies;
SELECT imdb_rating AS 'IMDb' FROM movies;

SELECT DISTINCT genre FROM movies;
SELECT DISTINCT year FROM movies;

SELECT * FROM movies WHERE imdb_rating<5;
SELECT * FROM movies WHERE year>2014;

SELECT name FROM movies WHERE name LIKE 'Se_en';

SELECT * FROM movies WHERE name LIKE '%man%';
SELECT * FROM movies WHERE name LIKE 'the %';

SELECT name FROM movies WHERE imdb_rating IS NULL;

SELECT * FROM movies WHERE name BETWEEN 'D' AND 'G';
SELECT * FROM movies WHERE year BETWEEN 1970 AND 1979;

SELECT * FROM movies WHERE year BETWEEN 1970 AND 1979 and imdb_rating >8;
SELECT * FROM movies WHERE year < 1985 AND genre ='horror';

SELECT * FROM movies WHERE year > 2014 OR genre = 'action';
SELECT * FROM movies WHERE genre = 'comedy' OR genre = 'romance';

SELECT name, year FROM movies ORDER BY name;
SELECT name, year, imdb_rating FROM movies ORDER BY imdb_rating DESC;

SELECT * FROM movies ORDER BY imdb_rating DESC  /* LIMIT 3 -> this statement is for some reason wrong?*/; 

SELECT name,
  CASE
    WHEN genre = 'romance' THEN 'Chill'
    WHEN genre = 'comedy' THEN 'Chill'
    ELSE 'Intense'
  END AS 'mood'
FROM movies;

