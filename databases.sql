SELECT * FROM Books ORDER BY Price DESC;
SELECT * FROM Books LIMIT 2;  -- MySQL syntax for top 2 records
SELECT * FROM Books LIMIT (SELECT COUNT(*) * 0.2 FROM Books);  -- Example for 20%
SELECT LEFT(BookName, 4) AS Short_BookName FROM Books;
SELECT UPPER(BookName) FROM Books;  -- Convert to uppercase
SELECT LOWER(BookName) AS "BOOK NAME" FROM Books;  -- Convert to lowercase
SELECT REVERSE(BookName) AS REVERSE_NAME FROM Books;  -- Reverse string
SELECT BookId, Publish_Date, DATE_ADD(Publish_Date, INTERVAL 1 YEAR) AS NEW_PUBLISH_DATE FROM Books;
SELECT BookId, Publish_Date, DAYNAME(Publish_Date) AS Weekday_Name FROM Books;
SELECT MIN(Price) AS 'MIN-PRICE' FROM Books;
SELECT AVG(Price) AS 'AVG-PRICE' FROM Books;
SELECT COUNT(*) AS 'COUNT OF RECORDS' FROM Books;
SELECT MIN(Price) AS 'MIN-PRICE' FROM Books;
SELECT AVG(Price) AS 'AVG-PRICE' FROM Books;
SELECT COUNT(*) AS 'COUNT OF RECORDS' FROM Books;
SELECT BookId, Price, 
       CASE 
           WHEN Price > 500 THEN 'Expensive'
           ELSE 'Affordable'
       END AS Price_Category
FROM Books;
CREATE TABLE Employee (
    EmpId INT PRIMARY KEY,
    EmpName VARCHAR(30) NOT NULL,
    EmpSal FLOAT,
    Bonus FLOAT,
    Dept VARCHAR(30)
);
INSERT INTO Employee VALUES (101, 'Harish', 35700, 560, 'Defence');
UPDATE Employee SET EmpSal = 40500 WHERE EmpId = 119;
DELETE FROM Employee WHERE EmpId = 101;
SELECT Dept, COUNT(*) AS Num_Of_Emps FROM Employee GROUP BY Dept HAVING COUNT(*) > 1;
SELECT * FROM Employee WHERE EmpSal > (SELECT AVG(EmpSal) FROM Employee);
	/* 3. insert -> guest_recharge  */
	SELECT @guest_id = SCOPE_IDENTITY()
	INSERT INTO guest_recharge(guest_id, recharge_amount) VALUES(@guest_id, @initial_recharge_amount);
	
	/* 4. update -> guest_base for balance_amount */
	UPDATE guest_base 
	SET balance_amount = balance_amount + @initial_recharge_amount
	WHERE guest_id = @guest_id
	IF 
	(SELECT COUNT(*) FROM zone_collection 
		WHERE DATEADD(dd, DATEDIFF(dd, 0, tran_date), 0) = DATEADD(dd, DATEDIFF(dd, 0, GETDATE()), 0)
	) = 0 
	BEGIN
		INSERT INTO zone_collection(amount) VALUES(@initial_recharge_amount);	
	END
	ELSE
	BEGIN
		UPDATE zone_collection SET amount = amount + @initial_recharge_amount
		WHERE DATEADD(dd, DATEDIFF(dd, 0, tran_date), 0) = DATEADD(dd, DATEDIFF(dd, 0, GETDATE()), 0); 
	END;
COMMIT;

	SELECT @guest_id = SCOPE_IDENTITY()
exec do_recharge @guest_id, @initial_recharge_amount
COMMIT;

	INSERT INTO guest_recharge(guest_id, recharge_amount) VALUES(@guest_id, @recharge_amount);
	--exec topup_wallet @guest_id, @recharge_amount
	-- Trigger runs this proc
commit;

	/* 4. update -> guest_base for balance_amount */
	UPDATE guest_base 
	SET balance_amount = balance_amount + @recharge_amount
	WHERE guest_id = @guest_id
	IF 
	(SELECT COUNT(*) FROM zone_collection 
		WHERE DATEADD(dd, DATEDIFF(dd, 0, tran_date), 0) = DATEADD(dd, DATEDIFF(dd, 0, GETDATE()), 0)
	) = 0 
	BEGIN
		INSERT INTO zone_collection(amount) VALUES(@recharge_amount);	
	END
	ELSE
	BEGIN
		UPDATE zone_collection SET amount = amount + @recharge_amount
		WHERE DATEADD(dd, DATEDIFF(dd, 0, tran_date), 0) = DATEADD(dd, DATEDIFF(dd, 0, GETDATE()), 0); 
	END;
	commit;

    SET @collection_amount = 0;
Open cur_guest_recharge;  
FETCH NEXT FROM cur_guest_recharge INTO @recharge_amount  
WHILE @@FETCH_STATUS = 0
	BEGIN  
		SET @collection_amount = @collection_amount + @recharge_amount
		FETCH NEXT FROM cur_guest_recharge INTO @recharge_amount  
	END  
  
CLOSE cur_guest_recharge  
DEALLOCATE cur_guest_recharge  

SELECT @collection_amount

SELECT amount 
from zone_collection 
where DATEDIFF(DD,0,tran_date) = DATEDIFF(DD,0,getdate());

SELECT ISNULL(SUM(recharge_amount),0) 
from guest_recharge   
WHERE DATEDIFF(DD,0,recharge_date) = DATEDIFF(DD,0,getdate());

SET @collection_amount = 0;
Open cur_guest_recharge;  -- cursor working starts
FETCH NEXT FROM cur_guest_recharge INTO @recharge_amount  
WHILE @@FETCH_STATUS = 0 -- system variables starts with @@
	BEGIN  
		SET @collection_amount = @collection_amount + @recharge_amount
		FETCH NEXT FROM cur_guest_recharge INTO @recharge_amount  
	END  
  
CLOSE cur_guest_recharge  -- cursor working ends here
DEALLOCATE cur_guest_recharge  -- delete from memory

SELECT @collection_amount -- output of the cursor

SELECT ISNULL(SUM(recharge_amount),0) 
from guest_recharge   
WHERE DATEDIFF(DD,0,recharge_date) = DATEDIFF(DD,0,getdate());

DECLARE @recharge_amount float;
DECLARE @guest_id int;
DECLARE @recharge_date DATETIME;
DECLARE @recharge_id int;
DECLARE cur_guest_recharge CURSOR -- No @ is used
			FAST_FORWARD -- type of cursor
				FOR  
	Select recharge_id, guest_id, recharge_date, recharge_amount 
	From guest_recharge 
	WHERE DATEDIFF(DD,0,recharge_date) = DATEDIFF(DD,0,getdate());

Open cur_guest_recharge;  -- cursor working starts
FETCH NEXT FROM cur_guest_recharge INTO @recharge_id, @guest_id, @recharge_date, @recharge_amount 
WHILE @@FETCH_STATUS = 0 -- system variables starts with @@
	BEGIN  
		insert into new_table(recharge_id, guest_id, recharge_date, recharge_amount)
			values (@recharge_id, @guest_id, @recharge_date, @recharge_amount);
			FETCH NEXT FROM cur_guest_recharge INTO @recharge_id, @guest_id, @recharge_date, @recharge_amount 
	END  
CLOSE cur_guest_recharge  -- cursor working ends here
DEALLOCATE cur_guest_recharge  -- delete from memory


CREATE TABLE IF NOT EXISTS employees (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(30) NOT NULL,
    designation VARCHAR(30) NOT NULL,
    location VARCHAR(30),
    phone_number BIGINT UNIQUE,
    salary FLOAT DEFAULT 0,
    commission INT,
    years_of_experience TINYINT
);

INSERT INTO employees (name, designation, location, phone_number, commission, salary, years_of_experience) VALUES
('John Doe', 'Developer', 'New York', 9876543210, 1000, 60000, 5),
('Jane Smith', 'Designer', 'Los Angeles', 9876543211, 800, 55000, 3);


SELECT name, designation FROM employees;

UPDATE employees SET salary = 38000 WHERE id = 1;

DELETE FROM employees WHERE id = 1;

CREATE VIEW employee_summary AS
SELECT designation, AVG(salary) AS average_salary
FROM employees
GROUP BY designation;

CREATE PROCEDURE AddEmployee(
    IN emp_name VARCHAR(30),
    IN emp_designation VARCHAR(30),
    IN emp_location VARCHAR(30),
    IN emp_phone BIGINT,
    IN emp_salary FLOAT
)
BEGIN
    INSERT INTO employees (name, designation, location, phone_number, salary)
    VALUES (emp_name, emp_designation, emp_location, emp_phone, emp_salary);
END;

DECLARE cur_employee CURSOR FOR SELECT name FROM employees;
OPEN cur_employee;
FETCH NEXT FROM cur_employee INTO @employee_name;
-- Process each row
CLOSE cur_employee;
DEALLOCATE cur_employee;

