SELECT f.title, c.name FROM film AS f INNER JOIN film_category AS fc ON f.film_id = fc.film_id INNER JOIN category AS c ON fc.category_id = c.category_id ORDER BY f.title ASC;