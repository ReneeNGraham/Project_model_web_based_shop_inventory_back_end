DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS manufacturers;

CREATE TABLE manufacturers (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  description VARCHAR(255)

);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description VARCHAR(255),
    quantity_in_stock INT,
    cost_to_purchase DECIMAL,
    selling_price DECIMAL,
    manufacturer_id INT REFERENCES manufacturers(id) ON DELETE CASCADE,
);