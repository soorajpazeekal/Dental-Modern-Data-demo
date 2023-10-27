from faker import Faker
import logging as log
import random, uuid
from datetime import datetime, timedelta


log.basicConfig(level=log.INFO)

def tr_invoice(conn):
    fake = Faker()
    cursor = conn.cursor()
    invoice_id = uuid.uuid4() 
    patient_id = random.randint(1000, 99999)
    invoice_date = fake.date_time_between(start_date='-30d', end_date='now')
    due_date = invoice_date + timedelta(days=30)
    total_amount = round(random.uniform(100, 5000), 2)
    payment_status = random.choice(['Unpaid', 'Paid', 'Partially Paid'])
    billing_address = fake.street_address()
    billing_city = fake.city()
    billing_state = fake.state()
    billing_zip_code = fake.zipcode()
    itemized_details = fake.text()
    insert_query = """INSERT INTO invoices (invoice_id, patient_id, invoice_date, 
                     due_date, total_amount, payment_status, billing_address, billing_city, billing_state, 
                     billing_zip_code, itemized_details)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
    
    data = (str(invoice_id), patient_id, invoice_date, due_date, 
            total_amount, payment_status, billing_address, billing_city, billing_state, 
            billing_zip_code, itemized_details)
    cursor.execute(insert_query, data)
    conn.commit()
    cursor.close()
    log.info("Invoice added successfully")
    return invoice_id, patient_id, total_amount


def tr_payment_records(conn, invoice_id, patient_id, total_amount):
    cursor = conn.cursor()
    fake = Faker()
    patient_id = patient_id
    invoice_id = invoice_id
    payment_date = fake.date_time_between(start_date='-15d', end_date='now')
    payment_amount = total_amount
    payment_method = fake.word(ext_word_list=['Credit Card', 'Cash', 'Check', 'Online Payment'])
    transaction_reference = fake.lexify(text='??????#####')
    payment_status = random.choice(['Success', 'Pending', 'Failed'])
    additional_notes = random.choice(['All settled', 'Partially settled', 'Pending', 'Insured'])
    insert_query = """INSERT INTO payment_records (patient_id, invoice_id, payment_date, 
                        payment_amount, payment_method, transaction_reference, payment_status, additional_notes)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"""
        
    data = (patient_id, str(invoice_id), payment_date, payment_amount, payment_method, 
                transaction_reference, payment_status, additional_notes)
    cursor.execute(insert_query, data)
    conn.commit()
    cursor.close()
    conn.close()
    log.info("Payment record added successfully")
