mysql> CREATE DATABASE samsung;
Query OK, 1 row affected (0.03 sec)

mysql> USE samsung;
Database changed
mysql> CREATE TABLE IF NOT EXISTS employees (
    ->     id INT PRIMARY KEY AUTO_INCREMENT,
    ->     name VARCHAR(30) NOT NULL,
    ->     designation VARCHAR(30) NOT NULL,
    ->     location VARCHAR(30),
    ->     phone_number BIGINT UNIQUE,
    ->     salary FLOAT DEFAULT 0,
    ->     commission INT,
    ->     years_of_experience TINYINT
    -> );
Query OK, 0 rows affected (0.04 sec)

mysql> SHOW TABLES;