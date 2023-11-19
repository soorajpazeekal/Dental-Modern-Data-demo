FROM python:3.10

WORKDIR /staff_management
COPY . /staff_management

RUN pip install faker==19.12.0 mysql-connector-python==8.2.0 python-dotenv==1.0.0

WORKDIR /staff_management
CMD ["nohup", "python", "bg_worker.py", ">", "script.log", "2>&1", "&"]