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