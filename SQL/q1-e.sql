SELECT CONCAT(a.first_name, " ", a.last_name) full_name 
FROM actor AS a INNER JOIN film_actor AS fa ON fa.actor_id = a.actor_id 
GROUP BY a.actor_id HAVING COUNT(fa.film_id) > 1 ORDER BY full_name;