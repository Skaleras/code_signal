CREATE PROCEDURE solution()
BEGIN
	SELECT id, name, surname
	FROM Suspect
	WHERE NOT(height > 170
		AND LOWER(name)  LIKE 'b%'
		AND LOWER(surname)  LIKE 'gre_n')
	ORDER BY id ASC;
END
