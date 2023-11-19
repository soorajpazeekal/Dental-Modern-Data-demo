FROM python:3.10

WORKDIR /patient_crm
COPY . /patient_crm

RUN pip install faker==19.12.0 mysql-connector-python==8.2.0 python-dotenv==1.0.0

WORKDIR /patient_crm
CMD ["nohup", "python", "bg_worker.py", ">", "script.log", "2>&1", "&"]