CREATE TABLE IF NOT EXISTS invoices (
    invoice_id VARCHAR(200) PRIMARY KEY,
    patient_id INT,
    invoice_date DATE,
    due_date DATE,
    total_amount DECIMAL(10, 2),
    payment_status ENUM('Unpaid', 'Paid', 'Partially Paid'),
    billing_address VARCHAR(255),
    billing_city VARCHAR(50),
    billing_state VARCHAR(50),
    billing_zip_code VARCHAR(10),
    itemized_details TEXT
);

CREATE TABLE IF NOT EXISTS payment_records (
    patient_id INT AUTO_INCREMENT PRIMARY KEY,
    invoice_id VARCHAR(200),
    payment_date DATE,
    payment_amount DECIMAL(10, 2),
    payment_method VARCHAR(50),
    transaction_reference VARCHAR(100),
    payment_status ENUM('Success', 'Pending', 'Failed'),
    additional_notes TEXT,
    FOREIGN KEY (invoice_id) REFERENCES invoices(invoice_id)
);