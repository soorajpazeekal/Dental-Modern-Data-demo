CREATE TABLE IF NOT EXISTS staff_information (
    staff_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100),
    date_of_birth DATE,
    gender ENUM('Male', 'Female'),
    contact_number VARCHAR(30),
    email VARCHAR(100),
    address VARCHAR(255),
    city VARCHAR(50),
    state VARCHAR(50),
    zip_code VARCHAR(10),
    position VARCHAR(50),
    department VARCHAR(100),
    hire_date DATE,
    salary DECIMAL(10, 2),
    additional_notes TEXT
);

CREATE TABLE IF NOT EXISTS salary_history (
    salary_history_id INT AUTO_INCREMENT PRIMARY KEY,
    staff_id INT,
    effective_date DATE,
    old_salary DECIMAL(10, 2),
    new_salary DECIMAL(10, 2),
    salary_adjustment_reason VARCHAR(255),
    salary_adjustment_type VARCHAR(50),
    salary_adjustment_percentage DECIMAL(5, 2),
    tax_deductions DECIMAL(10, 2),
    bonus_amount DECIMAL(10, 2),
    review_comments TEXT,
    additional_notes TEXT,
    FOREIGN KEY (staff_id) REFERENCES staff_information(staff_id)
);

CREATE TABLE IF NOT EXISTS attendance_records (
    attendance_id INT AUTO_INCREMENT PRIMARY KEY,
    staff_id INT,
    attendance_date DATE,
    attendance_status ENUM('Present', 'Absent', 'Late', 'On Leave'),
    check_in_time TIME,
    check_out_time TIME,
    comments TEXT,
    FOREIGN KEY (staff_id) REFERENCES staff_information(staff_id)
);