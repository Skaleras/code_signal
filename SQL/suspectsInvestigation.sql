CREATE PROCEDURE solution()
BEGIN
	SELECT id, name, surname FROM Suspect 
	WHERE height<=170 
		AND LOWER(name) LIKE 'b%'
		AND LOWER(surname) LIKE 'gre_n'
	ORDER BY id ASC;
END

/* The LOWER() function converts a string to lower-case. 

The LIKE operator is used in a WHERE clause to search for a specified pattern in a column.

There are two wildcards often used in conjunction with the LIKE operator:

 The percent sign (%) represents zero, one, or multiple characters
 The underscore sign (_) represents one, single character
*/
