CREATE VIEW top_five_products_by_quantity AS
SELECT product_id, sum(quantity)
FROM orders AS o
JOIN orders_products AS op ON o.id = op.order_id
WHERE dt_created >= date('now', '-30 days')
GROUP BY product_id
ORDER BY sum(quantity) DESC
LIMIT 5;