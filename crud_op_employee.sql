
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
+-------------------+
| Tables_in_samsung |
+-------------------+
| employees         |
+-------------------+
1 row in set (0.01 sec)

mysql> USE samsung;
Database changed
mysql> UPDATE employees
    -> SET salary = new_salary, technology = 'new_technology'
    -> WHERE id = specific_id;
ERROR 1054 (42S22): Unknown column 'specific_id' in 'where clause'
mysql> UPDATE employees
    -> SET salary = 60000, technology = 'Java'
    -> WHERE id = 1;
ERROR 1054 (42S22): Unknown column 'technology' in 'field list'
mysql> show database
    -> SHOW TABLES;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'database
SHOW TABLES' at line 1
mysql> CREATE TABLE IF NOT EXISTS persons (
    ->     id INT PRIMARY KEY AUTO_INCREMENT,
    ->     name VARCHAR(50) NOT NULL,
    ->     gender VARCHAR(2),
    ->     location VARCHAR(50),
    ->     age INT CHECK(age > 0)
    -> );
Query OK, 0 rows affected (0.04 sec)

mysql> CREATE TABLE IF NOT EXISTS employees (
    ->     id INT PRIMARY KEY AUTO_INCREMENT,
    ->     name VARCHAR(50) NOT NULL,
    ->     designation VARCHAR(40) NOT NULL,
    ->     technology VARCHAR(30) NOT NULL,
    ->     phone_num BIGINT UNIQUE,
    ->     commission INT,
    ->     salary FLOAT DEFAULT 0,
    ->     years_of_exp INT
    -> );
Query OK, 0 rows affected, 1 warning (0.00 sec)

mysql> INSERT INTO persons (name, gender, location, age) VALUES
    -> ('Alice', 'F', 'Hubballi', 25),
    -> ('Bob', 'M', 'Dharwad', 30),
    -> ('Charlie', 'M', 'Belagavi', 22),
    -> ('David', 'M', 'Hubballi', 17),
    -> ('Eva', 'F', 'Dharwad', 19);
Query OK, 5 rows affected (0.01 sec)
Records: 5  Duplicates: 0  Warnings: 0

mysql> INSERT INTO employees (name, designation, technology, phone_num, commission, salary, years_of_exp) VALUES
    -> ('John Doe', 'Developer', 'Java', 9876543210, 1000, 60000, 5),
    -> ('Jane Smith', 'Designer', 'JavaScript', 9876543211, 800, 55000, 3),
    -> ('Alice Brown', 'Developer', 'Python', 9876543212, 1200, 70000, 4),
    -> ('Bob White', 'Manager', 'C#', 9876543213, 1500, 80000, 7),
    -> ('Charlie Green', 'Designer', 'HTML/CSS', 9876543214, 600, 50000, 2);
ERROR 1054 (42S22): Unknown column 'technology' in 'field list'
mysql> DESCRIBE employees;
+---------------------+-------------+------+-----+---------+----------------+
| Field               | Type        | Null | Key | Default | Extra          |
+---------------------+-------------+------+-----+---------+----------------+
| id                  | int         | NO   | PRI | NULL    | auto_increment |
| name                | varchar(30) | NO   |     | NULL    |                |
| designation         | varchar(30) | NO   |     | NULL    |                |
| location            | varchar(30) | YES  |     | NULL    |                |
| phone_number        | bigint      | YES  | UNI | NULL    |                |
| salary              | float       | YES  |     | 0       |                |
| commission          | int         | YES  |     | NULL    |                |
| years_of_experience | tinyint     | YES  |     | NULL    |                |
+---------------------+-------------+------+-----+---------+----------------+
8 rows in set (0.02 sec)

mysql> ALTER TABLE employees ADD technology VARCHAR(30) NOT NULL;
Query OK, 0 rows affected (0.03 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> INSERT INTO employees (name, designation, technology, phone_number, commission, salary, years_of_experience) VALUES
    -> ('John Doe', 'Developer', 'Java', 9876543210, 1000, 60000, 5),
    -> ('Jane Smith', 'Designer', 'JavaScript', 9876543211, 800, 55000, 3),
    -> ('Alice Brown', 'Developer', 'Python', 9876543212, 1200, 70000, 4),
    -> ('Bob White', 'Manager', 'C#', 9876543213, 1500, 80000, 7),
    -> ('Charlie Green', 'Designer', 'HTML/CSS', 9876543214, 600, 50000, 2);
Query OK, 5 rows affected (0.01 sec)
Records: 5  Duplicates: 0  Warnings: 0

mysql> UPDATE employees
    -> SET salary = 75000, technology = 'C++'
    -> WHERE id = 1;  -- Change the id to the specific employee you want to update
Query OK, 1 row affected (0.01 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> ALTER TABLE persons
    -> MODIFY location VARCHAR(50) NOT NULL;
Query OK, 0 rows affected (0.06 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> ALTER TABLE employees
    -> MODIFY commission FLOAT;
Query OK, 5 rows affected (0.04 sec)
Records: 5  Duplicates: 0  Warnings: 0

mysql> DELETE FROM employees
    -> WHERE designation = 'Designer';
Query OK, 2 rows affected (0.01 sec)

mysql> DELETE FROM employees
    -> WHERE id = 2;  -- Change the id to the specific employee you want to delete
Query OK, 0 rows affected (0.00 sec)

mysql> SELECT * FROM persons
    -> WHERE id = 1;  -- Change the id to the specific person you want to search for
+----+-------+--------+----------+------+
| id | name  | gender | location | age  |
+----+-------+--------+----------+------+
|  1 | Alice | F      | Hubballi |   25 |
+----+-------+--------+----------+------+
1 row in set (0.00 sec)

mysql> SELECT * FROM employees
    -> WHERE designation = 'Developer';  -- Change the designation as needed
+----+-------------+-------------+----------+--------------+--------+------------+---------------------+------------+
| id | name        | designation | location | phone_number | salary | commission | years_of_experience | technology |
+----+-------------+-------------+----------+--------------+--------+------------+---------------------+------------+
|  1 | John Doe    | Developer   | NULL     |   9876543210 |  75000 |       1000 |                   5 | C++        |
|  3 | Alice Brown | Developer   | NULL     |   9876543212 |  70000 |       1200 |                   4 | Python     |
+----+-------------+-------------+----------+--------------+--------+------------+---------------------+------------+
2 rows in set (0.00 sec)

mysql> SELECT designation, AVG(salary) AS average_salary
    -> FROM employees
    -> GROUP BY designation;
+-------------+----------------+
| designation | average_salary |
+-------------+----------------+
| Developer   |          72500 |
| Manager     |          80000 |
+-------------+----------------+
2 rows in set (0.00 sec)

mysql> SELECT technology, SUM(salary) AS total_salary
    -> FROM employees
    -> GROUP BY technology;
+------------+--------------+
| technology | total_salary |
+------------+--------------+
| C++        |        75000 |
| Python     |        70000 |
| C#         |        80000 |
+------------+--------------+
3 rows in set (0.00 sec)

mysql> SELECT *, (commission + salary) AS Total_salary
    -> FROM employees;
+----+-------------+-------------+----------+--------------+--------+------------+---------------------+------------+--------------+
| id | name        | designation | location | phone_number | salary | commission | years_of_experience | technology | Total_salary |
+----+-------------+-------------+----------+--------------+--------+------------+---------------------+------------+--------------+
|  1 | John Doe    | Developer   | NULL     |   9876543210 |  75000 |       1000 |                   5 | C++        |        76000 |
|  3 | Alice Brown | Developer   | NULL     |   9876543212 |  70000 |       1200 |                   4 | Python     |        71200 |
|  4 | Bob White   | Manager     | NULL     |   9876543213 |  80000 |       1500 |                   7 | C#         |        81500 |
+----+-------------+-------------+----------+--------------+--------+------------+---------------------+------------+--------------+
3 rows in set (0.00 sec)