/*Prep for project*/
CREATE TABLE 4_trips(
  id        INTEGER,
  date      TEXT,
  pickup    TEXT,
  dropoff   TEXT,
  rider_id  INTEGER,
  car_id    INTEGER,
  type      TEXT,
  cost      INTEGER

);

CREATE TABLE 4_riders(
  id          INTEGER,
  FIRST       TEXT,
  LAST        TEXT,
  username    TEXT,
  rating      INTEGER,
  total_trips INTEGER,
  referred    INTEGER

);

CREATE TABLE 4_riders2(
  select * from 4_riders
);
CREATE TABLE 4_cars(
  id              INTEGER,
  model           TEXT,
  OS              TEXT,
  status          TEXT,
  trips_completed INTEGER
);


LOAD DATA INFILE '../../../Google Drive/Codecademy/SQL/4_Multiple_Tables/trips.csv'
INTO TABLE 4_trips
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n';

LOAD DATA INFILE '../../../Google Drive/Codecademy/SQL/4_Multiple_Tables/riders.csv'
INTO TABLE 4_riders
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n';

LOAD DATA INFILE '../../../Google Drive/Codecademy/SQL/4_Multiple_Tables/riders2.csv'
INTO TABLE 4_riders2
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n';


LOAD DATA INFILE '../../../Google Drive/Codecademy/SQL/4_Multiple_Tables/cars.csv'
INTO TABLE 4_cars
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n';

/*START OF PROJECT */

/*1. what are the col names*/
SELECT * FROM 4_trips; /*id, date, pickup, dropoff, rider_id, car_id, type, cost*/
SELECT * FROM 4_riders;/*id, first, last, username, rating, total_trips, referred*/
SELECT * FROM 4_riders2;/*id, first, last, username, rating, total_trips, referred*/

/*2. What are the PKs? lol forgot to add them.. What about the FKs? the commands weren't mentioned..*/

ALTER TABLE 4_riders
  ADD PRIMARY KEY(id);

ALTER TABLE 4_riders2
  ADD PRIMARY KEY(id);
  
ALTER TABLE 4_cars
  ADD PRIMARY KEY(id);

ALTER TABLE 4_trips

  ADD FOREIGN KEY(rider_id) REFERENCES 4_riders(id), /*had to cancel these things out. it seems like my database system doesn't like multiple FKs to tables*/
  ADD FOREIGN KEY(rider_id) REFERENCES 4_riders2(id),/*ER_NO_REFERENCED_ROW_2: Cannot add or update child row: a foreign key constraint fails('codecademy_sql'.'#sql-4b78_1b9', CONSTRAINT '#sql-4b78_1b9_ibfk_2' FOREIGN KEY (rider_id) REFERENCES '4_riders'('id'))*/
  ADD FOREIGN KEY(car_id) REFERENCES 4_cars(id);

/*3. CROSS JOIN*/
SELECT *
  FROM 4_riders
CROSS JOIN 4_cars; /*not really useful... tbh*/

/*4. LEFT join trips and riders*/
SELECT *
  FROM 4_trips
LEFT JOIN 4_riders
  ON 4_riders.id = 4_trips.rider_id;

/*5. INNER JOIN ON TRIPS & CARS*/
SELECT *
  FROM 4_trips
JOIN 4_cars
  ON 4_trips.car_id = 4_cars.id;

/*6. NEW RIDERS */
SELECT *
  FROM 4_riders
UNION
SELECT *
  FROM 4_riders2;

/*7. avg cost of trip */

SELECT AVG(cost)
  FROM 4_trips; /*€ 32*/

/*8. RIDERS less than 500 times*/
WITH riders AS (
  SELECT * FROM 4_riders
  UNION
  SELECT * FROM 4_riders2)
SELECT FIRST AS 'Firstname', LAST AS 'Lastname', total_trips AS 'Trips'
  FROM riders
  WHERE total_trips< 500;

/*9. number cars active */
SELECT COUNT(*)
  FROM 4_cars
  WHERE status ='active'; /*3*/

/*10. Recall of cars*/
SELECT *
  FROM 4_cars
  ORDER BY trips_completed DESC
  LIMIT 2;