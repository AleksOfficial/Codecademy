/* in case you want to import it by phpMyAdmin, you can import it as well into a seperate table. then alter the column types.
after that you INSERT everything into your existing table you created with a sql statement. hihi. 
ALTER TABLE trial 
MODIFY COLUMN `COL 4` INTEGER,
MODIFY COLUMN `COL 5` INTEGER,
MODIFY COLUMN `COL 6` INTEGER,
MODIFY COLUMN `COL 7` INTEGER;
 

INSERT INTO 3_agg_startups SELECT * FROM trial;
*/

/*LOAD DATA [LOW_PRIORITY] [LOCAL] INFILE 'file_name.txt' [REPLACE | IGNORE]
    INTO TABLE tbl_name
    [FIELDS
        [TERMINATED BY '\t']
        [OPTIONALLY] ENCLOSED BY '']
        [ESCAPED BY '\\' ]]
    [LINES TERMINATED BY '\n']
    [IGNORE number LINES]
    [(col_name,...)]*/
/* that is the way to directly import data into a table from a CSV :)*/
CREATE TABLE 3_agg_startups(
  name TEXT,
  location TEXT,
  category TEXT,
  employees INTEGER,
  raised BIGINT,
  valuation BIGINT,
  founded INTEGER,
  stage TEXT,
  ceo TEXT,
  info TEXT
);


LOAD DATA INFILE '../../../Google Drive/Codecademy/SQL/3_Aggregate_Functions/DATA.csv'
INTO TABLE 3_agg_startups
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n';

/* Start of exercise lol*/
SELECT * FROM 3_agg_startups;
/* 10 cols*/
SELECT COUNT(*) FROM 3_agg_startups;
/*70 companies*/
SELECT SUM(valuation) FROM 3_agg_startups;
/*974,455,790,000.00*/

SELECT MAX(raised) FROM 3_agg_startups;
/*11,500,000,000	*/

SELECT MAX(raised) FROM 3_agg_startups WHERE stage ="Seed";
/*1,800,000.00*/

SELECT MIN(founded) FROM 3_agg_startups;
/*1994*/

SELECT AVG(valuation) FROM 3_agg_startups
WHERE valuation > 0;
/*13920797000.0000
-> That one was different than the Codecademy one cuz they didnt count the companies which had 0 evaluation
*/

SELECT AVG(valuation), category
FROM 3_agg_startups
WHERE valuation > 0
GROUP BY category;

SELECT ROUND(AVG(valuation),2), category
FROM 3_agg_startups
WHERE valuation > 0
GROUP BY category;

SELECT ROUND(AVG(valuation),2), category
FROM 3_agg_startups
WHERE valuation > 0
GROUP BY 2
ORDER BY 2 DESC;

SELECT category, COUNT(*) AS 'amount'
FROM 3_agg_startups
GROUP BY category;

SELECT category, COUNT(*) AS 'amount'
FROM 3_agg_startups
GROUP BY category
HAVING COUNT(*) >3
ORDER BY 2 DESC; 
/* lol. having was important and the 2.
Most competitive: Social, Mobile, Education */

SELECT AVG(employees), location
FROM 3_agg_startups
GROUP BY 2;

SELECT AVG(employees), location
FROM 3_agg_startups
GROUP BY 2
HAVING AVG(employees)>500
ORDER BY 1 DESC;
/* Silicon Valley, San Francisco, New York, Brooklyn */

