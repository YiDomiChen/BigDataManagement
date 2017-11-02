
SELECT COUNT(customer_id) cust_num FROM customer WHERE customer_id IN
(
    SELECT DISTINCT(c.customer_id) cust_num FROM customer AS c INNER JOIN rental AS r ON r.customer_id = c.customer_id 
    INNER JOIN inventory AS i ON i.inventory_id = r.inventory_id INNER JOIN film AS f ON f.film_id = i.film_id 
    INNER JOIN film_category AS fc ON fc.film_id = f.film_id INNER JOIN category AS ca ON ca.category_id = fc.category_id
    WHERE ca.name = 'Action'
) 
AND customer_id NOT IN 
(
    SELECT DISTINCT(c.customer_id) cust_num FROM customer AS c INNER JOIN rental AS r ON r.customer_id = c.customer_id 
    INNER JOIN inventory AS i ON i.inventory_id = r.inventory_id INNER JOIN film AS f ON f.film_id = i.film_id 
    INNER JOIN film_category AS fc ON fc.film_id = f.film_id INNER JOIN category AS ca ON ca.category_id = fc.category_id
    WHERE ca.name = 'Horror'
);