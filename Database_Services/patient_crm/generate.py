from faker import Faker
import logging as log
import random


#log.basicConfig(level=log.INFO)
fake = Faker()

def add_pi_informations(conn):
    cursor = conn.cursor()
    patient_id = random.randint(10000, 99999)
    first_name = fake.first_name()
    last_name = fake.last_name()
    date_of_birth = fake.date_of_birth(minimum_age=10, maximum_age=80)
    gender = random.choice(['Male', 'Female', 'Other'])
    phone_number = fake.phone_number()
    email = fake.email()
    address = fake.address()
    city = fake.city()
    state = fake.state()
    zip_code = fake.zipcode()
    registration_date = fake.date_time_between(start_date='-2y', end_date='now')

    insert_query = """INSERT INTO pi_informations (patient_id, first_name, last_name, date_of_birth, 
                        gender, phone_number, email, address, city, state, zip_code, registration_date)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    data = (patient_id, first_name, last_name, date_of_birth, gender, 
            phone_number, email, address, city, state, zip_code, registration_date)
    cursor.execute(insert_query, data)
    conn.commit()
    log.info("Patient information added successfully")
    return patient_id, date_of_birth


def add_medical_history(conn, patient_id):
    cursor = conn.cursor()
    medical_condition = random.choice(('Healthy', 'Unhealthy', 'Critical', 'None'))
    diagnosis_date = fake.date_time_between(start_date='-2y', end_date='now')
    treatment_description = fake.paragraph(nb_sentences=3)
    attending_physician = random.choice(('Dr Louise Santana', 'Dr Evan Frank', 'Dr Helen Smith', 'Dr John Doe'))
    insert_query = """INSERT INTO medical_history (patient_id, medical_condition, diagnosis_date, 
                    treatment_description, attending_physician) 
                    VALUES (%s, %s, %s, %s, %s)"""
    data = (patient_id, medical_condition, diagnosis_date, treatment_description, attending_physician)

    cursor.execute(insert_query, data)
    conn.commit()
    log.info("Medical history added successfully")

def add_dental_records(conn, patient_id):
    cursor = conn.cursor()  
    patient_id = patient_id
    appointment_date = fake.date_between(start_date='-1y', end_date='now')
    procedure_name = random.choice(('Normal Tooth Extraction', 'Root Canal', 'Cosmetic Dentistry'
                                   , 'Dental Fillings', 'Dental Implants', 'Orthodontics'))
    booth_number = random.randint(1, 10)
    description = fake.paragraph(nb_sentences=2)
    dentist_name = random.choice(('Dr Saif Downs', 'Dr Lydia Fry', 'Dr Inaaya Keller', 'Dr Caleb Merrill',
                                  'Dr Oakley Brock', 'Dr Alexandra Woodward', 'Dr Leonardo Fisher'))
    insert_query = """INSERT INTO dental_records (patient_id, appointment_date, procedure_name, 
                    booth_number, description, dentist_name) 
                    VALUES (%s, %s, %s, %s, %s, %s)"""
    data = (patient_id, appointment_date, procedure_name, booth_number, description, dentist_name)

    cursor.execute(insert_query, data)
    conn.commit()
    log.info("Dental records added successfully")

def add_insurance_information(conn, patient_id, date_of_birth):
    cursor = conn.cursor()
    patient_id = patient_id
    insurance_provider = random.choice(('United Health', 'Anthem Inc', 'Centene Corporation', 
                                        'Blue Cross Blue Shield of California', 'CIGNA', 'Caresource',
                                        'UPMC Health System', 'Carefirst Inc', 'Health Net of California',
                                        'Point32Health'))
    policy_number = fake.unique.random_int(min=100000, max=999999)
    policy_start_date = fake.date_between(start_date='-10y', end_date='now')
    policy_end_date = fake.future_date(end_date='+5y')
    policy_type = random.choice(('Full Cover', 'Partial Cover', 'lerm Cover', 'None'))
    policy_holder_name = patient_id
    policy_holder_relation = random.choice(('Self', 'Spouse', 'Child', 'Parent'))
    policy_holder_date_of_birth = date_of_birth
    insert_query = """INSERT INTO insurance_information (patient_id, insurance_provider, 
    policy_number, policy_start_date, policy_end_date, policy_type, policy_holder_name, 
    policy_holder_relation, policy_holder_date_of_birth)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    data = (patient_id, insurance_provider, policy_number, 
            policy_start_date, policy_end_date, policy_type, policy_holder_name, 
            policy_holder_relation, policy_holder_date_of_birth)
    cursor.execute(insert_query, data)
    conn.commit()
    conn.close()
    log.info("Insurance information added successfully")

