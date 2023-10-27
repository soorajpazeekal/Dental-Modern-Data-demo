from faker import Faker
import logging as log
import random
from datetime import datetime, timedelta

log.basicConfig(level=log.INFO)
fake = Faker()

def staff_information(conn):
    cursor = conn.cursor()
    staff_id = random.randint(1000, 99999)
    full_name = random.choice(('Dr Saif Downs', 'Dr Lydia Fry', 'Dr Inaaya Keller', 'Dr Caleb Merrill',
                                  'Dr Oakley Brock', 'Dr Alexandra Woodward', 'Dr Leonardo Fisher',
                                  'Dr Louise Santana', 'Dr Evan Frank', 'Dr Helen Smith', 'Dr John Doe'))
    date_of_birth = fake.date_of_birth(tzinfo=None, minimum_age=25, maximum_age=60)
    gender = random.choice(['Male', 'Female'])
    contact_number = fake.phone_number()
    email = fake.email()
    address = fake.street_address()
    city = fake.city()
    state = fake.state()
    zip_code = fake.zipcode()
    position = random.choice(('Junior Staff', 'Staff', 'Senior Staff', 'Assistant', 'Head'
                              'Junior Staff', 'Staff','Junior Staff', 'Staff','Junior Staff', 'Assistant',
                              'Assistant', 'Assistant', 'Assistant', 'Assistant', 'Assistant', 'Assistant'))
    department = random.choice(('Endodontics', 'Periodontology', 'Orthodontics', 
                                'Dental public', 'health Pediatric', 'dentistry',
                                'Oral pathology', 'Prosthodontics', 'Orthopedics Restorative dentis'))
    hire_date = fake.date_time_between(start_date='-20y', end_date='now')
    salary = round(random.uniform(30000, 90000), 2)  # Generate a random decimal salary
    additional_notes = fake.text()

    insert_query = """INSERT INTO staff_information (staff_id, full_name, date_of_birth, gender, 
                        contact_number, email, address, city, state, zip_code, position, department, 
                        hire_date, salary, additional_notes)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
    data = (staff_id, full_name, date_of_birth, gender, contact_number, email, address, 
            city, state, zip_code, position, department, hire_date, salary, additional_notes)
    cursor.execute(insert_query, data)
    conn.commit()
    cursor.close()
    log.info("Staff information added successfully")
    return staff_id, hire_date


def salary_history(conn, staff_id, hire_date):
    cursor = conn.cursor()
    staff_id = staff_id
    effective_date = fake.date_between_dates(date_start=hire_date, date_end='now')
    old_salary = round(random.uniform(30000, 90000), 2)
    new_salary = round(old_salary * (1 + random.uniform(0.01, 0.10)), 2)  # Adjusted salary based on a percentage increase
    salary_adjustment_reason = fake.sentence()
    salary_adjustment_type = random.choice(['Promotion', 'Annual Raise', 'Performance Bonus'])
    salary_adjustment_percentage = round((new_salary - old_salary) / old_salary * 100, 2)
    tax_deductions = round(random.uniform(500, 2000), 2)
    bonus_amount = round(random.uniform(500, 2000), 2)
    review_comments = fake.text()
    additional_notes = fake.text()

    insert_query = """INSERT INTO salary_history (staff_id, effective_date, old_salary, new_salary, 
                        salary_adjustment_reason, salary_adjustment_type, salary_adjustment_percentage, 
                        tax_deductions, bonus_amount, review_comments, additional_notes)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
    data = (staff_id, effective_date, old_salary, new_salary, salary_adjustment_reason, 
            salary_adjustment_type, salary_adjustment_percentage, tax_deductions, bonus_amount, 
            review_comments, additional_notes)
    cursor.execute(insert_query, data)
    conn.commit()
    cursor.close()
    log.info("Salary history added successfully")
    return staff_id, effective_date


def attendance_records(conn, staff_id):
    cursor = conn.cursor()
    staff_id = staff_id
    attendance_date = fake.date_time_between(start_date='-1y', end_date='-30d')
    attendance_status = random.choice(['Present', 'Absent', 'Late', 'On Leave'])
    
    if attendance_status == 'Present' or attendance_status == 'Late':
        # Generate check-in time for staff who are present or arrived late
        check_in_time = fake.time(pattern='%H:%M:%S', end_datetime=datetime(2023, 1, 1, 10, 0, 0))
    else:
        check_in_time = None
    
    if attendance_status == 'Present':
        # Generate check-out time for staff who are present
        check_out_time = fake.time(pattern='%H:%M:%S', end_datetime=datetime(2023, 1, 1, 18, 0, 0))
    else:
        check_out_time = None
    
    comments = fake.text()

    insert_query = """INSERT INTO attendance_records (staff_id, attendance_date, attendance_status, check_in_time, 
                    check_out_time, comments)
             VALUES (%s, %s, %s, %s, %s, %s);"""
    data = (staff_id, attendance_date, attendance_status, check_in_time, check_out_time, comments)
    cursor.execute(insert_query, data)
    conn.commit()
    cursor.close()
    log.info("Attendance records added successfully")
    return 'ok'