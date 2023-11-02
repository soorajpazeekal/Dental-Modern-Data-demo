/*
    Creating ready to use tables from raw_landing zone 
*/
{{ config(materialized='table') }}

with __track_patient_informations as (
    SELECT CONCAT(FIRST_NAME, ' ', LAST_NAME) AS FULL_NAME, GENDER, DATE_OF_BIRTH, PHONE_NUMBER, EMAIL, STATE, REGISTRATION_DATE
    FROM RAW_BRONZE.PI_INFORMATIONS
)

SELECT * FROM __track_patient_informations

