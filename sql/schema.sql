CREATE TABLE IF NOT EXISTS products
(
    id       INTEGER PRIMARY KEY AUTOINCREMENT,
    name     TEXT    NOT NULL UNIQUE,
    quantity INTEGER NOT NULL,
    price    REAL    NOT NULL
);

CREATE TABLE IF NOT EXISTS categories
(
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    name      TEXT UNIQUE,
    parent_id INTEGER
);

--потому что из тз не понятно - может ли один продукт входить в несколько категорий
CREATE TABLE IF NOT EXISTS categories_has_products
(
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    category_id INTEGER NOT NULL,
    product_id  INTEGER NOT NULL,
    FOREIGN KEY (category_id) REFERENCES categories (id),
    FOREIGN KEY (product_id) REFERENCES products (id)
);

CREATE TABLE IF NOT EXISTS clients
(
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    name    TEXT,
    address TEXT
);

CREATE TABLE IF NOT EXISTS orders
(
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    dt_created  DATETIME NOT NULL,
    client_id   INTEGER  NOT NULL,
    product_ids TEXT     NOT NULL,
    FOREIGN KEY (client_id) REFERENCES clients (id)
);

CREATE TABLE IF NOT EXISTS orders_price
(
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    FOREIGN KEY (product_id) REFERENCES products (id)
);
