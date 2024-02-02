  

# Dental-Modern-Data-demo

## Overview


This repository contains a data engineering proof-of-concept project designed for a US-based dental software startup. The project focuses on implementing a robust data pipeline to seamlessly transfer data from various services within the startup to a centralized data warehouse.


Moving away from their current manual data tools, which are known for their time-consuming and complex processes, offers significant advantages. A more automated and intuitive solution would not only streamline their workflow but also empower them to analyze and utilize their data with greater speed and accuracy. This shift would enhance their overall productivity, unlock valuable insights, and ultimately drive better decision-making.

  


## Project Objectives


1.  **Data Integration:** The primary goal is to establish a smooth data flow between different services, ensuring comprehensive coverage of the startup's operations.

- Implement a standardized data ingestion and transformation process to ensure data consistency and accessibility.

- Address any challenges related to data heterogeneity, volume, and velocity.

2.  **Schedule and monitoring:**

- Develop a comprehensive scheduling mechanism for data ingestion, transformation, and loading processes.

- Implement robust monitoring and alerting systems to track pipeline performance, identify errors, and ensure timely data delivery.

3.  **Data Quality and Validation:**

- Implement rigorous data quality checks at every stage of the pipeline to ensure accuracy, completeness, consistency, and validity.

- Establish data validation rules and procedures to prevent the introduction of invalid or corrupt data.

4.  **Centralized Data Warehouse:**

- Design and build a centralized data warehouse to consolidate and store integrated, high-quality data from various sources.

- Choose an appropriate data warehouse architecture that aligns with project requirements and scalability needs.

- Consider using cloud-based data warehousing solutions to enhance scalability and cost-effectiveness.

  
  

## Data Architecture

### Current architecture

![Architecture Screenshot](https://raw.githubusercontent.com/soorajpazeekal/Dental-Modern-Data-demo/main/doc/fundamental-step.png)


### Modern Architecture

![Architecture Screenshot](https://raw.githubusercontent.com/soorajpazeekal/Dental-Modern-Data-demo/main/doc/new-data-modern.png)

  

### Demo

[screen-capture.webm](https://github.com/soorajpazeekal/Dental-Modern-Data-demo/assets/41431605/998e1be7-bd6a-40d1-bcd0-3a879827386e)

## Tech & Prerequisites

- [Pyspark](https://spark.apache.org/docs/3.3.2/api/python/index.html)

- Aws Data stack and RDS

- [Snowflake](https://www.snowflake.com/en/)

- [greatexpectations](https://greatexpectations.io)

- [Github Actions](https://github.com/features/actions)

- [Data Bulid Tool (DBT)](https://www.getdbt.com/)

- [Docker Compose](https://docs.docker.com/compose/)
  

## Installation 

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/soorajpazeekal/Dental-Modern-Data-demo)

To run this project:  

**1 .First Clone this repo and select project directory**

```bash
git clone  https://github.com/soorajpazeekal/Dental-Modern-Data-demo.git
cd Dental-Modern-Data-demo
```


**2. Prepare .env and .ini files.**

- Open '.env.example' file and rename to .env with:

```env
MYSQL_USER = admin
MYSQL_PASSWORD = password
MYSQL_ROOT_PASSWORD = password
MYSQL_ALLOW_PUBLIC_KEY_RETRIEVAL = True
```

- After open directory called 'elt_jobs' and open file '.ini.example' and rename to '.ini with:'

***Note: Please check your database connectivity with the URL, username, and password. also add snowflake connection details with relevant options.***

```env

[global]
username = <root database username>
password = <root database password>
port = 3306

[cluster_01]
jdbc_url = jdbc:mysql://<ip>:3306/patient_crm
tables = pi_informations,medical_history,dental_records,insurance_information

[cluster_02]
jdbc_url = jdbc:mysql://<ip>:3306/billing_and_payment
tables = invoices,payment_records

[cluster_03]
jdbc_url = jdbc:mysql://<ip>:3306/staff_management
tables = staff_information,salary_history,attendance_records

[cluster_04]
jdbc_url = jdbc:mysql://<ip>:3306/inventory_and_supplies
tables = table_inventory_and_supplies

  

[sfOptions]
sfURL = <Snowflake url>
sfUser = <Snowflake username>
sfPassword = <Snowflake password>
sfDatabase = <Snowflake database>
sfSchema = <Snowflake schema name>
sfWarehouse = <Snowflake sWarehouse name>

```

**3. Encrypt the configuration file (added security for using github actions and repos publicly).**

*Note: This is an optional one! but highly recommend it if you are running locally. (Run this command with in 'elt_jobs' Folder)*

  

```bash

openssl enc  -aes-256-cbc  -salt  -in  .ini  -out  config.enc  -pbkdf2  -k <public_key> #Any string

```

**Note:** This project can be installed in different ways:

- Cloud environment (Using AWS)
- Standalone locally (Follow the instructions below)


```bash
docker compose  up  -d
docker ps
```


It will spin up Docker with MySQL containers and other required dependencies for the project.
After starting, please verify container health with 'docker ps'.


**Note:** This proof-of-concept has two different parts:

Database services

- This part mainly works with database services. also generate data for the live simulation of this project.

- After generating data, this service automatically writes it to the database.

- It used Python, the [Faker Library](https://faker.readthedocs.io/en/master/), and some other random algorithms to generate mock data for this simulation.

Main Data Services

- It will manage and monitor data pipelines using GitHub actions.

- Write to the Snowflake staging zone and perform data quality and validations.

- using data-building tool to move data between different layers ([medallion architecture](https://www.databricks.com/glossary/medallion-architecture))


**4. Install act (To run Github actions locally, this project uses [act](https://github.com/nektos/act) ~ Run your GitHub Actions locally 🚀 ~)**


```bash
curl -s  https://raw.githubusercontent.com/nektos/act/master/install.sh | sudo bash
```


***If you run this command in the project directory, Act will create a directory called 'bin' and install an executable file called ~act! [Please click this link for more info](https://github.com/nektos/act#example-commands)***



**5. Run 'act' it will automatically start this project**

***Note: run this command on root Folder of this project***

```bash

./bin/act -s  public_key=<public_key>

```

## Lessons Learned
**Modern Data Engineering:** Embracing modern practices ensured a robust, scalable, and maintainable data pipeline.

**Integration Challenges:** Navigated complexities by developing flexible solutions for diverse data formats.

**Software Engineering Principles:** Modular design, code reusability, and thorough documentation were key to efficiency.

**Balancing Quality and Business Needs:** Striking a cost-effective balance optimized resources without compromising quality.

**Continuous Monitoring:** Proactive monitoring and regular maintenance contributed to overall system stability.

  
  

## Contact

  

Please feel free to contact me if you have any questions at: LinkedIn: [![open Linkedin profile](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/soorajpazeekal)
