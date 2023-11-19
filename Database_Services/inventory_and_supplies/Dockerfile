FROM python:3.10

WORKDIR /inventory_and_supplies
COPY . /inventory_and_supplies

RUN pip install faker==19.12.0 mysql-connector-python==8.2.0 python-dotenv==1.0.0

WORKDIR /inventory_and_supplies
CMD ["nohup", "python", "bg_worker.py", ">", "script.log", "2>&1", "&"]