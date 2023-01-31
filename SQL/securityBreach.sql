CREATE PROCEDURE solution()
BEGIN
	SELECT * FROM users 
	WHERE attribute LIKE BINARY concat('_%\%',first_name,'\_',second_name,'\%%');
END
/*
The LIKE operator is used in a WHERE clause to search for a specified pattern in a column.
The MySQL BINARY function is used for converting a value to a binary string.
The CONCAT() function adds two or more expressions together.

There are two wildcards often used in conjunction with the LIKE operator:

 The percent sign (%) represents zero, one, or multiple characters
 The underscore sign (_) represents one, single character

\%	Represents a single actual percent sign or just %
\_	Represents a single underscore character or just _
 */
