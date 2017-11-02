SELECT tc.name from
(
    SELECT c.name, COUNT(fc.film_id) film_num FROM category AS c INNER JOIN film_category AS fc ON fc.category_id = c.category_id 
        GROUP BY c.name
) AS tc ORDER BY tc.film_num DESC LIMIT 1;

