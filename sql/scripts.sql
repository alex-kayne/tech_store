-- order total amount by clients
SELECT o.client_id AS client_id, SUM(p.price * op.quantity) AS total_price
FROM orders AS o
JOIN orders_products AS op ON o.id = o.id = op.order_id
JOIN products AS p ON p.id = op.product_id
GROUP BY client_id;

-- recursive tree visitor
WITH RECURSIVE categories_tree AS (

    SELECT id, name, parent_id, id as first_level
    FROM categories
    WHERE parent_id = 0

    UNION ALL

    SELECT child.id, child.name, child.parent_id, first_level
    FROM categories AS child
    JOIN categories_tree AS parent ON child.parent_id = parent.id
)

SELECT first_level as category_id, count(*) as child_count
FROM categories_tree
where parent_id != 0
GROUP BY first_level;

--find most popular products by quantity
SELECT product_id, sum(quantity)
FROM orders AS o
JOIN orders_products AS op ON o.id = op.order_id
WHERE dt_created >= date('now', '-30 days')
GROUP BY product_id
ORDER BY sum(quantity) DESC
LIMIT 5;
