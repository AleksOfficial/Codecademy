/*
relational database -> stores data into one or more tables, data is related to one another
table -> collection of data organized into rows and cols
cols -> Set of data values of particular type
CREATE -> Syntax
CREATE TABLE <table_name>(
  <col1> <datatype>,
  <col1> <datatype>,
  <col1> <datatype>,
  );
ALTER TABLE <table_name> -> SYNTAX
  ADD col <columnname>;

UPDATE <table_name>
  SET <col_name> = <value>
  WHERE <col_name> = <value>;

DELETE FROM <table_name>
  WHERE <col_name> = <VALUE>;

CONSTRAINTS: PRIMARY KEY, UNIQUE, NOT NULL, DEFAULT



*/
SELECT * FROM celebs;
/*id name age*/

 SELECT * FROM celebs;
 CREATE TABLE celebs(
   id INTEGER,
   name TEXT,
   age INTEGER
 );
 -- Insert rows into table 'celebs'
 INSERT INTO celebs
 ( -- columns to insert data into
  id, name, age
 )
 VALUES
 ( -- first row: values for the columns in the list above
  1, 'Justin Bieber', 22
 );
