/*We want to compute a DWH table for transactions. 
For every user transaction, it should compute the number of transactions the user had within the previous seven days.*/

SELECT 
    t.transaction_id,
    t.user_id,
    t.date,
    COUNT(*) OVER (PARTITION BY t.user_id ORDER BY t.date RANGE BETWEEN INTERVAL '7' DAY PRECEDING AND CURRENT ROW) AS no_txn_last_7days
FROM 
    transactions t
JOIN 
    users u ON t.user_id = u.user_id
WHERE 
    u.is_active = TRUE
ORDER BY 
    t.user_id, t.date;



Indexing: The database might use indexes on the date column of the transactions
 table to efficiently retrieve rows within the specified date range. 
 Indexes on the user_id column might also be beneficial for partitioning and joining
  data efficiently.

Filtering Active Users: The condition u.is_active = TRUE might be optimized using an
 index on the is_active column of the users table, especially if there are many 
 inactive users.
 