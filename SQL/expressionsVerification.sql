CREATE PROCEDURE solution()
BEGIN
	SELECT * FROM expressions 
	WHERE elt(locate(operation, "+-*/"), a+b, a-b, a*b, a/b) = c;
END

/* MySQL ELT() returns the string at the index number specified in the list of arguments. The first argument indicates the index of the string to be retrieved from the list of arguments.
Syntax
ELT(index number, string1, string2, string3,…)

The LOCATE() function returns the position of the first occurrence of a substring in a string.
LOCATE(substring, string, start)*/
