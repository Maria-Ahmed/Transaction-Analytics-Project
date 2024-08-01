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

## Transaction Analysis
### Objectives
1- Compute a Data Warehouse (DWH) table for transactions. For each user transaction, calculate the number of transactions the user had within the previous seven days.

### SQL Query
```schema
   CREATE TABLE transactions (
        transaction_id UUID,
        date DATE,
        user_id UUID,
        is_blocked BOOL,
        transaction_amount INTEGER,
        transaction_category_id INTEGER
);
   CREATE TABLE users (
        user_id UUID,
        is_active BOOLEAN
   ); ```

