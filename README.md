# Transaction-Analytics-Project

This repository contains solutions for analyzing transactional and user data stored in a database. The project involves writing SQL queries to derive insights and a Python program to compute results from CSV files.

## Table of Contents
- [Overview](#overview)
- [Setup](#setup)
- [SQL Query for Transaction Analysis](#sql-query-for-transaction-analysis)
- [Python Script for Data Aggregation](#python-script-for-data-aggregation)

## Overview
This project demonstrates how to analyze transaction data to gain meaningful insights. It includes:
1. A SQL query to compute the number of transactions a user had within the previous seven days.
2. A Python program to aggregate and analyze data from CSV files.

## Setup
1. Clone the repository:
    ```bash
    git clone https://github.com/Maria-Ahmed/Transaction-Analytics-Project.git
    cd Transaction-Analytics-Project
    ```
2. Generate example data:
    ```bash
    python generate_data.py
    ```
3. Ensure you have the necessary CSV files (`transactions.csv` and `users.csv`) in the repository directory.

## SQL Query for Transaction Analysis
### Objective
Compute a Data Warehouse (DWH) table for transactions. For each user transaction, calculate the number of transactions the user had within the previous seven days.

### SQL Query
```sql
SELECT 
    t1.transaction_id,
    t1.user_id,
    t1.date,
    COUNT(t2.transaction_id) AS no_txn_last_7days
FROM 
    transactions t1
LEFT JOIN 
    transactions t2 
ON 
    t1.user_id = t2.user_id 
    AND t2.date BETWEEN t1.date - INTERVAL '7 DAY' AND t1.date - INTERVAL '1 DAY'
GROUP BY 
    t1.transaction_id, t1.user_id, t1.date
ORDER BY 
    t1.user_id, t1.date;
