SELECT COUNT(customer_id) AS cust_num FROM customer WHERE 
customer_id IN 
(
    SELECT customer_id FROM action_view
)
AND customer_id NOT IN 
(
    SELECT customer_id FROM horror_view
);