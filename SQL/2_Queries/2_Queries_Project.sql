/*
1.
SELECT * FROM nomnom;
  name, neighborhood, cuisine, review, price, health
2.
SELECT DISTINCT neighborhood  FROM nomnom;
  Brooklyn, Midtown, Chinatown, Uptown, Queens, Downtown 
3.
SELECT DISTINCT cuisine FROM nomnom;
Steak Korean Chinese Pizza Ethiopian Vegetarian Italian Japanese American Mediterranean Indian Soul Food Mexican
4.
SELECT * FROM nomnom
 WHERE cuisine = 'Chinese';
5.
SELECT * FROM nomnom
 WHERE cuisine = 'Chinese' AND review >=4 ;
6.
SELECT * FROM nomnom WHERE cuisine ='Italian' AND price = '$$$';
SELECT * FROM nomnom WHERE cuisine ='Italian' AND price LIKE '%$$$%';
7.
SELECT * FROM nomnom WHERE name LIKE '%meatball%';
8.
SELECT * FROM nomnom
  WHERE neighborhood ='Midtown' 
  OR neighborhood='Downtown' 
  OR neighborhood ='Chinatown';
9.
SELECT * FROM nomnom WHERE health IS NULL;
10.
SELECT * FROM nomnom ORDER BY review DESC LIMIT 10;
SELECT name,
  CASE
    WHEN review>4.5 THEN 'Extraordinary'
    WHEN review>4 THEN 'Excellent'
    WHEN review>3 THEN 'Good'
    WHEN review>2 THEN 'Fair'
    ELSE 'Poor'
  END
  AS 'Grade'
FROM nomnom;
*/
