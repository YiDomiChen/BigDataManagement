CREATE OR REPLACE VIEW action_view AS SELECT DISTINCT(c.customer_id) customer_id FROM customer c 
INNER JOIN rental r ON r.customer_id = c.customer_id 
    INNER JOIN inventory i ON i.inventory_id = r.inventory_id INNER JOIN film f ON f.film_id = i.film_id 
    INNER JOIN film_category fc ON fc.film_id = f.film_id INNER JOIN category ca ON ca.category_id = fc.category_id
    WHERE ca.name = 'Action' ORDER BY c.customer_id;