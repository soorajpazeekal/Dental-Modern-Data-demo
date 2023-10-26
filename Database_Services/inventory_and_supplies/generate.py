from faker import Faker
import logging as log
import random, uuid
from datetime import datetime, timedelta


log.basicConfig(level=log.INFO)

def tr_inventory_supplies(conn):
    fake = Faker()
    cursor = conn.cursor()
    item_name = fake.unique.word()  # Generate a unique item name
    item_description = fake.paragraph()
    supplier_name = fake.company()
    purchase_date = fake.date_time_between(start_date='-2y', end_date='-60d')
    purchase_price = round(random.uniform(1000, 100000), 2)
    quantity = random.randint(1, 100)
    unit_of_measurement = random.choice(['kg', 'unit', 'liter', 'box', 'pack'])
    location = fake.word()
    minimum_stock = random.randint(5, 20)
    maximum_stock = random.randint(50, 100)
    last_restock_date = fake.date_between(start_date=purchase_date, end_date='today')
    additional_notes = fake.text()

    insert_query = """INSERT INTO table_inventory_and_supplies (item_name, item_description, supplier_name, 
                    purchase_date, purchase_price, quantity, unit_of_measurement, location, 
                    minimum_stock, maximum_stock, last_restock_date, additional_notes)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
    
    data = (item_name, item_description, supplier_name, purchase_date, purchase_price, quantity, 
            unit_of_measurement, location, minimum_stock, maximum_stock, last_restock_date, additional_notes)
    cursor.execute(insert_query, data)
    conn.commit()
    cursor.close()
    conn.close()
    log.info("inventory and supplies added successfully")
    return 'ok'


