SELECT c.name, COUNT(fc.film_id) FROM category AS c INNER JOIN film_category AS fc ON fc.category_id = c.category_id 
GROUP BY c.name HAVING COUNT(film_id) >= 60 ORDER BY COUNT(fc.film_id) DESC;