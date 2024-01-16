FROM python:3.10

WORKDIR /Dental-Modern-Data-demo
COPY . /Dental-Modern-Data-demo

RUN pip install -r ./Database_Services/requirements.txt

WORKDIR /Dental-Modern-Data-demo/Database_Services/billing_and_payment

CMD ["nohup", "python", "bg_worker.py", ">", "script.log", "2>&1", "&"]

WORKDIR /Dental-Modern-Data-demo/Database_Services/inventory_and_supplies
CMD ["nohup", "python", "bg_worker.py", ">", "script.log", "2>&1", "&"]


WORKDIR /Dental-Modern-Data-demo/Database_Services/patient_crm
CMD ["nohup", "python", "bg_worker.py", ">", "script.log", "2>&1", "&"]


WORKDIR /Dental-Modern-Data-demo/Database_Services/staff_management
CMD ["nohup", "python", "bg_worker.py", ">", "script.log", "2>&1", "&"]
