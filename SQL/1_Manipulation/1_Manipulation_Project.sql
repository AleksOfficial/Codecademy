CREATE TABLE 1_friends(
  id INTEGER PRIMARY KEY,
  name TEXT, 
  birthday DATE
);
  
INSERT INTO 1_friends (id,name, birthday)
VALUES (1,'Jane Doe', '1990-05-30');

INSERT INTO 1_friends (id,name,birthday)
VALUES (2,'Josh Banger', '1980-10-30');

INSERT INTO 1_friends (id,name,birthday)
VALUES (3,'cuck holder', '1994-07-30');

UPDATE 1_friends 
  SET name ='Jane Smith'
  WHERE name='Jane Doe';


ALTER TABLE 1_friends
  ADD COLUMN email text;

UPDATE 1_friends
SET email ='jane@codecademy.com'
WHERE name LIKE 'Ja%';

SELECT *
  FROM 1_friends;

DELETE FROM 1_friends WHERE id=1;
  

