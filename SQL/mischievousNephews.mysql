CREATE PROCEDURE solution()
BEGIN
	SELECT WEEKDAY(mischief.`mischief_date`) AS `weekday`, mischief.*
	FROM mischief
	ORDER BY `weekday` ASC, 
			FIELD(mischief.author, 'Huey', 'Dewey', 'Louie'),
			mischief.`mischief_date`,
			mischief.`title` ASC;
END

/*The WEEKDAY() function returns the weekday number for a given date.
Note: 0 = Monday, 1 = Tuesday, 2 = Wednesday, 3 = Thursday, 4 = Friday, 5 = Saturday, 6 = Sunday.

FIELD() function :
This function in MySQL is used to return the index position of a specified value in a list of given values. 
For example, if the given list is (“3”, “1”, “2”) and the value is “1” for which index position is going to be search, 
then this function will return 2 as the index position.
*/
