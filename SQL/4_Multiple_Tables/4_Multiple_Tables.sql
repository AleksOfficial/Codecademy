/*
splitting up reduces redundant information
joining 2 tables to get full picture is used to get the full image of an unreadable TABLE_CHECKSUM
f.e.
orders
order_id    customer_id   subs_id   date
1           2             3         2017-01-01
2           3             2         2017-01-01
3           3             1         2017-01-01
^unreadable. you will have to go into the customers table and the subsrpctions table to understand what these numbers mean
to make it readable: combine 2 tables using JOIN
SELECT *
FROM orders
JOIN customers // says we want to combine information from orders with customers
  ON orders.customer_id = customers.customer_id; // match the col from customer id in orders with the row in customers

the ON statement makes sure that the data is available in the 2 tables. if it is, it is returned to the query . (in a normal JOIN)

LEFT JOIN lets you combine unmatched values as well. this way, the left table is printed even though there are missing values on the right table
left table = above statement
PK & FK; Already discussed intesively in the onenote videos

SELECT *
  FROM newspaper
LEFT JOIN online
  ON online.id = newspaper.id;

SELECT *
  FROM newspaper
LEFT JOIN online
  ON online.id = newspaper.id
  WHERE online.id IS NULL;

CROSS JOIN combines each element with the other

UNION lets us combine 2 tables with the same cols + datatypes within cols; duplicate entries will be excluded

WITH statement -> uses 
*/

SELECT *
FROM orders
JOIN subscriptions
  ON orders.subscription_id = subscriptions.subscription_id;

SELECT *
FROM orders
JOIN subscriptions
  ON orders.subscription_id = subscriptions.subscription_id
  WHERE description = 'Fashion Magazine';

SELECT *
  FROM newspaper
LEFT JOIN online
  ON online.id = newspaper.id;

SELECT *
  FROM newspaper
LEFT JOIN online
  ON online.id = newspaper.id
  WHERE online.id IS NULL; /* THIS STATEMENT SELECTS ALL THE ELEMENTS THAT AREN'T MATCHED BY ONLINE*/

SELECT COUNT(*)
  FROM newspaper
  WHERE start_month <= 3 AND end_month >=3;

SELECT *
  from newspaper
CROSS JOIN months;

SELECT *
  FROM newspaper
CROSS JOIN months
  WHERE newspaper.start_month <= month AND newspaper.end_month >= month;

SELECT month, COUNT(*)
FROM newspaper
CROSS JOIN months
WHERE newspaper.start_month<= month AND newspaper.end_month >= month
GROUP BY month;
