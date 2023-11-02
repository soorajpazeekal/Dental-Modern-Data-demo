/*
    Question: 
    Customer Demographics:
    What is the distribution of patients by gender in our database?
    How many patients do we have in each state?
    What is the average age of our patients based on their date of birth?
*/

with main_table as (
    SELECT GENDER, COUNT(*) as COUNT
    FROM RAW_BRONZE.PI_INFORMATIONS
    GROUP BY GENDER
    UNION ALL
    SELECT STATE, COUNT(*) as COUNT
    FROM RAW_BRONZE.PI_INFORMATIONS
    GROUP BY STATE
)

SELECT * FROM main_table