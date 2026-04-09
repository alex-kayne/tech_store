CREATE VIEW IF NOT EXISTS top_five_products_by_quantity AS
WITH RECURSIVE categories_tree AS (

    SELECT id, name, parent_id, name as first_level_name
    FROM categories
    WHERE parent_id = 0

    UNION ALL

    SELECT child.id, child.name, child.parent_id, first_level_name
    FROM categories AS child
    JOIN categories_tree AS parent ON child.parent_id = parent.id
)

SELECT p.name,  group_concat(ct.first_level_name) AS first_level_name, sum(op.quantity) as total_quantity
FROM orders AS o
JOIN orders_products AS op ON o.id = op.order_id
JOIN products AS p ON op.product_id = p.id
JOIN categories_has_products AS chp ON p.id = chp.product_id
JOIN categories_tree AS ct ON chp.category_id = ct.id
WHERE dt_created >= date('now', '-30 days')
GROUP BY op.product_id
ORDER BY sum(op.quantity) DESC
LIMIT 5;