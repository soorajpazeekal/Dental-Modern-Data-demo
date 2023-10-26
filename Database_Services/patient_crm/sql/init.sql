CREATE TABLE IF NOT EXISTS pi_informations (
    patient_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    gender ENUM('Male', 'Female', 'Other') NOT NULL,
    phone_number VARCHAR(30) NOT NULL,
    email VARCHAR(100),
    address VARCHAR(255) NOT NULL,
    city VARCHAR(50) NOT NULL,
    state VARCHAR(50) NOT NULL,
    zip_code VARCHAR(10) NOT NULL,
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS medical_history (
    patient_id INT PRIMARY KEY,
    medical_condition VARCHAR(255),
    diagnosis_date DATE,
    treatment_description TEXT,
    attending_physician VARCHAR(100),
    CONSTRAINT FK_patient_id FOREIGN KEY (patient_id) REFERENCES pi_informations(patient_id)
);

CREATE TABLE IF NOT EXISTS dental_records (
    patient_id INT,
    appointment_date DATE,
    procedure_name VARCHAR(100),
    booth_number INT,
    description TEXT,
    dentist_name VARCHAR(100),
    PRIMARY KEY (patient_id),
    FOREIGN KEY (patient_id) REFERENCES pi_informations(patient_id)
);

CREATE TABLE IF NOT EXISTS insurance_information (
    patient_id INT PRIMARY KEY,
    insurance_provider VARCHAR(100),
    policy_number VARCHAR(50),
    policy_start_date DATE,
    policy_end_date DATE,
    policy_type VARCHAR(50),
    policy_holder_name VARCHAR(100),
    policy_holder_relation VARCHAR(50),
    policy_holder_date_of_birth DATE,
    FOREIGN KEY (patient_id) REFERENCES pi_informations(patient_id)
);

