/*
    Creating ready to use tables from raw_landing zone 
*/
{{ config(materialized='table') }}


with __track_payment_and_invoice as (
    SELECT 
        pr.PAYMENT_AMOUNT,
        pr.PAYMENT_METHOD,
        pr.PAYMENT_STATUS,
        i.TOTAL_AMOUNT,
        i.BILLING_STATE
    FROM RAW_BRONZE.PAYMENT_RECORDS pr
    JOIN RAW_BRONZE.INVOICES i ON pr.INVOICE_ID = i.INVOICE_ID
)

SELECT * FROM __track_payment_and_invoice