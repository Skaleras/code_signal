CREATE PROCEDURE solution()
BEGIN
	SELECT name, id 
	FROM Grades 
	WHERE 2 * final > midterm1 + midterm2
	ORDER BY LEFT(name, 3) ASC, id ASC;
END

/* LEFT() function in MySQL is used to extract a specified number of characters 
from the left side of a given string. It uses its second argument to decide, how many characters it should return. */
