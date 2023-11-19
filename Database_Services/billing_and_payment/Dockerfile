FROM python:3.10

WORKDIR /billing_and_payment
COPY . /billing_and_payment

RUN pip install faker==19.12.0 mysql-connector-python==8.2.0 python-dotenv==1.0.0

WORKDIR /billing_and_payment
CMD ["nohup", "python", "bg_worker.py", ">", "script.log", "2>&1", "&"]