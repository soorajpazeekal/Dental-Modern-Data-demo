
# Module title

Please follow these steps to deploy 'database-services'



## Deployment

This module requires python 3.10, docker-ce, compose, python-pip

```bash
  sudo apt-get install python-is-python3
  sudo apt install python3-pip
  docker ps - check 
```
under 'Database_Services'
```bash
    pip install -r requirements.txt
    cd <any of the services> eg: cd billing_and_payment
```
prepare .env with these values and save
```env
    MYSQL_USER = <any>
    MYSQL_PASSWORD = <password>
    MYSQL_ROOT_PASSWORD = <password>
    MYSQL_DATABASE = billing_and_payment
```
```bash
    docker compose up -d
    if using linux vm use 'sudo'
```
Finally double check health status:
```bash
    docker ps
``` 
Start worker:
```bash
    nohup python bg_worker.py > script.log 2>&1 &
``` 
```bash
    ps aux | grep bg_worker.py
    kill -9 <p-id>
``` 