CREATE TABLE IF NOT EXISTS table_inventory_and_supplies (
    item_id INT AUTO_INCREMENT PRIMARY KEY,
    item_name VARCHAR(100),
    item_description TEXT,
    supplier_name VARCHAR(100),
    purchase_date DATE,
    purchase_price DECIMAL(10, 2),
    quantity INT,
    unit_of_measurement VARCHAR(50),
    location VARCHAR(100),
    minimum_stock INT,
    maximum_stock INT,
    last_restock_date DATE,
    additional_notes TEXT
);